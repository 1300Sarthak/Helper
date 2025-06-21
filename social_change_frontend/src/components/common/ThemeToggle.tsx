import React from 'react';
import { useTheme } from '../../contexts/ThemeContext';

export const ThemeToggle: React.FC = () => {
  const { theme, toggleTheme } = useTheme();

  return (
    <button
      onClick={toggleTheme}
      className="btn btn-text"
      title={`Switch to ${theme.mode === 'light' ? 'dark' : 'light'} mode`}
      aria-label={`Switch to ${theme.mode === 'light' ? 'dark' : 'light'} mode`}
      style={{
        padding: '8px',
        borderRadius: '50%',
        width: '40px',
        height: '40px',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
      }}
    >
      {theme.mode === 'light' ? '🌙' : '☀️'}
    </button>
  );
}; 