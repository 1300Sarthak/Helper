import React, { createContext, useContext, useState, useEffect, ReactNode } from 'react';
import { Theme } from '../types';
import { STORAGE_KEYS } from '../types';

// Default themes
const lightTheme: Theme = {
  mode: 'light',
  colors: {
    primary: '#3b82f6',
    secondary: '#64748b',
    background: '#f8fafc',
    surface: '#ffffff',
    text: '#1e293b',
    textSecondary: '#64748b',
    border: '#e2e8f0',
    error: '#ef4444',
    success: '#10b981',
    warning: '#f59e0b',
    info: '#3b82f6',
  },
};

const darkTheme: Theme = {
  mode: 'dark',
  colors: {
    primary: '#60a5fa',
    secondary: '#94a3b8',
    background: '#0f172a',
    surface: '#1e293b',
    text: '#f1f5f9',
    textSecondary: '#94a3b8',
    border: '#334155',
    error: '#f87171',
    success: '#34d399',
    warning: '#fbbf24',
    info: '#60a5fa',
  },
};

interface ThemeContextType {
  theme: Theme;
  toggleTheme: () => void;
  setTheme: (mode: 'light' | 'dark') => void;
}

const ThemeContext = createContext<ThemeContextType | undefined>(undefined);

interface ThemeProviderProps {
  children: ReactNode;
}

export const ThemeProvider: React.FC<ThemeProviderProps> = ({ children }) => {
  const [theme, setThemeState] = useState<Theme>(lightTheme);

  // Load theme from localStorage on mount
  useEffect(() => {
    const savedTheme = localStorage.getItem(STORAGE_KEYS.THEME);
    if (savedTheme) {
      try {
        const parsedTheme = JSON.parse(savedTheme);
        setThemeState(parsedTheme.mode === 'dark' ? darkTheme : lightTheme);
      } catch (error) {
        console.error('Error parsing saved theme:', error);
        setThemeState(lightTheme);
      }
    } else {
      // Check system preference
      const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
      setThemeState(prefersDark ? darkTheme : lightTheme);
    }
  }, []);

  // Apply theme to document
  useEffect(() => {
    const root = document.documentElement;
    
    // Apply CSS custom properties
    Object.entries(theme.colors).forEach(([key, value]) => {
      root.style.setProperty(`--color-${key}`, value);
    });
    
    // Apply theme class to body
    document.body.className = `theme-${theme.mode}`;
    
    // Update meta theme-color
    const metaThemeColor = document.querySelector('meta[name="theme-color"]');
    if (metaThemeColor) {
      metaThemeColor.setAttribute('content', theme.colors.background);
    }
  }, [theme]);

  const setTheme = (mode: 'light' | 'dark') => {
    const newTheme = mode === 'dark' ? darkTheme : lightTheme;
    setThemeState(newTheme);
    localStorage.setItem(STORAGE_KEYS.THEME, JSON.stringify(newTheme));
  };

  const toggleTheme = () => {
    const newMode = theme.mode === 'light' ? 'dark' : 'light';
    setTheme(newMode);
  };

  const value: ThemeContextType = {
    theme,
    toggleTheme,
    setTheme,
  };

  return (
    <ThemeContext.Provider value={value}>
      {children}
    </ThemeContext.Provider>
  );
};

export const useTheme = (): ThemeContextType => {
  const context = useContext(ThemeContext);
  if (context === undefined) {
    throw new Error('useTheme must be used within a ThemeProvider');
  }
  return context;
};

// CSS-in-JS styles for theme-aware components
export const createThemeStyles = (theme: Theme) => ({
  container: {
    backgroundColor: theme.colors.background,
    color: theme.colors.text,
    minHeight: '100vh',
    transition: 'background-color 0.3s ease, color 0.3s ease',
  },
  
  card: {
    backgroundColor: theme.colors.surface,
    border: `1px solid ${theme.colors.border}`,
    borderRadius: '8px',
    padding: '16px',
    boxShadow: theme.mode === 'dark' 
      ? '0 4px 6px -1px rgba(0, 0, 0, 0.3)' 
      : '0 1px 3px 0 rgba(0, 0, 0, 0.1)',
  },
  
  button: {
    primary: {
      backgroundColor: theme.colors.primary,
      color: '#ffffff',
      border: 'none',
      borderRadius: '6px',
      padding: '8px 16px',
      cursor: 'pointer',
      transition: 'background-color 0.2s ease',
      '&:hover': {
        backgroundColor: theme.mode === 'dark' ? '#4f9eff' : '#2563eb',
      },
      '&:disabled': {
        backgroundColor: theme.colors.secondary,
        cursor: 'not-allowed',
      },
    },
    
    secondary: {
      backgroundColor: 'transparent',
      color: theme.colors.primary,
      border: `1px solid ${theme.colors.primary}`,
      borderRadius: '6px',
      padding: '8px 16px',
      cursor: 'pointer',
      transition: 'all 0.2s ease',
      '&:hover': {
        backgroundColor: theme.colors.primary,
        color: '#ffffff',
      },
    },
    
    text: {
      backgroundColor: 'transparent',
      color: theme.colors.primary,
      border: 'none',
      padding: '8px 16px',
      cursor: 'pointer',
      transition: 'color 0.2s ease',
      '&:hover': {
        color: theme.mode === 'dark' ? '#4f9eff' : '#2563eb',
      },
    },
  },
  
  input: {
    backgroundColor: theme.colors.surface,
    color: theme.colors.text,
    border: `1px solid ${theme.colors.border}`,
    borderRadius: '6px',
    padding: '8px 12px',
    fontSize: '14px',
    transition: 'border-color 0.2s ease',
    '&:focus': {
      outline: 'none',
      borderColor: theme.colors.primary,
      boxShadow: `0 0 0 3px ${theme.colors.primary}20`,
    },
    '&::placeholder': {
      color: theme.colors.textSecondary,
    },
  },
  
  text: {
    primary: {
      color: theme.colors.text,
    },
    secondary: {
      color: theme.colors.textSecondary,
    },
    link: {
      color: theme.colors.primary,
      textDecoration: 'none',
      '&:hover': {
        textDecoration: 'underline',
      },
    },
  },
  
  status: {
    error: {
      color: theme.colors.error,
    },
    success: {
      color: theme.colors.success,
    },
    warning: {
      color: theme.colors.warning,
    },
    info: {
      color: theme.colors.info,
    },
  },
}); 