import React, { useState, useRef, useEffect } from 'react';
import { useTheme } from '../../contexts/ThemeContext';
import { useChat } from '../../contexts/ChatContext';
import { useUser } from '../../contexts/UserContext';
import { VoiceInterface } from '../chat/VoiceInterface';
import { ChatSidebar } from '../chat/ChatSidebar';
import { MessageBubble } from '../chat/MessageBubble';

export const VoiceChatTab: React.FC = () => {
  const { theme } = useTheme();
  const { messages, sendMessage, isLoading, currentMode, setMode } = useChat();
  const { user } = useUser();
  
  const [inputMessage, setInputMessage] = useState('');
  const [isListening, setIsListening] = useState(false);
  const messagesEndRef = useRef<HTMLDivElement>(null);

  // Auto-scroll to bottom when new messages arrive
  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  const handleSendMessage = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!inputMessage.trim() || isLoading) return;

    const message = inputMessage.trim();
    setInputMessage('');
    await sendMessage(message, currentMode);
  };

  const handleVoiceInput = async (transcript: string) => {
    if (transcript.trim()) {
      await sendMessage(transcript, currentMode);
    }
  };

  const handleModeToggle = () => {
    setMode(currentMode === 'support' ? 'coach' : 'support');
  };

  return (
    <div style={{ display: 'flex', gap: '1rem', height: 'calc(100vh - 200px)' }}>
      {/* Main Chat Area */}
      <div style={{ flex: 1, display: 'flex', flexDirection: 'column' }}>
        {/* Mode Toggle */}
        <div style={{
          display: 'flex',
          justifyContent: 'center',
          marginBottom: '1rem',
        }}>
          <div style={{
            display: 'flex',
            backgroundColor: theme.colors.background,
            borderRadius: '8px',
            padding: '4px',
            border: `1px solid ${theme.colors.border}`,
          }}>
            <button
              onClick={() => setMode('support')}
              className={`btn ${currentMode === 'support' ? 'btn-primary' : 'btn-text'}`}
              style={{
                borderRadius: '4px',
                fontSize: '0.875rem',
              }}
            >
              💬 Support Mode
            </button>
            <button
              onClick={() => setMode('coach')}
              className={`btn ${currentMode === 'coach' ? 'btn-primary' : 'btn-text'}`}
              style={{
                borderRadius: '4px',
                fontSize: '0.875rem',
              }}
            >
              🎯 Coach Mode
            </button>
          </div>
        </div>

        {/* Voice Interface */}
        <div className="voice-interface">
          <VoiceInterface
            isListening={isListening}
            onListeningChange={setIsListening}
            onTranscript={handleVoiceInput}
          />
          
          <div style={{ textAlign: 'center', maxWidth: '400px' }}>
            <h3 style={{
              fontSize: '1.25rem',
              fontWeight: '600',
              color: theme.colors.text,
              marginBottom: '0.5rem',
            }}>
              {currentMode === 'support' ? 'Get Support & Resources' : 'Life Coaching & Goals'}
            </h3>
            <p style={{
              color: theme.colors.textSecondary,
              fontSize: '0.875rem',
            }}>
              {currentMode === 'support' 
                ? 'Talk to our AI assistant for immediate support, resource recommendations, and crisis help.'
                : 'Get personalized coaching to set goals, build confidence, and create action plans.'
              }
            </p>
          </div>
        </div>

        {/* Chat Messages */}
        {messages.length > 0 && (
          <div className="chat-container">
            <div className="chat-messages">
              {messages.map((message) => (
                <MessageBubble key={message.message_id} message={message} />
              ))}
              <div ref={messagesEndRef} />
            </div>

            {/* Text Input */}
            <form onSubmit={handleSendMessage} className="chat-input">
              <input
                type="text"
                className="input"
                value={inputMessage}
                onChange={(e) => setInputMessage(e.target.value)}
                placeholder="Type your message here..."
                disabled={isLoading}
              />
              <button
                type="submit"
                className="btn btn-primary"
                disabled={!inputMessage.trim() || isLoading}
              >
                {isLoading ? (
                  <div className="loading-spinner" style={{ width: '16px', height: '16px' }}></div>
                ) : (
                  'Send'
                )}
              </button>
            </form>
          </div>
        )}

        {/* Quick Actions */}
        {messages.length === 0 && (
          <div style={{ marginTop: '2rem' }}>
            <h4 style={{
              fontSize: '1rem',
              fontWeight: '600',
              color: theme.colors.text,
              marginBottom: '1rem',
            }}>
              Quick Start
            </h4>
            <div style={{
              display: 'grid',
              gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))',
              gap: '1rem',
            }}>
              {currentMode === 'support' ? (
                <>
                  <button
                    onClick={() => sendMessage("I need help finding shelter")}
                    className="btn btn-secondary"
                    style={{ justifyContent: 'flex-start', textAlign: 'left' }}
                  >
                    🏠 Find shelter
                  </button>
                  <button
                    onClick={() => sendMessage("I need food assistance")}
                    className="btn btn-secondary"
                    style={{ justifyContent: 'flex-start', textAlign: 'left' }}
                  >
                    🍽️ Get food help
                  </button>
                  <button
                    onClick={() => sendMessage("I need medical care")}
                    className="btn btn-secondary"
                    style={{ justifyContent: 'flex-start', textAlign: 'left' }}
                  >
                    🏥 Medical care
                  </button>
                  <button
                    onClick={() => sendMessage("I'm in crisis and need immediate help")}
                    className="btn btn-secondary"
                    style={{ justifyContent: 'flex-start', textAlign: 'left' }}
                  >
                    🆘 Crisis help
                  </button>
                </>
              ) : (
                <>
                  <button
                    onClick={() => sendMessage("Help me set some goals")}
                    className="btn btn-secondary"
                    style={{ justifyContent: 'flex-start', textAlign: 'left' }}
                  >
                    🎯 Set goals
                  </button>
                  <button
                    onClick={() => sendMessage("I need motivation")}
                    className="btn btn-secondary"
                    style={{ justifyContent: 'flex-start', textAlign: 'left' }}
                  >
                    💪 Get motivated
                  </button>
                  <button
                    onClick={() => sendMessage("Help me build confidence")}
                    className="btn btn-secondary"
                    style={{ justifyContent: 'flex-start', textAlign: 'left' }}
                  >
                    🌟 Build confidence
                  </button>
                  <button
                    onClick={() => sendMessage("I want to improve my life")}
                    className="btn btn-secondary"
                    style={{ justifyContent: 'flex-start', textAlign: 'left' }}
                  >
                    📈 Life improvement
                  </button>
                </>
              )}
            </div>
          </div>
        )}
      </div>

      {/* Sidebar */}
      <ChatSidebar />
    </div>
  );
}; 