// User profile types
export interface UserProfile {
  user_id?: string;
  name?: string;
  location?: string;
  situation: 'housed' | 'shelter' | 'unsheltered' | 'transitional' | 'risk';
  primary_needs: string[];
  previous_services?: string;
  created_at?: string;
  updated_at?: string;
}

// Chat message types
export interface ChatMessage {
  message_id: string;
  content: string;
  sender: 'user' | 'assistant';
  timestamp: string;
  mode: 'support' | 'coach';
}

// Conversation types
export interface Conversation {
  conversation_id: string;
  user_id: string;
  messages: ChatMessage[];
  created_at: string;
  updated_at: string;
}

// Resource types
export interface Resource {
  id: string;
  name: string;
  type: string;
  category: string;
  location: string;
  address: string;
  phone: string;
  hours: string;
  description: string;
  eligibility: string;
  services: string[];
  coordinates?: {
    lat: number;
    lng: number;
  };
}

// Quick action types
export interface QuickAction {
  id: string;
  title: string;
  description: string;
  icon: string;
  category: string;
  action?: 'search';
  search_params?: Record<string, any>;
  resources?: Array<{
    name: string;
    phone: string;
    description: string;
  }>;
}

// Resource category types
export interface ResourceCategory {
  id: string;
  name: string;
  icon: string;
  description: string;
}

// Crisis resource types
export interface CrisisResource {
  name: string;
  phone: string;
  description: string;
  hours: string;
  type: string;
}

// API response types
export interface ApiResponse<T> {
  data?: T;
  error?: string;
  message?: string;
}

export interface ChatResponse {
  response: string;
  timestamp: string;
  mode: 'support' | 'coach';
  conversation_id?: string;
}

export interface ResourceSearchResponse {
  resources: Resource[];
  search_params: {
    location: string;
    needs: string[];
    type: string;
  };
  total_count: number;
}

export interface QuickActionsResponse {
  quick_actions: QuickAction[];
  location: string;
}

export interface CategoriesResponse {
  categories: ResourceCategory[];
}

export interface CrisisResourcesResponse {
  crisis_resources: CrisisResource[];
  location: string;
}

// Theme types
export interface Theme {
  mode: 'light' | 'dark';
  colors: {
    primary: string;
    secondary: string;
    background: string;
    surface: string;
    text: string;
    textSecondary: string;
    border: string;
    error: string;
    success: string;
    warning: string;
    info: string;
  };
}

// App state types
export interface AppState {
  user: UserProfile | null;
  theme: Theme;
  currentTab: 'voice-chat' | 'resources' | 'life-coach';
  isLoading: boolean;
  error: string | null;
}

// Form types
export interface ProfileFormData {
  name: string;
  location: string;
  situation: 'housed' | 'shelter' | 'unsheltered' | 'transitional' | 'risk';
  primary_needs: string[];
  previous_services: string;
}

// Voice interface types
export interface VoiceState {
  isListening: boolean;
  isProcessing: boolean;
  transcript: string;
  error: string | null;
}

// Navigation types
export interface TabConfig {
  id: 'voice-chat' | 'resources' | 'life-coach';
  label: string;
  icon: string;
  description: string;
}

// Error types
export interface AppError {
  message: string;
  code?: string;
  details?: any;
}

// Loading states
export interface LoadingState {
  isLoading: boolean;
  message?: string;
}

// Search filters
export interface ResourceFilters {
  location: string;
  needs: string[];
  type: string;
  category: string;
}

// Local storage keys
export const STORAGE_KEYS = {
  USER_PROFILE: 'social_change_user_profile',
  THEME: 'social_change_theme',
  CONVERSATION_HISTORY: 'social_change_conversation',
  USER_ID: 'social_change_user_id',
} as const;

// API endpoints
export const API_ENDPOINTS = {
  CHAT: {
    MESSAGE: '/api/chat/message',
    CONVERSATION: '/api/chat/conversation',
    VOICE_TO_TEXT: '/api/chat/voice-to-text',
  },
  USERS: {
    PROFILE: '/api/users/profile',
    CONTEXT: '/api/users/profile',
  },
  RESOURCES: {
    SEARCH: '/api/resources/search',
    QUICK_ACTIONS: '/api/resources/quick-actions',
    CATEGORIES: '/api/resources/categories',
    NEARBY: '/api/resources/nearby',
    CRISIS: '/api/resources/crisis',
  },
  HEALTH: '/api/health',
} as const;

// Constants
export const SITUATION_OPTIONS = [
  { value: 'unsheltered', label: 'Unsheltered (sleeping outside)' },
  { value: 'shelter', label: 'In a shelter' },
  { value: 'transitional', label: 'In transitional housing' },
  { value: 'housed', label: 'Housed but at risk' },
  { value: 'risk', label: 'At risk of homelessness' },
] as const;

export const NEED_OPTIONS = [
  { value: 'shelter', label: 'Shelter/Housing' },
  { value: 'food', label: 'Food' },
  { value: 'healthcare', label: 'Healthcare' },
  { value: 'employment', label: 'Employment' },
  { value: 'legal', label: 'Legal Help' },
  { value: 'mental_health', label: 'Mental Health' },
  { value: 'substance_abuse', label: 'Substance Abuse Treatment' },
  { value: 'transportation', label: 'Transportation' },
  { value: 'clothing', label: 'Clothing' },
  { value: 'hygiene', label: 'Hygiene Items' },
] as const;

export const CRISIS_KEYWORDS = [
  'suicide', 'kill myself', 'end it all', 'want to die',
  'hurt myself', 'self-harm', 'overdose', 'dangerous',
  'emergency', 'crisis', 'help me', 'desperate',
  'no hope', 'give up', 'can\'t take it anymore'
] as const; 