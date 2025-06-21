import React, { useState, useRef, useEffect } from 'react';
import { useTheme } from '../../contexts/ThemeContext';
import { useChat } from '../../contexts/ChatContext';
import { useUser } from '../../contexts/UserContext';
import { MessageBubble } from '../chat/MessageBubble';

export const LifeCoachTab: React.FC = () => {
  const { theme } = useTheme();
  const { messages, sendMessage, isLoading, setMode } = useChat();
  const { user } = useUser();
  
  const [inputMessage, setInputMessage] = useState('');
  const messagesEndRef = useRef<HTMLDivElement>(null);

  // Set mode to coach when component mounts
  useEffect(() => {
    setMode('coach');
  }, [setMode]);

  // Auto-scroll to bottom when new messages arrive
  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  const handleSendMessage = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!inputMessage.trim() || isLoading) return;

    const message = inputMessage.trim();
    setInputMessage('');
    await sendMessage(message, 'coach');
  };

  const handleQuickGoal = async (goal: string) => {
    await sendMessage(goal, 'coach');
  };

  const coachMessages = messages.filter(msg => msg.mode === 'coach');

  return (
    <div style={{ display: 'flex', gap: '1rem', height: 'calc(100vh - 200px)' }}>
      {/* Main Coaching Area */}
      <div style={{ flex: 1, display: 'flex', flexDirection: 'column' }}>
        {/* Header */}
        <div style={{ textAlign: 'center', marginBottom: '2rem' }}>
          <h2 style={{
            fontSize: '1.5rem',
            fontWeight: '600',
            color: theme.colors.text,
            marginBottom: '0.5rem',
          }}>
            🎯 Life Coach
          </h2>
          <p style={{
            color: theme.colors.textSecondary,
            fontSize: '0.875rem',
            maxWidth: '600px',
            margin: '0 auto',
          }}>
            Get personalized coaching to set goals, build confidence, and create action plans for your future.
          </p>
        </div>

        {/* Chat Messages */}
        {coachMessages.length > 0 ? (
          <div className="chat-container">
            <div className="chat-messages">
              {coachMessages.map((message) => (
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
                placeholder="Tell me about your goals or what you'd like to work on..."
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
        ) : (
          /* Welcome Screen */
          <div style={{ textAlign: 'center', padding: '2rem' }}>
            <div style={{
              fontSize: '4rem',
              marginBottom: '1rem',
            }}>
              🎯
            </div>
            <h3 style={{
              fontSize: '1.25rem',
              fontWeight: '600',
              color: theme.colors.text,
              marginBottom: '1rem',
            }}>
              Ready to work on your goals?
            </h3>
            <p style={{
              color: theme.colors.textSecondary,
              fontSize: '0.875rem',
              marginBottom: '2rem',
              maxWidth: '500px',
              margin: '0 auto 2rem',
            }}>
              I'm here to help you set meaningful goals, build confidence, and create actionable steps 
              toward the life you want to live. Let's start by talking about what matters most to you.
            </p>

            {/* Quick Start Goals */}
            <div style={{
              display: 'grid',
              gridTemplateColumns: 'repeat(auto-fit, minmax(250px, 1fr))',
              gap: '1rem',
              maxWidth: '800px',
              margin: '0 auto',
            }}>
              <button
                onClick={() => handleQuickGoal("I want to set some goals for my future")}
                className="btn btn-secondary"
                style={{ 
                  justifyContent: 'flex-start', 
                  textAlign: 'left',
                  padding: '1rem',
                  height: 'auto',
                }}
              >
                <div style={{ fontSize: '1.5rem', marginBottom: '0.5rem' }}>🎯</div>
                <div>
                  <div style={{ fontWeight: '600', marginBottom: '0.25rem' }}>Set Goals</div>
                  <div style={{ fontSize: '0.75rem', opacity: 0.8 }}>
                    Define what you want to achieve
                  </div>
                </div>
              </button>

              <button
                onClick={() => handleQuickGoal("I need help building confidence")}
                className="btn btn-secondary"
                style={{ 
                  justifyContent: 'flex-start', 
                  textAlign: 'left',
                  padding: '1rem',
                  height: 'auto',
                }}
              >
                <div style={{ fontSize: '1.5rem', marginBottom: '0.5rem' }}>🌟</div>
                <div>
                  <div style={{ fontWeight: '600', marginBottom: '0.25rem' }}>Build Confidence</div>
                  <div style={{ fontSize: '0.75rem', opacity: 0.8 }}>
                    Work on self-esteem and belief
                  </div>
                </div>
              </button>

              <button
                onClick={() => handleQuickGoal("I want to create an action plan")}
                className="btn btn-secondary"
                style={{ 
                  justifyContent: 'flex-start', 
                  textAlign: 'left',
                  padding: '1rem',
                  height: 'auto',
                }}
              >
                <div style={{ fontSize: '1.5rem', marginBottom: '0.5rem' }}>📋</div>
                <div>
                  <div style={{ fontWeight: '600', marginBottom: '0.25rem' }}>Action Plan</div>
                  <div style={{ fontSize: '0.75rem', opacity: 0.8 }}>
                    Break down goals into steps
                  </div>
                </div>
              </button>

              <button
                onClick={() => handleQuickGoal("I need motivation and encouragement")}
                className="btn btn-secondary"
                style={{ 
                  justifyContent: 'flex-start', 
                  textAlign: 'left',
                  padding: '1rem',
                  height: 'auto',
                }}
              >
                <div style={{ fontSize: '1.5rem', marginBottom: '0.5rem' }}>💪</div>
                <div>
                  <div style={{ fontWeight: '600', marginBottom: '0.25rem' }}>Get Motivated</div>
                  <div style={{ fontSize: '0.75rem', opacity: 0.8 }}>
                    Find inspiration and encouragement
                  </div>
                </div>
              </button>

              <button
                onClick={() => handleQuickGoal("I want to improve my life situation")}
                className="btn btn-secondary"
                style={{ 
                  justifyContent: 'flex-start', 
                  textAlign: 'left',
                  padding: '1rem',
                  height: 'auto',
                }}
              >
                <div style={{ fontSize: '1.5rem', marginBottom: '0.5rem' }}>📈</div>
                <div>
                  <div style={{ fontWeight: '600', marginBottom: '0.25rem' }}>Life Improvement</div>
                  <div style={{ fontSize: '0.75rem', opacity: 0.8 }}>
                    Work on overall life changes
                  </div>
                </div>
              </button>

              <button
                onClick={() => handleQuickGoal("I want to talk about my strengths")}
                className="btn btn-secondary"
                style={{ 
                  justifyContent: 'flex-start', 
                  textAlign: 'left',
                  padding: '1rem',
                  height: 'auto',
                }}
              >
                <div style={{ fontSize: '1.5rem', marginBottom: '0.5rem' }}>✨</div>
                <div>
                  <div style={{ fontWeight: '600', marginBottom: '0.25rem' }}>Find Strengths</div>
                  <div style={{ fontSize: '0.75rem', opacity: 0.8 }}>
                    Discover and build on your talents
                  </div>
                </div>
              </button>
            </div>

            {/* Coaching Tips */}
            <div style={{
              marginTop: '3rem',
              padding: '1.5rem',
              backgroundColor: theme.colors.info + '20',
              borderRadius: '8px',
              maxWidth: '600px',
              margin: '3rem auto 0',
            }}>
              <h4 style={{
                fontSize: '1rem',
                fontWeight: '600',
                color: theme.colors.text,
                marginBottom: '1rem',
              }}>
                💡 Coaching Approach
              </h4>
              <div style={{
                display: 'grid',
                gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))',
                gap: '1rem',
                fontSize: '0.875rem',
                color: theme.colors.textSecondary,
              }}>
                <div>
                  <strong>🎯 Goal-Oriented:</strong> We'll work together to set clear, achievable goals.
                </div>
                <div>
                  <strong>🌟 Strengths-Based:</strong> We'll focus on your abilities and build from there.
                </div>
                <div>
                  <strong>📋 Action-Focused:</strong> We'll create concrete steps to move forward.
                </div>
                <div>
                  <strong>💪 Encouraging:</strong> I'll provide support and celebrate your progress.
                </div>
              </div>
            </div>
          </div>
        )}
      </div>

      {/* Coaching Sidebar */}
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
        <h4 style={{
          fontSize: '0.875rem',
          fontWeight: '600',
          color: theme.colors.text,
          marginBottom: '1rem',
        }}>
          🎯 Coaching Session
        </h4>

        <div style={{
          marginBottom: '1.5rem',
          padding: '1rem',
          backgroundColor: theme.colors.background,
          borderRadius: '6px',
        }}>
          <div style={{
            fontSize: '0.75rem',
            color: theme.colors.textSecondary,
          }}>
            <div><strong>Mode:</strong> Life Coach</div>
            <div><strong>Messages:</strong> {coachMessages.length}</div>
            <div><strong>Focus:</strong> Goals & Growth</div>
          </div>
        </div>

        <div style={{ marginBottom: '1.5rem' }}>
          <h5 style={{
            fontSize: '0.875rem',
            fontWeight: '600',
            color: theme.colors.text,
            marginBottom: '0.75rem',
          }}>
            💭 Reflection Prompts
          </h5>
          <div style={{
            fontSize: '0.75rem',
            color: theme.colors.textSecondary,
          }}>
            <div style={{ marginBottom: '0.5rem' }}>
              • What would success look like for you?
            </div>
            <div style={{ marginBottom: '0.5rem' }}>
              • What's one small step you can take today?
            </div>
            <div style={{ marginBottom: '0.5rem' }}>
              • What are you most proud of?
            </div>
            <div>
              • What would you like to change?
            </div>
          </div>
        </div>

        <div style={{
          padding: '1rem',
          backgroundColor: theme.colors.success + '20',
          borderRadius: '6px',
          fontSize: '0.75rem',
        }}>
          <h5 style={{
            fontSize: '0.875rem',
            fontWeight: '600',
            color: theme.colors.text,
            marginBottom: '0.5rem',
          }}>
            🌟 Remember
          </h5>
          <div style={{ color: theme.colors.textSecondary }}>
            Every step forward, no matter how small, is progress worth celebrating. 
            You have the strength within you to create positive change.
          </div>
        </div>
      </div>
    </div>
  );
}; 