import React, { useState, useEffect } from 'react';
import { useTheme } from '../../contexts/ThemeContext';
import { useUser } from '../../contexts/UserContext';
import { apiService } from '../../services/api';
import { Resource, QuickAction, ResourceCategory } from '../../types';
import { QuickActions } from '../common/QuickActions';

export const ResourcesTab: React.FC = () => {
  const { theme } = useTheme();
  const { user } = useUser();
  
  const [resources, setResources] = useState<Resource[]>([]);
  const [quickActions, setQuickActions] = useState<QuickAction[]>([]);
  const [categories, setCategories] = useState<ResourceCategory[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  
  const [searchLocation, setSearchLocation] = useState(user?.location || '');
  const [selectedCategory, setSelectedCategory] = useState('');
  const [selectedNeeds, setSelectedNeeds] = useState<string[]>([]);

  // Load initial data
  useEffect(() => {
    const loadData = async () => {
      try {
        setIsLoading(true);
        setError(null);

        const [quickActionsData, categoriesData] = await Promise.all([
          apiService.getQuickActions(user?.location),
          apiService.getResourceCategories(),
        ]);

        setQuickActions(quickActionsData.quick_actions);
        setCategories(categoriesData.categories);

        // Load nearby resources if user has location
        if (user?.location) {
          const nearbyResources = await apiService.getNearbyResources(user.location);
          setResources(nearbyResources);
        }
      } catch (error) {
        console.error('Error loading resources:', error);
        setError('Failed to load resources. Please try again.');
      } finally {
        setIsLoading(false);
      }
    };

    loadData();
  }, [user?.location]);

  const handleSearch = async () => {
    if (!searchLocation.trim()) {
      setError('Please enter a location to search for resources.');
      return;
    }

    try {
      setIsLoading(true);
      setError(null);

      const searchResult = await apiService.searchResources(
        searchLocation,
        selectedNeeds,
        selectedCategory
      );

      setResources(searchResult.resources);
    } catch (error) {
      console.error('Error searching resources:', error);
      setError('Failed to search resources. Please try again.');
    } finally {
      setIsLoading(false);
    }
  };

  const handleQuickAction = async (action: QuickAction) => {
    if (action.action === 'search' && action.search_params) {
      setSelectedCategory(action.search_params.type || '');
      await handleSearch();
    }
  };

  const handleNeedToggle = (need: string) => {
    setSelectedNeeds(prev => 
      prev.includes(need)
        ? prev.filter(n => n !== need)
        : [...prev, need]
    );
  };

  const formatPhoneNumber = (phone: string) => {
    // Simple phone formatting
    const cleaned = phone.replace(/\D/g, '');
    if (cleaned.length === 10) {
      return `(${cleaned.slice(0, 3)}) ${cleaned.slice(3, 6)}-${cleaned.slice(6)}`;
    }
    return phone;
  };

  if (isLoading && resources.length === 0) {
    return (
      <div style={{
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        height: '400px',
      }}>
        <div style={{ textAlign: 'center' }}>
          <div className="loading-spinner" style={{ margin: '0 auto 1rem' }}></div>
          <p>Loading resources...</p>
        </div>
      </div>
    );
  }

  return (
    <div>
      {/* Header */}
      <div style={{ marginBottom: '2rem' }}>
        <h2 style={{
          fontSize: '1.5rem',
          fontWeight: '600',
          color: theme.colors.text,
          marginBottom: '0.5rem',
        }}>
          📋 Find Local Resources
        </h2>
        <p style={{
          color: theme.colors.textSecondary,
          fontSize: '0.875rem',
        }}>
          Search for services and support in your area. We'll help you find the resources you need.
        </p>
      </div>

      {/* Quick Actions */}
      <QuickActions
        actions={quickActions}
        onAction={handleQuickAction}
      />

      {/* Search Section */}
      <div className="card" style={{ marginBottom: '2rem' }}>
        <h3 style={{
          fontSize: '1.125rem',
          fontWeight: '600',
          color: theme.colors.text,
          marginBottom: '1rem',
        }}>
          🔍 Search Resources
        </h3>

        <div style={{
          display: 'grid',
          gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))',
          gap: '1rem',
          marginBottom: '1rem',
        }}>
          {/* Location Input */}
          <div>
            <label style={{
              display: 'block',
              marginBottom: '0.5rem',
              fontWeight: '500',
              color: theme.colors.text,
              fontSize: '0.875rem',
            }}>
              Location
            </label>
            <input
              type="text"
              className="input"
              value={searchLocation}
              onChange={(e) => setSearchLocation(e.target.value)}
              placeholder="City, State (e.g., San Francisco, CA)"
            />
          </div>

          {/* Category Filter */}
          <div>
            <label style={{
              display: 'block',
              marginBottom: '0.5rem',
              fontWeight: '500',
              color: theme.colors.text,
              fontSize: '0.875rem',
            }}>
              Service Type
            </label>
            <select
              className="input"
              value={selectedCategory}
              onChange={(e) => setSelectedCategory(e.target.value)}
            >
              <option value="">All Services</option>
              {categories.map(category => (
                <option key={category.id} value={category.id}>
                  {category.icon} {category.name}
                </option>
              ))}
            </select>
          </div>
        </div>

        {/* Needs Selection */}
        <div style={{ marginBottom: '1rem' }}>
          <label style={{
            display: 'block',
            marginBottom: '0.5rem',
            fontWeight: '500',
            color: theme.colors.text,
            fontSize: '0.875rem',
          }}>
            Specific Needs
          </label>
          <div style={{
            display: 'grid',
            gridTemplateColumns: 'repeat(auto-fit, minmax(150px, 1fr))',
            gap: '0.5rem',
          }}>
            {['shelter', 'food', 'healthcare', 'employment', 'legal', 'mental_health', 'transportation'].map(need => (
              <label
                key={need}
                style={{
                  display: 'flex',
                  alignItems: 'center',
                  gap: '0.5rem',
                  padding: '0.5rem',
                  border: `1px solid ${theme.colors.border}`,
                  borderRadius: '4px',
                  cursor: 'pointer',
                  backgroundColor: selectedNeeds.includes(need)
                    ? theme.colors.primary + '20'
                    : 'transparent',
                }}
              >
                <input
                  type="checkbox"
                  checked={selectedNeeds.includes(need)}
                  onChange={() => handleNeedToggle(need)}
                  style={{ margin: 0 }}
                />
                <span style={{ fontSize: '0.875rem' }}>
                  {need.replace('_', ' ').replace(/\b\w/g, l => l.toUpperCase())}
                </span>
              </label>
            ))}
          </div>
        </div>

        {/* Search Button */}
        <button
          onClick={handleSearch}
          className="btn btn-primary"
          disabled={isLoading || !searchLocation.trim()}
          style={{ width: '100%' }}
        >
          {isLoading ? (
            <>
              <div className="loading-spinner" style={{ width: '16px', height: '16px' }}></div>
              Searching...
            </>
          ) : (
            '🔍 Search Resources'
          )}
        </button>

        {/* Error Message */}
        {error && (
          <div style={{
            marginTop: '1rem',
            padding: '0.75rem',
            backgroundColor: theme.colors.error + '20',
            color: theme.colors.error,
            borderRadius: '4px',
            fontSize: '0.875rem',
          }}>
            {error}
          </div>
        )}
      </div>

      {/* Results */}
      {resources.length > 0 && (
        <div>
          <h3 style={{
            fontSize: '1.125rem',
            fontWeight: '600',
            color: theme.colors.text,
            marginBottom: '1rem',
          }}>
            📍 Found {resources.length} Resource{resources.length !== 1 ? 's' : ''}
          </h3>

          <div className="resource-grid">
            {resources.map((resource) => (
              <div key={resource.id} className="resource-card">
                <div className="resource-header">
                  <span className="resource-icon">
                    {resource.category === 'housing' ? '🏠' :
                     resource.category === 'basic_needs' ? '🍽️' :
                     resource.category === 'health' ? '🏥' :
                     resource.category === 'employment' ? '💼' :
                     resource.category === 'legal' ? '⚖️' : '📋'}
                  </span>
                  <div>
                    <div className="resource-title">{resource.name}</div>
                    <div style={{
                      fontSize: '0.75rem',
                      color: theme.colors.textSecondary,
                    }}>
                      {resource.type.replace(/\b\w/g, l => l.toUpperCase())}
                    </div>
                  </div>
                </div>

                <div className="resource-description">
                  {resource.description}
                </div>

                <div className="resource-details">
                  <div className="resource-detail">
                    📍 {resource.address}
                  </div>
                  <div className="resource-detail">
                    📞 <a href={`tel:${resource.phone}`} style={{ color: 'inherit' }}>
                      {formatPhoneNumber(resource.phone)}
                    </a>
                  </div>
                  <div className="resource-detail">
                    🕒 {resource.hours}
                  </div>
                  <div className="resource-detail">
                    ✅ {resource.eligibility}
                  </div>
                </div>

                <div style={{
                  marginTop: '1rem',
                  paddingTop: '1rem',
                  borderTop: `1px solid ${theme.colors.border}`,
                }}>
                  <strong style={{ fontSize: '0.75rem', color: theme.colors.textSecondary }}>
                    Services:
                  </strong>
                  <div style={{
                    fontSize: '0.75rem',
                    color: theme.colors.textSecondary,
                    marginTop: '0.25rem',
                  }}>
                    {resource.services.join(', ')}
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* No Results */}
      {!isLoading && resources.length === 0 && searchLocation && (
        <div style={{
          textAlign: 'center',
          padding: '2rem',
          color: theme.colors.textSecondary,
        }}>
          <div style={{ fontSize: '3rem', marginBottom: '1rem' }}>🔍</div>
          <h3 style={{ marginBottom: '0.5rem' }}>No resources found</h3>
          <p>Try adjusting your search criteria or location.</p>
        </div>
      )}
    </div>
  );
}; 