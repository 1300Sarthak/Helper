import React, { useState, useEffect } from 'react';
import { ThemeProvider } from './contexts/ThemeContext';
import { UserProvider } from './contexts/UserContext';
import { ChatProvider } from './contexts/ChatContext';
import { Header } from './components/common/Header';
import { VoiceChatTab } from './components/tabs/VoiceChatTab';
import { ResourcesTab } from './components/tabs/ResourcesTab';
import { LifeCoachTab } from './components/tabs/LifeCoachTab';
import { UserProfileModal } from './components/onboarding/UserProfileModal';
import { useTheme } from './contexts/ThemeContext';
import { useAuth } from './contexts/UserContext';
import { TabConfig } from './types';
import './App.css';

// Tab configuration
const tabs: TabConfig[] = [
  {
    id: 'voice-chat',
    label: 'Voice Chat',
    icon: '🎤',
    description: 'Talk to our AI assistant for support and guidance',
  },
  {
    id: 'resources',
    label: 'Resources',
    icon: '📋',
    description: 'Find local services and support resources',
  },
  {
    id: 'life-coach',
    label: 'Life Coach',
    icon: '🎯',
    description: 'Get personalized coaching and goal-setting help',
  },
];

const AppContent: React.FC = () => {
  const { theme } = useTheme();
  const { isAuthenticated, isLoading } = useAuth();
  const [currentTab, setCurrentTab] = useState<'voice-chat' | 'resources' | 'life-coach'>('voice-chat');
  const [showProfileModal, setShowProfileModal] = useState(false);

  // Show profile modal if user is not authenticated
  useEffect(() => {
    if (!isLoading && !isAuthenticated) {
      setShowProfileModal(true);
    }
  }, [isAuthenticated, isLoading]);

  const handleTabChange = (tabId: 'voice-chat' | 'resources' | 'life-coach') => {
    setCurrentTab(tabId);
  };

  const handleProfileComplete = () => {
    setShowProfileModal(false);
  };

  const renderTabContent = () => {
    switch (currentTab) {
      case 'voice-chat':
        return <VoiceChatTab />;
      case 'resources':
        return <ResourcesTab />;
      case 'life-coach':
        return <LifeCoachTab />;
      default:
        return <VoiceChatTab />;
    }
  };

  if (isLoading) {
    return (
      <div style={{ 
        display: 'flex', 
        justifyContent: 'center', 
        alignItems: 'center', 
        height: '100vh',
        backgroundColor: theme.colors.background,
        color: theme.colors.text
      }}>
        <div style={{ textAlign: 'center' }}>
          <div className="loading-spinner" style={{ margin: '0 auto 1rem' }}></div>
          <p>Loading For Social Change...</p>
        </div>
      </div>
    );
  }

  return (
    <div style={{ 
      backgroundColor: theme.colors.background,
      color: theme.colors.text,
      minHeight: '100vh',
      transition: 'background-color 0.3s ease, color 0.3s ease'
    }}>
      <Header 
        currentTab={currentTab}
        onTabChange={handleTabChange}
        tabs={tabs}
      />
      
      <main style={{ padding: '1rem', maxWidth: '1200px', margin: '0 auto' }}>
        {renderTabContent()}
      </main>

      {showProfileModal && (
        <UserProfileModal 
          isOpen={showProfileModal}
          onClose={handleProfileComplete}
          onComplete={handleProfileComplete}
        />
      )}
    </div>
  );
};

const App: React.FC = () => {
  return (
    <ThemeProvider>
      <UserProvider>
        <ChatProvider>
          <AppContent />
        </ChatProvider>
      </UserProvider>
    </ThemeProvider>
  );
};

export default App; 