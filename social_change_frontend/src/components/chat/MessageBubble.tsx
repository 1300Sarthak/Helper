import React from 'react';
import { useTheme } from '../../contexts/ThemeContext';
import { ChatMessage } from '../../types';

interface MessageBubbleProps {
  message: ChatMessage;
}

export const MessageBubble: React.FC<MessageBubbleProps> = ({ message }) => {
  const { theme } = useTheme();
  
  const formatTime = (timestamp: string) => {
    const date = new Date(timestamp);
    return date.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
  };

  const getAvatarText = (sender: string) => {
    return sender === 'user' ? 'U' : 'AI';
  };

  const getAvatarIcon = (sender: string) => {
    return sender === 'user' ? '👤' : '🤖';
  };

  return (
    <div className={`message ${message.sender}`}>
      <div className="message-avatar">
        {getAvatarIcon(message.sender)}
      </div>
      
      <div className="message-content">
        <div style={{
          marginBottom: '0.25rem',
        }}>
          <span style={{
            fontSize: '0.75rem',
            color: theme.colors.textSecondary,
            fontWeight: '500',
          }}>
            {message.sender === 'user' ? 'You' : 'AI Assistant'}
          </span>
          
          {message.mode && (
            <span style={{
              fontSize: '0.75rem',
              color: theme.colors.textSecondary,
              marginLeft: '0.5rem',
              padding: '0.125rem 0.375rem',
              backgroundColor: theme.colors.background,
              borderRadius: '4px',
            }}>
              {message.mode === 'support' ? '💬 Support' : '🎯 Coach'}
            </span>
          )}
          
          <span style={{
            fontSize: '0.75rem',
            color: theme.colors.textSecondary,
            marginLeft: 'auto',
            float: 'right',
          }}>
            {formatTime(message.timestamp)}
          </span>
        </div>
        
        <div style={{
          whiteSpace: 'pre-wrap',
          wordBreak: 'break-word',
          lineHeight: '1.5',
        }}>
          {message.content}
        </div>
        
        {/* Crisis warning styling */}
        {message.content.includes('⚠️') && (
          <div style={{
            marginTop: '0.5rem',
            padding: '0.5rem',
            backgroundColor: theme.colors.warning + '20',
            border: `1px solid ${theme.colors.warning}`,
            borderRadius: '4px',
            fontSize: '0.875rem',
          }}>
            <strong>🚨 Crisis Resources:</strong>
            <ul style={{
              margin: '0.25rem 0 0 1rem',
              padding: 0,
            }}>
              <li>National Suicide Prevention Lifeline: <strong>988</strong> (24/7)</li>
              <li>Crisis Text Line: Text <strong>HOME</strong> to <strong>741741</strong></li>
              <li>Emergency Services: <strong>911</strong></li>
            </ul>
          </div>
        )}
      </div>
    </div>
  );
}; 