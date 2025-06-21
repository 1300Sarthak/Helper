import React from 'react';
import { useTheme } from '../../contexts/ThemeContext';
import { useChat } from '../../contexts/ChatContext';
import { useUser } from '../../contexts/UserContext';
import { useConversationStats } from '../../contexts/ChatContext';

export const ChatSidebar: React.FC = () => {
  const { theme } = useTheme();
  const { clearMessages, currentMode } = useChat();
  const { user } = useUser();
  const stats = useConversationStats();

  const handleClearMessages = () => {
    if (window.confirm('Are you sure you want to clear all messages? This cannot be undone.')) {
      clearMessages();
    }
  };

  return (
    <div style={{
      width: '280px',
      backgroundColor: theme.colors.surface,
      border: `1px solid ${theme.colors.border}`,
      borderRadius: '8px',
      padding: '1rem',
      height: 'fit-content',
      position: 'sticky',
      top: '1rem',
    }}>
      {/* User Info */}
      {user && (
        <div style={{
          marginBottom: '1.5rem',
          padding: '1rem',
          backgroundColor: theme.colors.background,
          borderRadius: '6px',
        }}>
          <h4 style={{
            fontSize: '0.875rem',
            fontWeight: '600',
            color: theme.colors.text,
            marginBottom: '0.5rem',
          }}>
            👤 Your Profile
          </h4>
          <div style={{
            fontSize: '0.75rem',
            color: theme.colors.textSecondary,
          }}>
            <div><strong>Location:</strong> {user.location || 'Not specified'}</div>
            <div><strong>Situation:</strong> {user.situation}</div>
            <div><strong>Needs:</strong> {user.primary_needs?.join(', ') || 'None specified'}</div>
          </div>
        </div>
      )}

      {/* Conversation Stats */}
      <div style={{
        marginBottom: '1.5rem',
        padding: '1rem',
        backgroundColor: theme.colors.background,
        borderRadius: '6px',
      }}>
        <h4 style={{
          fontSize: '0.875rem',
          fontWeight: '600',
          color: theme.colors.text,
          marginBottom: '0.75rem',
        }}>
          📊 Conversation Stats
        </h4>
        <div style={{
          display: 'grid',
          gridTemplateColumns: '1fr 1fr',
          gap: '0.5rem',
          fontSize: '0.75rem',
        }}>
          <div style={{ color: theme.colors.textSecondary }}>
            <div>Total Messages</div>
            <div style={{ fontWeight: '600', color: theme.colors.text }}>
              {stats.totalMessages}
            </div>
          </div>
          <div style={{ color: theme.colors.textSecondary }}>
            <div>Your Messages</div>
            <div style={{ fontWeight: '600', color: theme.colors.text }}>
              {stats.userMessages}
            </div>
          </div>
          <div style={{ color: theme.colors.textSecondary }}>
            <div>AI Responses</div>
            <div style={{ fontWeight: '600', color: theme.colors.text }}>
              {stats.aiMessages}
            </div>
          </div>
          <div style={{ color: theme.colors.textSecondary }}>
            <div>Current Mode</div>
            <div style={{ fontWeight: '600', color: theme.colors.text }}>
              {currentMode === 'support' ? '💬 Support' : '🎯 Coach'}
            </div>
          </div>
        </div>
      </div>

      {/* Quick Actions */}
      <div style={{
        marginBottom: '1.5rem',
      }}>
        <h4 style={{
          fontSize: '0.875rem',
          fontWeight: '600',
          color: theme.colors.text,
          marginBottom: '0.75rem',
        }}>
          ⚡ Quick Actions
        </h4>
        <div style={{
          display: 'flex',
          flexDirection: 'column',
          gap: '0.5rem',
        }}>
          <button
            onClick={handleClearMessages}
            className="btn btn-text"
            style={{
              justifyContent: 'flex-start',
              fontSize: '0.75rem',
              padding: '0.5rem',
            }}
            disabled={stats.totalMessages === 0}
          >
            🗑️ Clear Messages
          </button>
          
          <a
            href="tel:988"
            className="btn btn-text"
            style={{
              justifyContent: 'flex-start',
              fontSize: '0.75rem',
              padding: '0.5rem',
              color: theme.colors.error,
            }}
          >
            🆘 Crisis Hotline (988)
          </a>
          
          <a
            href="tel:911"
            className="btn btn-text"
            style={{
              justifyContent: 'flex-start',
              fontSize: '0.75rem',
              padding: '0.5rem',
              color: theme.colors.error,
            }}
          >
            🚨 Emergency (911)
          </a>
        </div>
      </div>

      {/* Help & Tips */}
      <div style={{
        padding: '1rem',
        backgroundColor: theme.colors.info + '20',
        borderRadius: '6px',
        fontSize: '0.75rem',
      }}>
        <h4 style={{
          fontSize: '0.875rem',
          fontWeight: '600',
          color: theme.colors.text,
          marginBottom: '0.5rem',
        }}>
          💡 Tips
        </h4>
        <ul style={{
          color: theme.colors.textSecondary,
          margin: 0,
          paddingLeft: '1rem',
        }}>
          <li>Be specific about your needs</li>
          <li>Ask follow-up questions</li>
          <li>Use voice input for easier communication</li>
          <li>Switch modes for different types of help</li>
        </ul>
      </div>

      {/* Privacy Notice */}
      <div style={{
        marginTop: '1rem',
        padding: '0.75rem',
        backgroundColor: theme.colors.background,
        borderRadius: '6px',
        fontSize: '0.625rem',
        color: theme.colors.textSecondary,
        textAlign: 'center',
      }}>
        <strong>Privacy:</strong> Your conversations are stored locally and used only to provide better assistance.
      </div>
    </div>
  );
}; 