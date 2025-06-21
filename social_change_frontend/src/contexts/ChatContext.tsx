import React, { createContext, useContext, useState, useEffect, ReactNode, useCallback } from 'react';
import { ChatMessage, ChatResponse, STORAGE_KEYS } from '../types';
import { apiService } from '../services/api';
import { useUserContext } from './UserContext';

interface ChatContextType {
  messages: ChatMessage[];
  isLoading: boolean;
  error: string | null;
  currentMode: 'support' | 'coach';
  sendMessage: (content: string, mode?: 'support' | 'coach') => Promise<void>;
  clearMessages: () => void;
  setMode: (mode: 'support' | 'coach') => void;
  loadConversationHistory: () => Promise<void>;
}

const ChatContext = createContext<ChatContextType | undefined>(undefined);

interface ChatProviderProps {
  children: ReactNode;
}

export const ChatProvider: React.FC<ChatProviderProps> = ({ children }) => {
  const [messages, setMessages] = useState<ChatMessage[]>([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [currentMode, setCurrentMode] = useState<'support' | 'coach'>('support');
  
  const userContext = useUserContext();

  // Load conversation history from localStorage
  useEffect(() => {
    const loadHistory = () => {
      try {
        const savedHistory = localStorage.getItem(STORAGE_KEYS.CONVERSATION_HISTORY);
        if (savedHistory) {
          const parsedHistory = JSON.parse(savedHistory);
          setMessages(parsedHistory.messages || []);
          setCurrentMode(parsedHistory.mode || 'support');
        }
      } catch (error) {
        console.error('Error loading conversation history:', error);
      }
    };

    loadHistory();
  }, []);

  // Save messages to localStorage whenever they change
  useEffect(() => {
    if (messages.length > 0) {
      const historyData = {
        messages,
        mode: currentMode,
        timestamp: new Date().toISOString(),
      };
      localStorage.setItem(STORAGE_KEYS.CONVERSATION_HISTORY, JSON.stringify(historyData));
    }
  }, [messages, currentMode]);

  const sendMessage = useCallback(async (content: string, mode: 'support' | 'coach' = currentMode) => {
    if (!content.trim()) return;

    const userMessage: ChatMessage = {
      message_id: `user_${Date.now()}`,
      content: content.trim(),
      sender: 'user',
      timestamp: new Date().toISOString(),
      mode,
    };

    // Add user message immediately
    setMessages(prev => [...prev, userMessage]);
    setError(null);
    setIsLoading(true);

    try {
      // Get user ID from localStorage
      const userId = localStorage.getItem(STORAGE_KEYS.USER_ID);

      // Send to AI
      const response: ChatResponse = await apiService.sendMessage(content, userId || undefined, mode);

      // Add AI response
      const aiMessage: ChatMessage = {
        message_id: `ai_${Date.now()}`,
        content: response.response,
        sender: 'assistant',
        timestamp: response.timestamp,
        mode: response.mode,
      };

      setMessages(prev => [...prev, aiMessage]);

      // Check for crisis keywords
      const crisisKeywords = [
        'suicide', 'kill myself', 'end it all', 'want to die',
        'hurt myself', 'self-harm', 'overdose', 'dangerous',
        'emergency', 'crisis', 'help me', 'desperate',
        'no hope', 'give up', 'can\'t take it anymore'
      ];

      const hasCrisisKeywords = crisisKeywords.some(keyword => 
        content.toLowerCase().includes(keyword)
      );

      if (hasCrisisKeywords) {
        // Add crisis warning message
        const crisisMessage: ChatMessage = {
          message_id: `crisis_${Date.now()}`,
          content: `⚠️ I'm concerned about what you're going through. If you're in immediate danger, please call 911 or the National Suicide Prevention Lifeline at 988 (24/7). You're not alone, and there are people who want to help you.`,
          sender: 'assistant',
          timestamp: new Date().toISOString(),
          mode: 'support',
        };
        setMessages(prev => [...prev, crisisMessage]);
      }

    } catch (error) {
      console.error('Error sending message:', error);
      setError(error instanceof Error ? error.message : 'Failed to send message');
      
      // Add error message
      const errorMessage: ChatMessage = {
        message_id: `error_${Date.now()}`,
        content: 'I apologize, but I\'m having trouble responding right now. Please try again in a moment.',
        sender: 'assistant',
        timestamp: new Date().toISOString(),
        mode,
      };
      setMessages(prev => [...prev, errorMessage]);
    } finally {
      setIsLoading(false);
    }
  }, [currentMode, userContext]);

  const clearMessages = useCallback(() => {
    setMessages([]);
    localStorage.removeItem(STORAGE_KEYS.CONVERSATION_HISTORY);
  }, []);

  const setMode = useCallback((mode: 'support' | 'coach') => {
    setCurrentMode(mode);
  }, []);

  const loadConversationHistory = useCallback(async () => {
    const userId = localStorage.getItem(STORAGE_KEYS.USER_ID);
    if (!userId) return;

    try {
      setIsLoading(true);
      const history = await apiService.getConversationHistory(userId);
      setMessages(history);
    } catch (error) {
      console.error('Error loading conversation history:', error);
      setError('Failed to load conversation history');
    } finally {
      setIsLoading(false);
    }
  }, []);

  const value: ChatContextType = {
    messages,
    isLoading,
    error,
    currentMode,
    sendMessage,
    clearMessages,
    setMode,
    loadConversationHistory,
  };

  return (
    <ChatContext.Provider value={value}>
      {children}
    </ChatContext.Provider>
  );
};

export const useChat = (): ChatContextType => {
  const context = useContext(ChatContext);
  if (context === undefined) {
    throw new Error('useChat must be used within a ChatProvider');
  }
  return context;
};

// Hook for getting recent messages for context
export const useRecentMessages = (limit: number = 5) => {
  const { messages } = useChat();
  return messages.slice(-limit);
};

// Hook for checking if there are unread messages
export const useUnreadMessages = () => {
  const { messages } = useChat();
  const lastMessage = messages[messages.length - 1];
  
  return {
    hasUnread: lastMessage?.sender === 'assistant',
    lastMessage,
  };
};

// Hook for getting conversation statistics
export const useConversationStats = () => {
  const { messages, currentMode } = useChat();
  
  const stats = {
    totalMessages: messages.length,
    userMessages: messages.filter(m => m.sender === 'user').length,
    aiMessages: messages.filter(m => m.sender === 'assistant').length,
    supportMessages: messages.filter(m => m.mode === 'support').length,
    coachMessages: messages.filter(m => m.mode === 'coach').length,
    currentMode,
  };

  return stats;
}; 