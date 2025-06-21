import axios from 'axios';
import type { AxiosInstance, AxiosResponse, InternalAxiosRequestConfig, AxiosError } from 'axios';
import {
  UserProfile,
  ChatMessage,
  ChatResponse,
  Resource,
  ResourceSearchResponse,
  QuickAction,
  QuickActionsResponse,
  ResourceCategory,
  CategoriesResponse,
  CrisisResource,
  CrisisResourcesResponse,
  ApiResponse,
  API_ENDPOINTS,
} from '../types';

// Create axios instance with default configuration
const apiClient: AxiosInstance = axios.create({
  baseURL: process.env.REACT_APP_API_URL || 'http://localhost:5001',
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Request interceptor for adding auth tokens, etc.
apiClient.interceptors.request.use(
  (config: InternalAxiosRequestConfig) => {
    // Add any auth headers here if needed
    return config;
  },
  (error: AxiosError) => {
    return Promise.reject(error);
  }
);

// Response interceptor for handling errors
apiClient.interceptors.response.use(
  (response: AxiosResponse) => {
    return response;
  },
  (error: AxiosError) => {
    // Handle common errors
    if (error.response?.status === 401) {
      // Handle unauthorized
      console.error('Unauthorized request');
    } else if (error.response?.status === 500) {
      // Handle server errors
      console.error('Server error:', error.response.data);
    } else if (!error.response) {
      // Handle network errors
      console.error('Network error:', error.message);
    }
    
    return Promise.reject(error);
  }
);

// API service class
class ApiService {
  // Health check
  async healthCheck(): Promise<boolean> {
    try {
      const response = await apiClient.get(API_ENDPOINTS.HEALTH);
      return response.data.status === 'healthy';
    } catch (error) {
      console.error('Health check failed:', error);
      return false;
    }
  }

  // Chat endpoints
  async sendMessage(
    message: string,
    userId?: string,
    mode: 'support' | 'coach' = 'support'
  ): Promise<ChatResponse> {
    try {
      const response = await apiClient.post(API_ENDPOINTS.CHAT.MESSAGE, {
        message,
        user_id: userId,
        mode,
      });
      
      return response.data;
    } catch (error) {
      console.error('Error sending message:', error);
      throw new Error('Failed to send message. Please try again.');
    }
  }

  async getConversationHistory(userId: string): Promise<ChatMessage[]> {
    try {
      const response = await apiClient.get(`${API_ENDPOINTS.CHAT.CONVERSATION}/${userId}`);
      return response.data.messages || [];
    } catch (error) {
      console.error('Error getting conversation history:', error);
      return [];
    }
  }

  // User endpoints
  async createOrUpdateProfile(profile: UserProfile): Promise<UserProfile> {
    try {
      const response = await apiClient.post(API_ENDPOINTS.USERS.PROFILE, profile);
      return response.data.user;
    } catch (error) {
      console.error('Error creating/updating profile:', error);
      throw new Error('Failed to save profile. Please try again.');
    }
  }

  async getUserProfile(userId: string): Promise<UserProfile | null> {
    try {
      const response = await apiClient.get(`${API_ENDPOINTS.USERS.PROFILE}/${userId}`);
      return response.data.user;
    } catch (error) {
      console.error('Error getting user profile:', error);
      return null;
    }
  }

  async getUserContext(userId: string): Promise<any> {
    try {
      const response = await apiClient.get(`${API_ENDPOINTS.USERS.CONTEXT}/${userId}/context`);
      return response.data.context;
    } catch (error) {
      console.error('Error getting user context:', error);
      return {};
    }
  }

  // Resource endpoints
  async searchResources(
    location: string,
    needs: string[] = [],
    type: string = ''
  ): Promise<ResourceSearchResponse> {
    try {
      const params = new URLSearchParams({
        location,
        needs: needs.join(','),
        type,
      });

      const response = await apiClient.get(`${API_ENDPOINTS.RESOURCES.SEARCH}?${params}`);
      return response.data;
    } catch (error) {
      console.error('Error searching resources:', error);
      return {
        resources: [],
        search_params: { location, needs, type },
        total_count: 0,
      };
    }
  }

  async getQuickActions(location?: string): Promise<QuickActionsResponse> {
    try {
      const params = location ? `?location=${encodeURIComponent(location)}` : '';
      const response = await apiClient.get(`${API_ENDPOINTS.RESOURCES.QUICK_ACTIONS}${params}`);
      return response.data;
    } catch (error) {
      console.error('Error getting quick actions:', error);
      return {
        quick_actions: [],
        location: location || '',
      };
    }
  }

  async getResourceCategories(): Promise<CategoriesResponse> {
    try {
      const response = await apiClient.get(API_ENDPOINTS.RESOURCES.CATEGORIES);
      return response.data;
    } catch (error) {
      console.error('Error getting resource categories:', error);
      return { categories: [] };
    }
  }

  async getNearbyResources(location: string): Promise<Resource[]> {
    try {
      const response = await apiClient.get(`${API_ENDPOINTS.RESOURCES.NEARBY}/${encodeURIComponent(location)}`);
      return response.data.resources || [];
    } catch (error) {
      console.error('Error getting nearby resources:', error);
      return [];
    }
  }

  async getCrisisResources(location?: string): Promise<CrisisResourcesResponse> {
    try {
      const params = location ? `?location=${encodeURIComponent(location)}` : '';
      const response = await apiClient.get(`${API_ENDPOINTS.RESOURCES.CRISIS}${params}`);
      return response.data;
    } catch (error) {
      console.error('Error getting crisis resources:', error);
      return {
        crisis_resources: [],
        location: location || '',
      };
    }
  }

  // Voice endpoints (placeholder for future implementation)
  async convertVoiceToText(audioBlob: Blob): Promise<string> {
    try {
      const formData = new FormData();
      formData.append('audio', audioBlob);

      const response = await apiClient.post(API_ENDPOINTS.CHAT.VOICE_TO_TEXT, formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });

      return response.data.text || '';
    } catch (error) {
      console.error('Error converting voice to text:', error);
      throw new Error('Voice-to-text conversion failed. Please try typing instead.');
    }
  }
}

// Export singleton instance
export const apiService = new ApiService();

// Export axios instance for direct use if needed
export { apiClient };

// Utility functions for common API operations
export const apiUtils = {
  // Handle API errors consistently
  handleError: (error: any): string => {
    if (error.response?.data?.error) {
      return error.response.data.error;
    } else if (error.message) {
      return error.message;
    } else {
      return 'An unexpected error occurred. Please try again.';
    }
  },

  // Check if response is successful
  isSuccess: (response: AxiosResponse): boolean => {
    return response.status >= 200 && response.status < 300;
  },

  // Retry function for failed requests
  retry: async <T>(
    fn: () => Promise<T>,
    maxRetries: number = 3,
    delay: number = 1000
  ): Promise<T> => {
    let lastError: any;

    for (let i = 0; i < maxRetries; i++) {
      try {
        return await fn();
      } catch (error) {
        lastError = error;
        if (i < maxRetries - 1) {
          await new Promise(resolve => setTimeout(resolve, delay * (i + 1)));
        }
      }
    }

    throw lastError;
  },
}; 