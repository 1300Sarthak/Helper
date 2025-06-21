import React from 'react';
import { useTheme } from '../../contexts/ThemeContext';
import { useUser } from '../../contexts/UserContext';
import { TabConfig } from '../../types';
import { ThemeToggle } from './ThemeToggle';

interface HeaderProps {
  currentTab: 'voice-chat' | 'resources' | 'life-coach';
  onTabChange: (tabId: 'voice-chat' | 'resources' | 'life-coach') => void;
  tabs: TabConfig[];
}

export const Header: React.FC<HeaderProps> = ({ currentTab, onTabChange, tabs }) => {
  const { theme } = useTheme();
  const { user, logout } = useUser();

  return (
    <header style={{
      backgroundColor: theme.colors.surface,
      borderBottom: `1px solid ${theme.colors.border}`,
      padding: '1rem',
      position: 'sticky',
      top: 0,
      zIndex: 100,
    }}>
      <div style={{
        maxWidth: '1200px',
        margin: '0 auto',
        display: 'flex',
        flexDirection: 'column',
        gap: '1rem',
      }}>
        {/* Top row with logo and controls */}
        <div style={{
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
        }}>
          <div style={{
            display: 'flex',
            alignItems: 'center',
            gap: '12px',
          }}>
            <h1 style={{
              fontSize: '1.5rem',
              fontWeight: '700',
              color: theme.colors.text,
              margin: 0,
            }}>
              🤝 For Social Change
            </h1>
            {user && (
              <span style={{
                fontSize: '0.875rem',
                color: theme.colors.textSecondary,
                padding: '4px 8px',
                backgroundColor: theme.colors.background,
                borderRadius: '4px',
              }}>
                Welcome, {user.name || 'Friend'}
              </span>
            )}
          </div>
          
          <div style={{
            display: 'flex',
            alignItems: 'center',
            gap: '12px',
          }}>
            <ThemeToggle />
            {user && (
              <button
                onClick={logout}
                className="btn btn-text"
                style={{
                  fontSize: '0.875rem',
                }}
                title="Logout"
              >
                Logout
              </button>
            )}
          </div>
        </div>

        {/* Tab navigation */}
        <nav>
          <div className="tab-container">
            {tabs.map((tab) => (
              <button
                key={tab.id}
                className={`tab ${currentTab === tab.id ? 'active' : ''}`}
                onClick={() => onTabChange(tab.id)}
                title={tab.description}
                style={{
                  display: 'flex',
                  alignItems: 'center',
                  gap: '8px',
                }}
              >
                <span style={{ fontSize: '1.2rem' }}>{tab.icon}</span>
                <span>{tab.label}</span>
              </button>
            ))}
          </div>
        </nav>
      </div>
    </header>
  );
}; 