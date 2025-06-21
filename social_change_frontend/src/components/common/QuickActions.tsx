import React from 'react';
import { useTheme } from '../../contexts/ThemeContext';
import { QuickAction } from '../../types';

interface QuickActionsProps {
  actions: QuickAction[];
  onAction: (action: QuickAction) => void;
}

export const QuickActions: React.FC<QuickActionsProps> = ({ actions, onAction }) => {
  const { theme } = useTheme();

  const handleActionClick = (action: QuickAction) => {
    onAction(action);
  };

  if (actions.length === 0) {
    return null;
  }

  return (
    <div style={{ marginBottom: '2rem' }}>
      <h3 style={{
        fontSize: '1.125rem',
        fontWeight: '600',
        color: theme.colors.text,
        marginBottom: '1rem',
      }}>
        ⚡ Quick Actions
      </h3>
      
      <div className="quick-actions">
        {actions.map((action) => (
          <div
            key={action.id}
            className="quick-action-card"
            onClick={() => handleActionClick(action)}
            style={{ cursor: 'pointer' }}
          >
            <div className="quick-action-icon">
              {action.icon}
            </div>
            <div className="quick-action-title">
              {action.title}
            </div>
            <div className="quick-action-description">
              {action.description}
            </div>
            
            {/* Crisis resources display */}
            {action.resources && action.resources.length > 0 && (
              <div style={{
                marginTop: '1rem',
                padding: '0.75rem',
                backgroundColor: theme.colors.error + '20',
                borderRadius: '4px',
                fontSize: '0.75rem',
              }}>
                <strong style={{ color: theme.colors.error, display: 'block', marginBottom: '0.5rem' }}>
                  🆘 Crisis Resources:
                </strong>
                {action.resources.map((resource, index) => (
                  <div key={index} style={{ marginBottom: '0.25rem' }}>
                    <strong>{resource.name}:</strong> {resource.phone}
                    <div style={{ fontSize: '0.625rem', color: theme.colors.textSecondary }}>
                      {resource.description}
                    </div>
                  </div>
                ))}
              </div>
            )}
          </div>
        ))}
      </div>
    </div>
  );
}; 