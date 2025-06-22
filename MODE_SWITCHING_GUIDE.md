# Mode Switching Implementation Guide

## Overview

Successfully implemented dual-mode functionality for the Social Change Helper app with **Coach Mode** and **Assistant Mode** that provide distinctly different response styles and user experiences.

## 🧠 Coach Mode

**Purpose**: Life coaching, motivation, and emotional support

### Features:

- **Empathetic Response Style**: Warm, encouraging, and confidence-building language
- **Motivational Approach**: Helps users see situations from a clearer perspective
- **Life Advice Focus**: Provides practical wisdom and coping strategies
- **Simplification**: Breaks complex problems into manageable steps
- **Examples & Analogies**: Uses relatable examples to help users understand
- **Minimal Resources**: Focuses on mindset and actionable steps rather than heavy resource lists

### Example Response Style:

```
"I hear you're feeling overwhelmed by your housing situation. Many people have been where you are, and here's what often helps... Let's break this down into simple steps you can take today."
```

## 📋 Assistant Mode

**Purpose**: Resource connection and immediate practical help

### Features:

- **Resource-First Response**: Immediately identifies and provides specific local resources
- **Detailed Information**: Includes addresses, phone numbers, hours, and requirements
- **Contact Details Priority**: Always provides actionable contact information
- **Multiple Options**: Offers backup resources when available
- **Clear Instructions**: Explains exactly how to access services
- **Action Buttons**: Shows Call and Email buttons for immediate contact

### Example Response Style:

```
"Here are food resources in Oakland:
• Alameda County Community Food Bank
• Address: 7900 Edgewater Dr, Oakland, CA 94621
• Phone: (510) 635-3663
• Hours: Monday-Friday, 9am-4pm
• Requirements: None - just show up during operating hours"
```

## 🎯 Frontend Implementation

### Mode Toggle UI

- Added mode toggle buttons in the top navigation bar
- Visual indicators show which mode is currently active
- Smooth transitions between modes

### Assistant Mode Features

- **Action Buttons**: Call and Email buttons appear when in Assistant Mode
- **Resource Extraction**: Automatically extracts phone numbers from responses
- **One-Click Actions**:
  - Call button opens phone app with resource number
  - Email button opens email client with pre-filled message

### Coach Mode Features

- **Clean Interface**: No action buttons, focus on conversation
- **Motivational Design**: Emphasizes the coaching relationship

## 🛠 Backend Implementation

### Enhanced Gemini Service

- **Mode-Specific Prompts**: Different system prompts for each mode
- **Dual Response Styles**: Coach mode focuses on empowerment, Assistant mode on resources
- **RAG Integration**: Assistant mode heavily utilizes local resource database
- **Context Awareness**: Responses adapt based on user location and needs

### API Updates

- **Mode Parameter**: All chat endpoints now accept `mode` parameter
- **Backward Compatibility**: Defaults to coach mode if not specified
- **Resource Integration**: Assistant mode responses include structured resource data

## 📱 Usage Examples

### Coach Mode Conversation:

```
User: "I'm struggling to find housing"
Response: "I understand housing challenges can feel overwhelming. Let's break this down into manageable steps. Many people have found success by first focusing on immediate shelter, then working on longer-term solutions. What's your most urgent need right now - a place to sleep tonight or help with applications for permanent housing?"
```

### Assistant Mode Conversation:

```
User: "I'm struggling to find housing"
Response: "Here are housing resources in your area:

SHELTER OPTIONS:
• Henry Robinson Center
• Address: 1026 Mission Blvd, Oakland, CA
• Phone: (510) 266-2724
• Beds Available: 137
• Call before 7 PM for intake

[Call Resource] [Send Email] buttons appear
```

## 🔄 How to Switch Modes

### For Users:

1. Use the mode toggle buttons in the top navigation
2. **🧠 Coach Mode**: For motivation, life advice, and emotional support
3. **📋 Assistant Mode**: For immediate resources and contact information

### For Developers:

```javascript
// Frontend
switchMode('coach')    // or 'assistant'

// Backend API
{
  "message": "I need help",
  "mode": "coach",      // or "assistant"
  "context": {...}
}
```

## 🎨 Visual Indicators

### Coach Mode:

- Blue accent colors
- Motivational language
- Focus on conversation flow
- No action buttons

### Assistant Mode:

- Resource-focused responses
- Green Call button (📞)
- Blue Email button (✉️)
- Structured information display

## 🧪 Testing

Both modes have been tested and show distinct behavioral differences:

**Coach Mode**: Provides empathetic, motivational responses focused on empowerment
**Assistant Mode**: Provides direct, resource-heavy responses with actionable contact information

The system successfully adapts the AI's personality and response style based on the selected mode while maintaining access to the same underlying resource database.

## 🚀 Benefits

1. **User Choice**: Users can select the type of help they prefer
2. **Situational Flexibility**: Different modes for different needs
3. **Immediate Action**: Assistant mode enables instant contact with resources
4. **Emotional Support**: Coach mode provides motivation and perspective
5. **Comprehensive Help**: Covers both emotional and practical needs

This implementation gives users control over their experience while ensuring they can access both emotional support and practical resources as needed.
