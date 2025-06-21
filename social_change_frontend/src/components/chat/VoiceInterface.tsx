import React, { useState, useEffect } from 'react';
import { useTheme } from '../../contexts/ThemeContext';

interface VoiceInterfaceProps {
  isListening: boolean;
  onListeningChange: (listening: boolean) => void;
  onTranscript: (transcript: string) => void;
}

export const VoiceInterface: React.FC<VoiceInterfaceProps> = ({
  isListening,
  onListeningChange,
  onTranscript,
}) => {
  const { theme } = useTheme();
  const [transcript, setTranscript] = useState('');
  const [isProcessing, setIsProcessing] = useState(false);

  const handleVoiceButtonClick = () => {
    if (isListening) {
      // Stop listening
      onListeningChange(false);
      if (transcript.trim()) {
        setIsProcessing(true);
        // Simulate processing delay
        setTimeout(() => {
          onTranscript(transcript);
          setTranscript('');
          setIsProcessing(false);
        }, 1000);
      }
    } else {
      // Start listening
      onListeningChange(true);
      setTranscript('');
      // Simulate voice input after 2 seconds
      setTimeout(() => {
        const sampleTranscripts = [
          "I need help finding shelter",
          "I'm looking for food assistance",
          "I need medical care",
          "Can you help me find a job",
          "I'm feeling overwhelmed and need support",
          "I want to set some goals for my future",
          "I need help with transportation",
          "I'm looking for mental health resources"
        ];
        const randomTranscript = sampleTranscripts[Math.floor(Math.random() * sampleTranscripts.length)];
        setTranscript(randomTranscript);
      }, 2000);
    }
  };

  return (
    <div style={{ textAlign: 'center' }}>
      {/* Voice Button */}
      <button
        onClick={handleVoiceButtonClick}
        className={`voice-button ${isListening ? 'listening' : ''}`}
        disabled={isProcessing}
        title={isListening ? 'Click to stop listening' : 'Click to start voice input'}
        aria-label={isListening ? 'Stop listening' : 'Start voice input'}
      >
        {isProcessing ? (
          <div className="loading-spinner" style={{ width: '24px', height: '24px' }}></div>
        ) : isListening ? (
          '⏹️'
        ) : (
          '🎤'
        )}
      </button>

      {/* Status Text */}
      <div style={{ marginTop: '1rem' }}>
        {isProcessing && (
          <p style={{
            color: theme.colors.textSecondary,
            fontSize: '0.875rem',
          }}>
            Processing your message...
          </p>
        )}
        
        {isListening && !isProcessing && (
          <p style={{
            color: theme.colors.primary,
            fontSize: '0.875rem',
            fontWeight: '500',
          }}>
            Listening... Click to stop
          </p>
        )}
        
        {!isListening && !isProcessing && (
          <p style={{
            color: theme.colors.textSecondary,
            fontSize: '0.875rem',
          }}>
            Click the microphone to start voice input
          </p>
        )}
      </div>

      {/* Transcript Display */}
      {transcript && (
        <div style={{
          marginTop: '1rem',
          padding: '1rem',
          backgroundColor: theme.colors.background,
          border: `1px solid ${theme.colors.border}`,
          borderRadius: '8px',
          maxWidth: '400px',
          margin: '1rem auto 0',
        }}>
          <p style={{
            color: theme.colors.text,
            fontSize: '0.875rem',
            margin: 0,
            fontStyle: 'italic',
          }}>
            "{transcript}"
          </p>
          {isListening && (
            <p style={{
              color: theme.colors.textSecondary,
              fontSize: '0.75rem',
              margin: '0.5rem 0 0 0',
            }}>
              Click the button above to send this message
            </p>
          )}
        </div>
      )}

      {/* Voice Input Instructions */}
      <div style={{
        marginTop: '2rem',
        padding: '1rem',
        backgroundColor: theme.colors.info + '20',
        borderRadius: '8px',
        maxWidth: '500px',
        margin: '2rem auto 0',
      }}>
        <h4 style={{
          fontSize: '0.875rem',
          fontWeight: '600',
          color: theme.colors.text,
          marginBottom: '0.5rem',
        }}>
          💡 Voice Input Tips
        </h4>
        <ul style={{
          fontSize: '0.75rem',
          color: theme.colors.textSecondary,
          textAlign: 'left',
          margin: 0,
          paddingLeft: '1rem',
        }}>
          <li>Speak clearly and at a normal pace</li>
          <li>Try phrases like "I need help with..." or "Can you help me find..."</li>
          <li>You can also type your message below</li>
          <li>For crisis situations, mention "crisis" or "emergency"</li>
        </ul>
      </div>
    </div>
  );
}; 