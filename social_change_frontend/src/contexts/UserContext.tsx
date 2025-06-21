import React, { createContext, useContext, useState, useEffect, ReactNode } from 'react';
import { UserProfile, STORAGE_KEYS } from '../types';
import { apiService } from '../services/api';

interface UserContextType {
  user: UserProfile | null;
  isLoading: boolean;
  error: string | null;
  login: (profile: UserProfile) => Promise<void>;
  logout: () => void;
  updateProfile: (updates: Partial<UserProfile>) => Promise<void>;
  refreshUser: () => Promise<void>;
}

const UserContext = createContext<UserContextType | undefined>(undefined);

interface UserProviderProps {
  children: ReactNode;
}

export const UserProvider: React.FC<UserProviderProps> = ({ children }) => {
  const [user, setUser] = useState<UserProfile | null>(null);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  // Load user from localStorage on mount
  useEffect(() => {
    const loadUser = async () => {
      try {
        const savedUser = localStorage.getItem(STORAGE_KEYS.USER_PROFILE);
        const userId = localStorage.getItem(STORAGE_KEYS.USER_ID);

        if (savedUser && userId) {
          const parsedUser = JSON.parse(savedUser);
          setUser(parsedUser);
          
          // Optionally refresh user data from server
          try {
            const serverUser = await apiService.getUserProfile(userId);
            if (serverUser) {
              setUser(serverUser);
              localStorage.setItem(STORAGE_KEYS.USER_PROFILE, JSON.stringify(serverUser));
            }
          } catch (error) {
            console.warn('Could not refresh user from server, using cached data');
          }
        }
      } catch (error) {
        console.error('Error loading user from storage:', error);
        setError('Failed to load user data');
      } finally {
        setIsLoading(false);
      }
    };

    loadUser();
  }, []);

  const login = async (profile: UserProfile) => {
    try {
      setIsLoading(true);
      setError(null);

      // Create or update profile on server
      const savedProfile = await apiService.createOrUpdateProfile(profile);
      
      // Save to local storage
      localStorage.setItem(STORAGE_KEYS.USER_PROFILE, JSON.stringify(savedProfile));
      if (savedProfile.user_id) {
        localStorage.setItem(STORAGE_KEYS.USER_ID, savedProfile.user_id);
      }
      
      setUser(savedProfile);
    } catch (error) {
      console.error('Login error:', error);
      setError(error instanceof Error ? error.message : 'Failed to login');
      throw error;
    } finally {
      setIsLoading(false);
    }
  };

  const logout = () => {
    setUser(null);
    localStorage.removeItem(STORAGE_KEYS.USER_PROFILE);
    localStorage.removeItem(STORAGE_KEYS.USER_ID);
    localStorage.removeItem(STORAGE_KEYS.CONVERSATION_HISTORY);
  };

  const updateProfile = async (updates: Partial<UserProfile>) => {
    if (!user) {
      throw new Error('No user logged in');
    }

    try {
      setIsLoading(true);
      setError(null);

      const updatedProfile = { ...user, ...updates };
      const savedProfile = await apiService.createOrUpdateProfile(updatedProfile);
      
      // Update local storage
      localStorage.setItem(STORAGE_KEYS.USER_PROFILE, JSON.stringify(savedProfile));
      setUser(savedProfile);
    } catch (error) {
      console.error('Update profile error:', error);
      setError(error instanceof Error ? error.message : 'Failed to update profile');
      throw error;
    } finally {
      setIsLoading(false);
    }
  };

  const refreshUser = async () => {
    if (!user?.user_id) {
      return;
    }

    try {
      setIsLoading(true);
      setError(null);

      const serverUser = await apiService.getUserProfile(user.user_id);
      if (serverUser) {
        setUser(serverUser);
        localStorage.setItem(STORAGE_KEYS.USER_PROFILE, JSON.stringify(serverUser));
      }
    } catch (error) {
      console.error('Refresh user error:', error);
      setError(error instanceof Error ? error.message : 'Failed to refresh user data');
    } finally {
      setIsLoading(false);
    }
  };

  const value: UserContextType = {
    user,
    isLoading,
    error,
    login,
    logout,
    updateProfile,
    refreshUser,
  };

  return (
    <UserContext.Provider value={value}>
      {children}
    </UserContext.Provider>
  );
};

export const useUser = (): UserContextType => {
  const context = useContext(UserContext);
  if (context === undefined) {
    throw new Error('useUser must be used within a UserProvider');
  }
  return context;
};

// Hook for checking if user is authenticated
export const useAuth = () => {
  const { user, isLoading } = useUser();
  return {
    isAuthenticated: !!user,
    isLoading,
    user,
  };
};

// Hook for getting user context for AI
export const useUserContext = () => {
  const { user } = useUser();
  
  if (!user) {
    return {
      location: 'Not specified',
      situation: 'Not specified',
      primaryNeeds: [],
      name: 'Anonymous',
    };
  }

  return {
    location: user.location || 'Not specified',
    situation: user.situation,
    primaryNeeds: user.primary_needs || [],
    name: user.name || 'Anonymous',
  };
}; 