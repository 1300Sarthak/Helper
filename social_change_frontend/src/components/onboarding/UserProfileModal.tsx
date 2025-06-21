import React, { useState } from 'react';
import { useTheme } from '../../contexts/ThemeContext';
import { useUser } from '../../contexts/UserContext';
import { UserProfile, SITUATION_OPTIONS, NEED_OPTIONS } from '../../types';

interface UserProfileModalProps {
  isOpen: boolean;
  onClose: () => void;
  onComplete: () => void;
}

export const UserProfileModal: React.FC<UserProfileModalProps> = ({
  isOpen,
  onClose,
  onComplete,
}) => {
  const { theme } = useTheme();
  const { login } = useUser();
  
  const [formData, setFormData] = useState({
    name: '',
    location: '',
    situation: 'unsheltered' as const,
    primary_needs: [] as string[],
    previous_services: '',
  });
  
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleInputChange = (field: keyof typeof formData, value: any) => {
    setFormData(prev => ({ ...prev, [field]: value }));
  };

  const handleNeedToggle = (need: string) => {
    setFormData(prev => ({
      ...prev,
      primary_needs: prev.primary_needs.includes(need)
        ? prev.primary_needs.filter(n => n !== need)
        : [...prev.primary_needs, need]
    }));
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    
    if (!formData.location.trim()) {
      setError('Please enter your location to help us find relevant resources.');
      return;
    }

    if (formData.primary_needs.length === 0) {
      setError('Please select at least one need so we can better assist you.');
      return;
    }

    setIsSubmitting(true);
    setError(null);

    try {
      const profile: UserProfile = {
        ...formData,
        name: formData.name.trim() || undefined,
        location: formData.location.trim(),
        previous_services: formData.previous_services.trim() || undefined,
      };

      await login(profile);
      onComplete();
    } catch (error) {
      setError(error instanceof Error ? error.message : 'Failed to save profile');
    } finally {
      setIsSubmitting(false);
    }
  };

  if (!isOpen) return null;

  return (
    <div className="modal-overlay" onClick={onClose}>
      <div className="modal-content" onClick={e => e.stopPropagation()}>
        <div style={{ marginBottom: '1.5rem' }}>
          <h2 style={{
            fontSize: '1.5rem',
            fontWeight: '600',
            color: theme.colors.text,
            marginBottom: '0.5rem',
          }}>
            Welcome to For Social Change
          </h2>
          <p style={{
            color: theme.colors.textSecondary,
            fontSize: '0.875rem',
          }}>
            Help us understand your situation so we can provide the most relevant support and resources.
          </p>
        </div>

        <form onSubmit={handleSubmit}>
          {/* Name (Optional) */}
          <div style={{ marginBottom: '1rem' }}>
            <label style={{
              display: 'block',
              marginBottom: '0.5rem',
              fontWeight: '500',
              color: theme.colors.text,
            }}>
              Name (Optional)
            </label>
            <input
              type="text"
              className="input"
              value={formData.name}
              onChange={(e) => handleInputChange('name', e.target.value)}
              placeholder="Your name or nickname"
            />
          </div>

          {/* Location */}
          <div style={{ marginBottom: '1rem' }}>
            <label style={{
              display: 'block',
              marginBottom: '0.5rem',
              fontWeight: '500',
              color: theme.colors.text,
            }}>
              Location *
            </label>
            <input
              type="text"
              className="input"
              value={formData.location}
              onChange={(e) => handleInputChange('location', e.target.value)}
              placeholder="City, State (e.g., San Francisco, CA)"
              required
            />
          </div>

          {/* Current Situation */}
          <div style={{ marginBottom: '1rem' }}>
            <label style={{
              display: 'block',
              marginBottom: '0.5rem',
              fontWeight: '500',
              color: theme.colors.text,
            }}>
              Current Situation *
            </label>
            <select
              className="input"
              value={formData.situation}
              onChange={(e) => handleInputChange('situation', e.target.value)}
              required
            >
              {SITUATION_OPTIONS.map(option => (
                <option key={option.value} value={option.value}>
                  {option.label}
                </option>
              ))}
            </select>
          </div>

          {/* Primary Needs */}
          <div style={{ marginBottom: '1rem' }}>
            <label style={{
              display: 'block',
              marginBottom: '0.5rem',
              fontWeight: '500',
              color: theme.colors.text,
            }}>
              What do you need help with? *
            </label>
            <div style={{
              display: 'grid',
              gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))',
              gap: '0.5rem',
            }}>
              {NEED_OPTIONS.map(option => (
                <label
                  key={option.value}
                  style={{
                    display: 'flex',
                    alignItems: 'center',
                    gap: '0.5rem',
                    padding: '0.5rem',
                    border: `1px solid ${theme.colors.border}`,
                    borderRadius: '4px',
                    cursor: 'pointer',
                    backgroundColor: formData.primary_needs.includes(option.value)
                      ? theme.colors.primary + '20'
                      : 'transparent',
                  }}
                >
                  <input
                    type="checkbox"
                    checked={formData.primary_needs.includes(option.value)}
                    onChange={() => handleNeedToggle(option.value)}
                    style={{ margin: 0 }}
                  />
                  <span style={{ fontSize: '0.875rem' }}>{option.label}</span>
                </label>
              ))}
            </div>
          </div>

          {/* Previous Services */}
          <div style={{ marginBottom: '1.5rem' }}>
            <label style={{
              display: 'block',
              marginBottom: '0.5rem',
              fontWeight: '500',
              color: theme.colors.text,
            }}>
              Previous Services (Optional)
            </label>
            <textarea
              className="input"
              value={formData.previous_services}
              onChange={(e) => handleInputChange('previous_services', e.target.value)}
              placeholder="Have you used any social services before? This helps us avoid duplicating efforts."
              rows={3}
              style={{ resize: 'vertical' }}
            />
          </div>

          {/* Error Message */}
          {error && (
            <div style={{
              padding: '0.75rem',
              backgroundColor: theme.colors.error + '20',
              color: theme.colors.error,
              borderRadius: '4px',
              marginBottom: '1rem',
              fontSize: '0.875rem',
            }}>
              {error}
            </div>
          )}

          {/* Buttons */}
          <div style={{
            display: 'flex',
            gap: '0.75rem',
            justifyContent: 'flex-end',
          }}>
            <button
              type="button"
              className="btn btn-secondary"
              onClick={onClose}
              disabled={isSubmitting}
            >
              Skip for Now
            </button>
            <button
              type="submit"
              className="btn btn-primary"
              disabled={isSubmitting}
            >
              {isSubmitting ? (
                <>
                  <div className="loading-spinner" style={{ width: '16px', height: '16px' }}></div>
                  Saving...
                </>
              ) : (
                'Save Profile'
              )}
            </button>
          </div>
        </form>

        <div style={{
          marginTop: '1rem',
          padding: '0.75rem',
          backgroundColor: theme.colors.info + '20',
          borderRadius: '4px',
          fontSize: '0.75rem',
          color: theme.colors.textSecondary,
        }}>
          <strong>Privacy Note:</strong> Your information is stored locally and used only to provide better assistance. 
          You can update or delete your profile at any time.
        </div>
      </div>
    </div>
  );
}; 