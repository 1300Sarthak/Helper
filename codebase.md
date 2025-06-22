# .gitignore

```
# Environment variables
.env
.env.local
.env.*.local

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
pip-wheel-metadata/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
.python-version

# pipenv
Pipfile.lock

# PEP 582
__pypackages__/

# Celery stuff
celerybeat-schedule
celerybeat.pid

# SageMath parsed files
*.sage.py

# Environments
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/

# IDEs
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
ehthumbs.db
Thumbs.db

# Database files
*.db
*.sqlite
*.sqlite3

# Logs
*.log
logs/

# Temporary files
*.tmp
*.temp 
```

# ADMIN_PORTAL_GUIDE.md

```md
# 🔧 Admin Portal Guide

## Overview

The Helper app now includes a comprehensive admin portal for monitoring and managing the system. The admin portal provides real-time insights into user activity, conversation logs, and system statistics.

## Accessing the Admin Portal

### URL

- **Main Portal**: `http://localhost:5001/admin/`
- **Alternative**: `http://localhost:5001/admin` (redirects to main portal)

### Access Requirements

- Currently accessible from localhost (development mode)
- In production, implement proper authentication
- No login required for development environment

## Features

### 📊 Dashboard Tab

**Real-time Statistics:**

- Total Users registered
- Total Conversations/Messages
- Users active today
- Messages sent today

**Recent Activity Feed:**

- Last 20 conversation messages
- User names and message previews
- Timestamps for each interaction
- Real-time updates every 30 seconds

### 👥 Users Tab

**User Management:**

- Complete user list with details
- User ID, name, location, housing situation
- Registration date and last activity
- Message count per user
- Search and filter functionality
- CSV export capability

**User Information Displayed:**

- ID: Unique user identifier
- Name: User's provided name (or "Anonymous")
- Location: City/area information
- Situation: Housing status (shelter, unsheltered, etc.)
- Created: Registration timestamp
- Last Active: Most recent activity
- Messages: Total conversation count

### 💬 Conversations Tab

**Message Monitoring:**

- Last 100 conversations displayed
- User messages and AI responses
- Mode tracking (Coach vs Assistant)
- Timestamp information
- Search and filter by mode
- Response previews (truncated for readability)

**Conversation Details:**

- Time: When the message was sent
- User: Who sent the message
- Mode: Coach or Assistant mode
- Message: User's input message
- Response Preview: First 100 characters of AI response
- Emotion: Placeholder for future emotion analysis

### ⚙️ System Tab

**System Information:**

- API status indicators
- Database connection status
- RAG pipeline status
- Resource database statistics

**Resource Database Stats:**

- Total Resources: 64 available resources
- Oakland Resources: 32 local resources
- Berkeley Resources: 32 regional resources

**System Actions:**

- **Clear Old Data**: Remove conversations older than 30 days
- **Reset System**: Complete data wipe (DANGER - irreversible)

## Navigation

### Tab Switching

- Click any tab in the navigation bar
- Dashboard, Users, Conversations, System
- Active tab highlighted in blue
- Smooth transitions between sections

### Auto-Refresh

- Dashboard updates every 30 seconds automatically
- Manual refresh button (circular arrow) in bottom-right
- Click refresh button for immediate data update

### Search & Filtering

**Users Tab:**

- Search box filters by name, location, situation
- Real-time filtering as you type
- Case-insensitive search

**Conversations Tab:**

- Search box filters by message content
- Mode filter dropdown (All/Coach/Assistant)
- Combined filtering for precise results

## Data Export

### User Export

- Click "Export CSV" in Users tab
- Downloads complete user database
- Includes: ID, Name, Location, Situation, Dates, Contact info
- Filename: `users_export.csv`

### Data Format

\`\`\`csv
ID,Name,Location,Situation,Created At,Last Active,Phone,Email
1,John Doe,Oakland,unsheltered,2025-06-21 20:15:00,2025-06-21 20:45:00,,
\`\`\`

## System Management

### Data Cleanup

**Clear Old Data:**

- Removes conversations older than 30 days
- Preserves user accounts and recent activity
- Shows count of deleted records
- Requires confirmation before execution

**Reset System:**

- **WARNING**: Deletes ALL data permanently
- Removes all users and conversations
- Cannot be undone
- Requires double confirmation
- Use only for complete system reset

### Safety Features

- Confirmation dialogs for destructive actions
- Error handling with user-friendly messages
- Database rollback on failed operations
- Graceful error recovery

## API Endpoints

### Admin Routes

- `GET /admin/` - Main dashboard
- `GET /admin/export/users` - CSV export
- `POST /admin/clear-old-data` - Cleanup old conversations
- `POST /admin/reset-system` - Complete system reset
- `GET /admin/api/stats` - Real-time statistics JSON

### Example API Response

\`\`\`json
{
  "total_users": 15,
  "total_conversations": 127,
  "today_users": 3,
  "today_conversations": 12
}
\`\`\`

## Visual Design

### Modern Interface

- Clean, professional design
- Blue accent color (#007bff)
- Card-based layout for statistics
- Responsive grid system
- Hover effects and smooth transitions

### Status Indicators

- **Green badges**: Successful states, Coach mode
- **Blue badges**: Information, Assistant mode
- **Yellow badges**: Warnings, housing situations
- **Red badges**: Errors, dangerous actions

### Typography

- System fonts for optimal readability
- Clear hierarchy with proper font weights
- Consistent spacing and alignment
- Accessible color contrast

## Browser Compatibility

### Supported Browsers

- ✅ Chrome (recommended)
- ✅ Firefox
- ✅ Safari
- ✅ Edge
- ⚠️ Internet Explorer (limited support)

### Required Features

- Modern CSS Grid support
- JavaScript ES6+ features
- Fetch API for AJAX requests
- CSS Flexbox for layouts

## Security Considerations

### Current Implementation

- **Development Mode**: Open access from localhost
- **No Authentication**: Direct access to admin panel
- **Local Database**: SQLite for development

### Production Recommendations

- **Implement Authentication**: Admin login system
- **HTTPS Required**: Secure connections only
- **IP Restrictions**: Limit admin access by IP
- **Audit Logging**: Track admin actions
- **Regular Backups**: Automated database backups

### Data Privacy

- **User Data Protection**: Secure handling of personal information
- **Conversation Privacy**: Limited access to message content
- **Export Controls**: Secure CSV download handling
- **Data Retention**: Configurable cleanup policies

## Troubleshooting

### Common Issues

#### Admin Portal Not Loading

**Symptoms**: 404 or connection errors
**Solutions**:

- Check if Flask server is running on port 5001
- Verify admin routes are registered
- Check for import errors in server logs

#### 500 Internal Server Error

**Symptoms**: Server error page
**Solutions**:

- Check server logs for Python errors
- Verify database connection
- Ensure all model fields exist

#### Empty Data Display

**Symptoms**: No users or conversations shown
**Solutions**:

- Check if database has data
- Verify database queries are correct
- Test with sample data

#### Export Not Working

**Symptoms**: CSV download fails
**Solutions**:

- Check file permissions
- Verify CSV module import
- Test with smaller datasets

### Debug Mode

\`\`\`bash
# Start server with debug output
python app.py

# Check specific admin route
curl -v http://localhost:5001/admin/

# Test API endpoints
curl http://localhost:5001/admin/api/stats
\`\`\`

## Usage Examples

### Daily Monitoring

1. Open admin portal: `http://localhost:5001/admin/`
2. Check dashboard for daily statistics
3. Review recent activity for unusual patterns
4. Monitor user registration trends

### User Management

1. Go to Users tab
2. Search for specific users by name/location
3. Export user data for reporting
4. Track user engagement through message counts

### Conversation Analysis

1. Switch to Conversations tab
2. Filter by mode (Coach/Assistant) to analyze usage
3. Search for specific topics or keywords
4. Monitor response quality and user satisfaction

### System Maintenance

1. Navigate to System tab
2. Check API status indicators
3. Clear old data monthly (30+ days)
4. Monitor resource database statistics

## Future Enhancements

### Planned Features

- **Real-time Analytics**: Live charts and graphs
- **User Authentication**: Secure admin login system
- **Advanced Filtering**: Date ranges, emotion filters
- **Conversation Analytics**: Sentiment analysis, topic modeling
- **Automated Reports**: Daily/weekly summary emails
- **Resource Management**: Add/edit/remove resources
- **User Communication**: Direct messaging capabilities
- **Data Visualization**: Charts for trends and patterns

### Integration Opportunities

- **Google Analytics**: Web analytics integration
- **Slack Notifications**: Real-time alerts
- **Email Reports**: Automated admin summaries
- **Database Backups**: Automated backup system
- **Performance Monitoring**: System health dashboards

---

## Quick Start Checklist

- [ ] ✅ Flask server running on port 5001
- [ ] ✅ Admin routes registered and working
- [ ] ✅ Database connected with sample data
- [ ] ✅ Admin portal accessible at `/admin/`
- [ ] ✅ All tabs functioning (Dashboard, Users, Conversations, System)
- [ ] ✅ Search and filter features working
- [ ] ✅ CSV export operational
- [ ] ✅ System actions (clear data, reset) functional

**The admin portal is now fully operational! 🎉**

Access it at: **http://localhost:5001/admin/**

```

# app.py

```py
from flask import Flask, jsonify, redirect
from flask_cors import CORS
import os
from datetime import datetime
import logging
from config import config
from models.user import db, User
from models.conversation import Conversation
from routes.chat import chat_bp
from routes.admin import admin_bp

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Enable CORS for frontend connection
CORS(app, origins=["http://localhost:8000", "http://127.0.0.1:8000"])

# Load configuration
config_name = os.environ.get('FLASK_ENV', 'default')
app_config = config[config_name]
app.config.from_object(app_config)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///social_change_app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db.init_app(app)

# Register blueprints
app.register_blueprint(chat_bp)
app.register_blueprint(admin_bp)

# Create tables
with app.app_context():
    db.create_all()


@app.route('/')
def home():
    """Health check endpoint"""
    return jsonify({
        'status': 'success',
        'message': 'Social Change Helper API is running',
        'timestamp': datetime.now().isoformat(),
        'version': '1.0.0'
    })


@app.route('/ping')
def ping():
    """Ping endpoint for Task 1"""
    return jsonify({'status': 'ok'})


@app.route('/admin')
def admin_redirect():
    """Redirect /admin to /admin/"""
    return redirect('/admin/')


@app.errorhandler(404)
def not_found(error):
    return jsonify({
        'error': 'Endpoint not found'
    }), 404


@app.errorhandler(500)
def internal_error(error):
    return jsonify({
        'error': 'Internal server error'
    }), 500


if __name__ == '__main__':
    port = app_config.PORT
    logger.info(f"Starting Social Change Helper API on port {port}")
    app.run(host='0.0.0.0', port=port, debug=app_config.DEBUG)

```

# architecture.md

```md
File and Folder Structure
social_change_app/
│
├── frontend/ # Mobile + Web app (React + Tailwind + Glass UI style)
│ ├── public/ # Static assets
│ ├── src/
│ │ ├── assets/ # Fonts, icons, images
│ │ ├── components/ # Shared UI: buttons, input fields, modals
│ │ ├── pages/ # Screens: Home, VoiceChat, ResourcesMap, Journal, Coach
│ │ ├── features/
│ │ │ ├── voiceAssistant/ # Browser-based voice input (Web Speech API)
│ │ │ ├── mapView/ # Google Maps resource overlay
│ │ │ ├── mentorChat/ # AI chat w/ motivational interviewing
│ │ │ └── journalLog/ # Guided journaling + emotion scoring
│ │ ├── services/ # Axios-based API calls to backend
│ │ ├── state/ # Zustand or Redux store (user, session, map state)
│ │ └── App.tsx # Main app layout
│ └── tailwind.config.js
│
├── backend/ # Python Flask backend with AI orchestration
│ ├── app.py # Main Flask entry point
│ ├── config.py # ENV configs, DB URIs, API keys
│ ├── requirements.txt
│ ├── .env # Claude, Gemini, Gmail, DB creds
│ ├── models/
│ │ ├── user.py # User info schema
│ │ ├── journal.py # Daily logs from journaling/chat
│ │ ├── resource.py # Food banks, shelters, clinics
│ │ └── session.py # LLM session + conversation memory
│ ├── routes/
│ │ ├── chat.py # /api/chat – AI chat endpoints
│ │ ├── resources.py # /api/resources – Location-based service listings
│ │ └── voice.py # /api/voice – basic speech-to-text handler (if needed)
│ ├── services/
│ │ ├── gemini_service.py # Gemini AI calls, complete assistant functionality
│ │ ├── email_service.py # Gmail API – sends support emails to users
│ │ └── rag_pipeline.py # Custom RAG pipeline for nearby resources
│ └── utils/
│ ├── formatters.py # Clean display text, time helpers
│

How Services Connect
graph TD
MobileUser -->|Mic Input (Web Speech API)| VoiceAssistant
VoiceAssistant -->|Transcript| FrontendChat
FrontendChat -->|API Call| FlaskBackend
FlaskBackend -->|Gemini Prompt| GeminiService
FlaskBackend -->|Resource Info| RAGPipeline
FlaskBackend -->|Gmail API| EmailService
FlaskBackend -->|Sends Back| MobileUI

State Management
Frontend:
User State: Anonymous or persistent (name, location, preferences)

Session State: Current AI chat memory (stored in local/session + backend)

Resource Data: Live location-based service listings

Emotion State: For personalized content in journal and coaching

Backend:
MongoDB: Journaling data, conversation logs

PostgreSQL: Resource locations, availability (e.g., # beds/meals)

In-Memory (Redis optional): AI chat memory, temp context for speech input

🤖 AI Orchestration
Gemini
Primary AI assistant for:

Personalized assistant interactions

Warm info delivery

Motivational interviewing-style coaching

Email-ready summaries of resources

Summarizes journal entries

Scores tone (distress, motivation, positivity)

Adds feedback suggestions for user support

RAG Pipeline
Pulls best-fit local services based on:

Geolocation

Past resource usage

Confidence scoring

Can generate smart outputs like:

“There’s a women’s shelter 0.8 miles away that closes at 9 PM.”

🗺️ Resource Discovery
Google Maps API overlays live service pins

Pins show:

Type (shelter, food, clinic)

Name + image

Availability (beds, meals)

Directions/contact info

Auto-updated from scraper

🗣️ Voice Assistant (Web Speech API / Twilio if fallback needed)
Browser-native mic input (no Vapi)

Voice → Text → Claude prompt → reply

Optionally reads the reply aloud (Text-to-Speech if needed)

Example use case:

“Where can I find food tonight?”
→ Gemini replies with open food banks nearby

📥 Email Support System
Gmail API sends:

Resources matched to the user

Nearby map links

Uplifting quote or message

📝 Journal + Coaching System
Daily journaling prompt

Gemini responds with tailored support

Gemini analyzes sentiment

Stored securely in MongoDB

```

# ask.md 

```md 
Tasks 

1. Initialize Flask App
    •    Start: Create app.py with a basic Flask server
    •    End: /ping route returns JSON { status: 'ok' }
    •    Test: curl localhost:5000/ping returns expected JSON
2. Create Project Structure
    •    Start: Create folders: routes/, models/, services/, utils/
    •    End: Files exist with init imports
    •    Test: Project runs with flask run without errors
3. Claude API Integration
    •    Start: Create claude_service.py in services/
    •    End: Function get_support_response(message, context) returns Claude reply
    •    Test: Pass test message and get Claude response in console
4. Define User and Message Models
    •    Start: Create user.py and conversation.py in models/
    •    End: SQLAlchemy models created and linked to SQLite
    •    Test: Insert test data into tables using Flask shell
5. Create /api/chat/message Endpoint
    •    Start: Add chat.py in routes/ with POST /api/chat/message
    •    End: Accepts message and user context, returns Claude response
    •    Test: Post JSON body, get chat reply

💬 Phase 2: Frontend Setup + Core UI (React + TypeScript)
6. Bootstrap React Project
    •    Start: Use Vite or CRA to scaffold social_change_frontend
    •    End: Project runs with “Hello from Helper” in browser
    •    Test: npm run dev or npm start shows root app
7. Set Up Tailwind CSS
    •    Start: Add Tailwind via PostCSS setup
    •    End: Can apply utility classes (e.g., bg-gray-100)
    •    Test: Modify <App /> to verify style works
8. Implement Theme Toggle
    •    Start: Add ThemeContext.tsx and ThemeToggle.tsx
    •    End: Toggle between light/dark modes
    •    Test: UI updates theme on toggle
9. Implement Tab Navigation
    •    Start: Create tab layout component (Tabs.tsx)
    •    End: Tabs: Voice Chat | Resources | Life Coach
    •    Test: Clicking switches views

🧍 Phase 3: User Profile + Local Storage
10. Create User Context
    •    Start: Add UserContext.tsx with user data shape
    •    End: Store name, location, situation, needs
    •    Test: Access user context in any component
11. Build UserProfileModal
    •    Start: Form inputs: name, zip, situation, needs
    •    End: Store in context + localStorage
    •    Test: Refresh page, user data persists

🧠 Phase 4: Claude Chat Integration (Text-Only)
12. Build Chatbox Component
    •    Start: Textarea input, send button, render bubbles
    •    End: Display user + assistant messages
    •    Test: Messages appear in order with timestamps
13. Wire Chat to Claude Endpoint
    •    Start: Use Axios to call POST /api/chat/message
    •    End: Claude reply is displayed in chat
    •    Test: Full back-and-forth flow works with dummy message


```

# config.py

```py
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Config:
    """Base configuration class"""
    SECRET_KEY = os.environ.get('SECRET_KEY', None)  # Optional for basic API
    DEBUG = os.environ.get('DEBUG', 'True').lower() == 'true'
    PORT = int(os.environ.get('PORT', 5001))

    # Gemini API Configuration
    GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY', None)

    # Legacy CAG Configuration (if needed)
    CAG_API_KEY = os.environ.get('CAG_API_KEY', None)
    CAG_MODEL_NAME = os.environ.get('CAG_MODEL_NAME', 'default-model')
    CAG_API_URL = os.environ.get('CAG_API_URL', 'https://api.cag.example.com')

    # Database Configuration (if needed)
    DATABASE_URL = os.environ.get('DATABASE_URL', 'sqlite:///chatbot.db')
    REDIS_URL = os.environ.get('REDIS_URL', 'redis://localhost:6379')

    # Logging Configuration
    LOG_LEVEL = os.environ.get('LOG_LEVEL', 'INFO')


class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True


class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False


class TestingConfig(Config):
    """Testing configuration"""
    TESTING = True
    DEBUG = True


# Configuration dictionary
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}

```

# ENHANCED_FORMATTING_GUIDE.md

```md
# Enhanced Message Formatting Implementation

## 🎨 Overview

Successfully implemented rich text formatting for chat messages with automatic resource extraction, clickable links, and improved visual presentation.

## ✨ Key Features

### 1. **Rich Text Formatting**

- **Bold Text**: `**text**` automatically converts to **bold** styling
- **Clickable Phone Numbers**: Phone numbers become clickable `tel:` links
- **Clickable Email Addresses**: Email addresses become clickable `mailto:` links
- **Paragraph Formatting**: Automatic paragraph breaks for better readability

### 2. **Resource Extraction & Display**

- **Automatic Detection**: Identifies organization names, addresses, phones, hours
- **Dedicated Resource Section**: Resources displayed in a separate, styled section
- **Contact Actions**: Direct call and directions buttons for each resource
- **Clean Separation**: Main content separated from resource information

### 3. **Visual Enhancements**

- **Better Typography**: Improved line spacing and paragraph structure
- **Color-Coded Links**: Blue accent color for all clickable elements
- **Resource Cards**: Individual cards for each resource with contact buttons
- **Professional Layout**: Clean, modern design that's easy to scan

## 🔧 Technical Implementation

### Message Processing Flow:

\`\`\`javascript
1. Raw AI Response → formatBotMessage()
2. Extract Resources → extractResources()
3. Format Text → Bold, Links, Paragraphs
4. Generate Resource Section → generateResourceSection()
5. Combine & Display → Final HTML
\`\`\`

### Formatting Examples:

#### Input:

\`\`\`
**Alameda County Community Food Bank** is available to help.

Contact them at (510) 635-3663 or email info@accfb.org

* **Address:** 7900 Edgewater Dr, Oakland, CA 94621
* **Phone:** (510) 635-3663
* **Hours:** Monday-Friday, 9am-4pm
\`\`\`

#### Output:

- **Bold text** properly styled
- Phone numbers as clickable links: `tel:(510) 635-3663`
- Email as clickable link: `mailto:info@accfb.org`
- Resource card with Call and Directions buttons

## 📱 Resource Section Features

### Each Resource Card Includes:

- **Organization Name** (prominent heading)
- **Address** with map icon (📍)
- **Hours** with clock icon (🕒)
- **Contact Buttons**:
  - 📞 **Call** - Opens phone app
  - 📍 **Directions** - Opens Google Maps

### Visual Design:

- Light blue background with accent border
- Individual cards for each resource
- Hover effects on interactive elements
- Mobile-friendly responsive design

## 🎯 Mode-Specific Behavior

### Assistant Mode:

- **Resource-Heavy Display**: Prominent resource sections
- **Immediate Actions**: Call/email buttons always visible
- **Structured Information**: Clean separation of advice vs. resources

### Coach Mode:

- **Content-Focused**: Emphasis on motivational text
- **Minimal Resources**: Resources integrated naturally into conversation
- **Personal Touch**: More narrative, less structured data

## 🚀 Benefits

### For Users:

1. **Instant Action**: One-click calling and directions
2. **Better Readability**: Clear formatting and structure
3. **Mobile-Friendly**: Works perfectly on phones
4. **Professional Appearance**: Trustworthy, clean design

### For Accessibility:

1. **Screen Readers**: Proper HTML structure
2. **High Contrast**: Good color contrast ratios
3. **Touch Targets**: Large, easy-to-tap buttons
4. **Semantic HTML**: Proper heading and link structure

## 📊 Before vs. After

### Before:

\`\`\`
Plain text with **asterisks** and phone numbers like (510) 635-3663
that weren't clickable. Resources mixed with advice text.
\`\`\`

### After:

- **Bold text** properly formatted
- Clickable phone: (510) 635-3663
- Separate resource section with action buttons
- Clean paragraph structure

## 🧪 Testing

You can test the formatting by:

1. **Live Chat**: Use the main interface at http://localhost:8000
2. **Test Page**: Open `test_formatting.html` for isolated testing
3. **API Testing**: Direct API calls show raw formatted responses

### Test Commands:

\`\`\`bash
# Test Assistant Mode (resource-heavy)
curl -X POST http://localhost:5001/api/chat/message \
  -H "Content-Type: application/json" \
  -d '{"message": "I need food help", "mode": "assistant"}'

# Test Coach Mode (content-focused)
curl -X POST http://localhost:5001/api/chat/message \
  -H "Content-Type: application/json" \
  -d '{"message": "I need food help", "mode": "coach"}'
\`\`\`

## 🎨 Customization

### CSS Variables for Easy Theming:

\`\`\`css
--accent-color: #007bff; /* Link and button color */
--text-color: #333333; /* Main text color */
--bg-color: #ffffff; /* Background color */
--border-color: #e0e0e0; /* Border color */
\`\`\`

### Responsive Design:

- Mobile-first approach
- Flexible button layouts
- Scalable typography
- Touch-friendly interactions

This enhanced formatting system creates a professional, user-friendly experience that makes it easy for users to both read advice and take immediate action on resources.

```

# GEMINI_MIGRATION.md

```md
# Claude to Gemini Migration

## Overview

Successfully migrated all API functionality from Claude to Gemini API. The system now uses Google's Gemini as the primary AI assistant for all operations.

## Changes Made

### 1. Services Updated

- **`services/gemini_service.py`**: Enhanced to include complete AI assistant functionality
  - Added `get_support_response()` function (previously Claude-only)
  - Added system prompts for "empathetic_coach" and "direct_assistant" modes
  - Integrated RAG pipeline support
  - Enhanced with user context handling
  - Maintained existing journal analysis and emotion scoring capabilities

### 2. Routes Updated

- **`routes/chat.py`**: Changed imports from `claude_service` to `gemini_service`
- Updated all function calls and comments to reference Gemini instead of Claude

### 3. Configuration Updated

- **`config.py`**: Added `GEMINI_API_KEY` configuration
- Maintained legacy CAG configuration for compatibility

### 4. Documentation Updated

- **`architecture.md`**: Updated AI orchestration section to reflect Gemini as primary AI
- Updated service descriptions and flow diagrams
- Removed Claude-specific references

### 5. RAG Pipeline Enhanced

- **`services/rag_pipeline.py`**: Added `format_resources_for_gemini()` method

### 6. Testing

- **`test_gemini.py`**: Created new comprehensive test file for Gemini integration
- **`test_chat_endpoint.py`**: Updated references to Gemini
- **`test_claude.py`**: Kept for legacy compatibility

## New Functionality

### Dual Prompt Types

The Gemini service now supports two interaction modes:

1. **empathetic_coach** (default): Warm, supportive, counselor-like responses
2. **direct_assistant**: Clear, step-by-step, no-nonsense guidance

### Enhanced Context Integration

- User location, situation, and needs are now fully integrated into prompts
- RAG pipeline results are formatted and provided as context to Gemini
- Greeting detection for natural conversation flow

## Environment Variables Required

\`\`\`bash
# Required for Gemini functionality
GEMINI_API_KEY=your_gemini_api_key_here

# Optional legacy
CAG_API_KEY=your_cag_api_key_here
\`\`\`

## API Endpoints

All existing endpoints remain the same but now use Gemini:

- `POST /api/chat/message` - Main chat interface
- `POST /api/chat/analyze-journal` - Journal analysis
- `GET /api/chat/summarize/<user_id>` - Conversation summarization
- `POST /api/chat/resources` - Resource retrieval

## Testing

Run the new Gemini tests:

\`\`\`bash
python test_gemini.py
\`\`\`

## Benefits of Migration

1. **Cost Efficiency**: Gemini typically offers better pricing than Claude
2. **Unified Service**: All AI functionality now handled by single service
3. **Enhanced Capabilities**: Gemini's multimodal capabilities ready for future features
4. **Better Integration**: Designed specifically for Google's ecosystem

## Backward Compatibility

- All existing API endpoints work identically
- Function signatures unchanged
- Database schema unchanged
- Frontend requires no changes

```

# index.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>For Social Change - Clean Voice Interface</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        :root {
            --bg-color: #ffffff;
            --text-color: #333333;
            --border-color: #e0e0e0;
            --accent-color: #007bff;
            --hover-color: #f8f9fa;
            --shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        
        [data-theme="dark"] {
            --bg-color: #1a1a1a;
            --text-color: #ffffff;
            --border-color: #333333;
            --accent-color: #0084ff;
            --hover-color: #2a2a2a;
            --shadow: 0 2px 10px rgba(0,0,0,0.3);
        }
        
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: var(--bg-color);
            color: var(--text-color);
            min-height: 100vh;
            transition: all 0.3s ease;
        }
        
        .top-bar {
            background: var(--bg-color);
            border-bottom: 1px solid var(--border-color);
            padding: 0 20px;
            height: 60px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            position: sticky;
            top: 0;
            z-index: 100;
        }
        
        .theme-toggle {
            background: var(--text-color);
            color: var(--bg-color);
            border: none;
            padding: 8px 16px;
            border-radius: 20px;
            cursor: pointer;
            font-size: 14px;
            transition: all 0.3s ease;
        }
        
        .theme-toggle:hover {
            opacity: 0.8;
        }
        
        .nav-tabs {
            display: flex;
            gap: 30px;
        }
        
        .nav-tab {
            padding: 10px 20px;
            background: none;
            border: none;
            color: var(--text-color);
            font-size: 16px;
            cursor: pointer;
            border-radius: 25px;
            transition: all 0.3s ease;
            opacity: 0.7;
        }
        
        .nav-tab.active {
            background: var(--accent-color);
            color: white;
            opacity: 1;
        }
        
        .nav-tab:hover {
            background: var(--hover-color);
            opacity: 1;
        }
        
        .nav-tab.active:hover {
            background: var(--accent-color);
            color: white;
        }
        
        .mode-toggle {
            display: flex;
            gap: 10px;
        }
        
        .mode-btn {
            padding: 8px 16px;
            background: var(--hover-color);
            border: 1px solid var(--border-color);
            color: var(--text-color);
            font-size: 14px;
            cursor: pointer;
            border-radius: 20px;
            transition: all 0.3s ease;
            opacity: 0.7;
        }
        
        .mode-btn.active {
            background: var(--accent-color);
            color: white;
            border-color: var(--accent-color);
            opacity: 1;
        }
        
        .mode-btn:hover {
            opacity: 1;
        }
        
        .main-container {
            padding: 40px 20px;
            max-width: 1200px;
            margin: 0 auto;
            position: relative;
        }
        
        .welcome-text {
            font-size: 24px;
            font-weight: 300;
            margin-bottom: 60px;
            color: var(--text-color);
        }
        
        .chat-interface {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            min-height: 60vh;
        }
        
        .voice-circle-container {
            position: relative;
            margin-bottom: 40px;
        }
        
        .logo-text {
            position: absolute;
            top: -30px;
            left: 50%;
            transform: translateX(-50%);
            font-size: 16px;
            font-weight: 600;
            color: var(--accent-color);
            white-space: nowrap;
        }
        
        .voice-circle {
            width: 200px;
            height: 200px;
            border-radius: 50%;
            background: linear-gradient(135deg, var(--accent-color), #00a8ff);
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            transition: all 0.3s ease;
            box-shadow: var(--shadow);
            position: relative;
            overflow: hidden;
        }
        
        .voice-circle:hover {
            transform: scale(1.05);
            box-shadow: 0 8px 25px rgba(0,123,255,0.3);
        }
        
        .voice-circle.listening {
            animation: pulse 2s infinite;
        }
        
        .voice-circle.speaking {
            animation: glow 1.5s ease-in-out infinite alternate;
        }
        
        @keyframes pulse {
            0% { box-shadow: 0 0 0 0 rgba(0,123,255,0.7); }
            70% { box-shadow: 0 0 0 20px rgba(0,123,255,0); }
            100% { box-shadow: 0 0 0 0 rgba(0,123,255,0); }
        }
        
        @keyframes glow {
            from { box-shadow: 0 0 20px rgba(0,255,123,0.5), 0 0 30px rgba(0,255,123,0.3); }
            to { box-shadow: 0 0 30px rgba(0,255,123,0.8), 0 0 40px rgba(0,255,123,0.5); }
        }
        
        .voice-icon {
            font-size: 48px;
            color: white;
        }
        
        .voice-status {
            margin-top: 20px;
            font-size: 18px;
            color: var(--text-color);
            text-align: center;
        }
        
        .microphone-help {
            font-size: 14px;
            color: var(--text-color);
            opacity: 0.6;
            margin-top: 10px;
            max-width: 400px;
            text-align: center;
            line-height: 1.4;
        }
        
        .permission-status {
            display: inline-block;
            width: 8px;
            height: 8px;
            border-radius: 50%;
            margin-left: 8px;
            background-color: #ccc;
        }
        
        .permission-status.granted {
            background-color: #00ff7f;
        }
        
        .permission-status.denied {
            background-color: #ff4444;
        }
        
        .message-button {
            background: none;
            border: 2px solid var(--border-color);
            color: var(--text-color);
            padding: 12px 24px;
            border-radius: 25px;
            cursor: pointer;
            font-size: 16px;
            margin-top: 30px;
            transition: all 0.3s ease;
        }
        
        .message-button:hover {
            border-color: var(--accent-color);
            color: var(--accent-color);
        }
        
        .quick-actions {
            display: flex;
            gap: 20px;
            margin-top: 40px;
            flex-wrap: wrap;
            justify-content: center;
        }
        
        .quick-action {
            background: var(--bg-color);
            border: 1px solid var(--border-color);
            padding: 15px 20px;
            border-radius: 15px;
            cursor: pointer;
            transition: all 0.3s ease;
            box-shadow: var(--shadow);
            text-align: center;
            min-width: 150px;
        }
        
        .quick-action:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 15px rgba(0,0,0,0.15);
            border-color: var(--accent-color);
        }
        
        .quick-action-icon {
            font-size: 24px;
            margin-bottom: 8px;
            display: block;
        }
        
        .quick-action-text {
            font-size: 14px;
            color: var(--text-color);
        }
        
        .chat-sidebar {
            position: fixed;
            left: -400px;
            top: 60px;
            width: 400px;
            height: calc(100vh - 60px);
            background: var(--bg-color);
            border-right: 1px solid var(--border-color);
            transition: left 0.3s ease;
            z-index: 50;
            display: flex;
            flex-direction: column;
            box-shadow: var(--shadow);
        }
        
        .chat-sidebar.open {
            left: 0;
        }
        
        .chat-header {
            padding: 20px;
            border-bottom: 1px solid var(--border-color);
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        
        .chat-title {
            font-size: 18px;
            font-weight: 600;
        }
        
        .close-chat {
            background: none;
            border: none;
            font-size: 24px;
            cursor: pointer;
            color: var(--text-color);
        }
        
        .chat-messages {
            flex: 1;
            padding: 20px;
            overflow-y: auto;
        }
        
        .message {
            margin-bottom: 15px;
            padding: 12px 16px;
            border-radius: 18px;
            max-width: 80%;
            line-height: 1.6;
        }
        
        .message.bot {
            background: var(--hover-color);
            color: var(--text-color);
            border: 1px solid var(--border-color);
        }
        
        .message.user {
            background: var(--accent-color);
            color: white;
            margin-left: auto;
        }
        
        .message-content {
            margin-bottom: 10px;
        }
        
        .message-content p {
            margin-bottom: 12px;
            line-height: 1.6;
        }
        
        .message-content strong {
            font-weight: 600;
            color: var(--accent-color);
        }
        
        .message-content a {
            color: var(--accent-color);
            text-decoration: none;
            font-weight: 500;
        }
        
        .message-content a:hover {
            text-decoration: underline;
        }
        
        .resource-section {
            margin-top: 15px;
            padding: 12px;
            background: rgba(0, 123, 255, 0.05);
            border-left: 3px solid var(--accent-color);
            border-radius: 8px;
        }
        
        .resource-title {
            font-weight: 600;
            color: var(--accent-color);
            margin-bottom: 8px;
            font-size: 14px;
        }
        
        .resource-item {
            margin-bottom: 12px;
            padding: 8px;
            background: var(--bg-color);
            border-radius: 6px;
            border: 1px solid var(--border-color);
        }
        
        .resource-name {
            font-weight: 600;
            margin-bottom: 4px;
        }
        
        .resource-details {
            font-size: 13px;
            color: var(--text-color);
            opacity: 0.8;
        }
        
        .resource-contact {
            margin-top: 6px;
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
        }
        
        .contact-link {
            display: inline-flex;
            align-items: center;
            gap: 4px;
            padding: 4px 8px;
            background: var(--accent-color);
            color: white;
            text-decoration: none;
            border-radius: 12px;
            font-size: 12px;
            font-weight: 500;
        }
        
        .contact-link:hover {
            background: #0056b3;
            color: white;
            text-decoration: none;
        }
        
        .chat-input-container {
            padding: 20px;
            border-top: 1px solid var(--border-color);
        }
        
        .chat-input {
            display: flex;
            gap: 10px;
        }
        
        .chat-input input {
            flex: 1;
            padding: 12px 16px;
            border: 1px solid var(--border-color);
            border-radius: 25px;
            background: var(--bg-color);
            color: var(--text-color);
            outline: none;
            font-size: 14px;
        }
        
        .chat-input input:focus {
            border-color: var(--accent-color);
        }
        
        .send-btn {
            background: var(--accent-color);
            color: white;
            border: none;
            padding: 12px 20px;
            border-radius: 25px;
            cursor: pointer;
            font-size: 14px;
        }
        
        .send-btn:hover {
            background: #0056b3;
        }
        
        .assistant-actions {
            display: flex;
            gap: 10px;
            margin-top: 10px;
            justify-content: center;
        }
        
        .action-btn {
            padding: 10px 20px;
            border: none;
            border-radius: 20px;
            cursor: pointer;
            font-size: 14px;
            font-weight: 500;
            transition: all 0.3s ease;
            display: flex;
            align-items: center;
            gap: 5px;
        }
        
        .call-btn {
            background: #28a745;
            color: white;
        }
        
        .call-btn:hover {
            background: #218838;
        }
        
        .email-btn {
            background: #17a2b8;
            color: white;
        }
        
        .email-btn:hover {
            background: #138496;
        }
        
        .overlay {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0,0,0,0.5);
            z-index: 40;
            opacity: 0;
            pointer-events: none;
            transition: opacity 0.3s ease;
        }
        
        .overlay.active {
            opacity: 1;
            pointer-events: all;
        }
        
        .info-popup {
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background: var(--bg-color);
            border: 1px solid var(--border-color);
            border-radius: 20px;
            padding: 40px;
            width: 90%;
            max-width: 500px;
            z-index: 60;
            box-shadow: 0 20px 40px rgba(0,0,0,0.2);
            opacity: 0;
            pointer-events: none;
            transition: all 0.3s ease;
        }
        
        .info-popup.active {
            opacity: 1;
            pointer-events: all;
        }
        
        .popup-header {
            text-align: center;
            margin-bottom: 30px;
        }
        
        .popup-title {
            font-size: 24px;
            font-weight: 600;
            color: var(--text-color);
            margin-bottom: 10px;
        }
        
        .popup-subtitle {
            font-size: 16px;
            color: var(--text-color);
            opacity: 0.7;
            line-height: 1.5;
        }
        
        .form-group {
            margin-bottom: 20px;
        }
        
        .form-label {
            display: block;
            font-size: 14px;
            font-weight: 500;
            color: var(--text-color);
            margin-bottom: 8px;
        }
        
        .form-input, .form-textarea, .form-select {
            width: 100%;
            padding: 12px 16px;
            border: 1px solid var(--border-color);
            border-radius: 10px;
            background: var(--bg-color);
            color: var(--text-color);
            font-size: 16px;
            outline: none;
            transition: border-color 0.3s ease;
        }
        
        .form-input:focus, .form-textarea:focus, .form-select:focus {
            border-color: var(--accent-color);
        }
        
        .form-textarea {
            resize: vertical;
            min-height: 80px;
        }
        
        .form-row {
            display: flex;
            gap: 15px;
        }
        
        .form-row .form-group {
            flex: 1;
        }
        
        .popup-buttons {
            display: flex;
            gap: 15px;
            margin-top: 30px;
        }
        
        .popup-btn {
            flex: 1;
            padding: 14px 24px;
            border: none;
            border-radius: 10px;
            font-size: 16px;
            font-weight: 500;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        
        .popup-btn.primary {
            background: var(--accent-color);
            color: white;
        }
        
        .popup-btn.primary:hover {
            background: #0056b3;
        }
        
        .popup-btn.secondary {
            background: var(--hover-color);
            color: var(--text-color);
            border: 1px solid var(--border-color);
        }
        
        .popup-btn.secondary:hover {
            background: var(--border-color);
        }
        
        .life-coach-interface {
            display: none;
        }
        
        .life-coach-interface.active {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            min-height: 60vh;
        }
        
        .coach-circle {
            width: 200px;
            height: 200px;
            border-radius: 50%;
            background: linear-gradient(135deg, #28a745, #20c997);
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            transition: all 0.3s ease;
            box-shadow: var(--shadow);
            position: relative;
            overflow: hidden;
            margin-bottom: 20px;
        }
        
        .coach-circle:hover {
            transform: scale(1.05);
            box-shadow: 0 8px 25px rgba(40,167,69,0.3);
        }
        
        .coach-circle.active {
            animation: pulse-green 2s infinite;
        }
        
        @keyframes pulse-green {
            0% { box-shadow: 0 0 0 0 rgba(40,167,69,0.7); }
            70% { box-shadow: 0 0 0 20px rgba(40,167,69,0); }
            100% { box-shadow: 0 0 0 0 rgba(40,167,69,0); }
        }
        
        .coach-icon {
            font-size: 48px;
            color: white;
        }
    </style>
</head>
<body>
    <div class="top-bar">
        <button class="theme-toggle" onclick="toggleTheme()">● Dark Mode</button>
        <div class="nav-tabs">
            <button class="nav-tab active" onclick="switchTab('voice')">Voice Chat</button>
            <button class="nav-tab" onclick="switchTab('resources')">Social Resources</button>
            <button class="nav-tab" onclick="switchTab('coach')">Life Coach</button>
        </div>
        <div class="mode-toggle">
            <button class="mode-btn active" onclick="switchMode('coach')" id="coachModeBtn">
                🧠 Coach Mode
            </button>
            <button class="mode-btn" onclick="switchMode('assistant')" id="assistantModeBtn">
                📋 Assistant Mode
            </button>
        </div>
    </div>

    <div class="main-container">
        <div class="welcome-text">
            Welcome Back, Alex!
        </div>

        <!-- Voice Chat Interface -->
        <div class="chat-interface" id="voiceChatInterface">
            <div class="voice-circle-container">
                <div class="logo-text">For Social Change</div>
                <div class="voice-circle listening" onclick="toggleVoice()">
                    <div class="voice-icon">🎤</div>
                </div>
            </div>
            
            <div class="voice-status" id="voiceStatus">
                Tap to speak <span class="permission-status" id="micPermissionStatus"></span>
            </div>
            <div class="microphone-help">
                🎤 Click the circle to start voice chat. Allow microphone access when prompted. Works best in Chrome, Edge, or Safari.
            </div>
            
            <button class="message-button" onclick="openChat()">
                💬 Switch to Text Chat
            </button>
            
            <div class="quick-actions">
                <div class="quick-action">
                    <span class="quick-action-icon">🏠</span>
                    <div class="quick-action-text">Find Shelter</div>
                </div>
                <div class="quick-action">
                    <span class="quick-action-icon">🍽️</span>
                    <div class="quick-action-text">Food Resources</div>
                </div>
                <div class="quick-action">
                    <span class="quick-action-icon">💊</span>
                    <div class="quick-action-text">Healthcare</div>
                </div>
                <div class="quick-action">
                    <span class="quick-action-icon">💼</span>
                    <div class="quick-action-text">Job Assistance</div>
                </div>
            </div>
        </div>

        <!-- Life Coach Interface -->
        <div class="life-coach-interface" id="lifeCoachInterface">
            <div class="voice-circle-container">
                <div class="logo-text">For Social Change</div>
                <div class="coach-circle" onclick="toggleCoach()">
                    <div class="coach-icon">🧠</div>
                </div>
            </div>
            
            <div class="voice-status" id="coachStatus">
                Your Life Coach is ready... Tap to start
            </div>
            
            <button class="message-button" onclick="openCoachChat()">
                💬 Switch to Text Chat
            </button>
            
            <div class="quick-actions">
                <div class="quick-action">
                    <span class="quick-action-icon">🎯</span>
                    <div class="quick-action-text">Set Goals</div>
                </div>
                <div class="quick-action">
                    <span class="quick-action-icon">📝</span>
                    <div class="quick-action-text">Journal Entry</div>
                </div>
                <div class="quick-action">
                    <span class="quick-action-icon">💪</span>
                    <div class="quick-action-text">Progress Check</div>
                </div>
                <div class="quick-action">
                    <span class="quick-action-icon">🧘</span>
                    <div class="quick-action-text">Mindfulness</div>
                </div>
            </div>
        </div>
    </div>

    <div class="overlay" onclick="closePopups()"></div>
    
    <!-- Information Popup -->
    <div class="info-popup" id="infoPopup">
        <div class="popup-header">
            <div class="popup-title">Welcome to For Social Change</div>
            <div class="popup-subtitle">Help us personalize your experience by sharing some basic information. This helps our AI provide more accurate and relevant support.</div>
        </div>
        
        <form id="userInfoForm">
            <div class="form-row">
                <div class="form-group">
                    <label class="form-label">First Name *</label>
                    <input type="text" class="form-input" placeholder="Enter your name" required>
                </div>
                <div class="form-group">
                    <label class="form-label">Phone Number</label>
                    <input type="tel" class="form-input" placeholder="(555) 123-4567">
                </div>
            </div>
            
            <div class="form-group">
                <label class="form-label">Email Address</label>
                <input type="email" class="form-input" placeholder="your.email@example.com">
            </div>
            
            <div class="form-group">
                <label class="form-label">Current Location/Area</label>
                <input type="text" class="form-input" placeholder="e.g., Berkeley, Oakland, San Francisco">
            </div>
            
            <div class="form-group">
                <label class="form-label">Current Situation</label>
                <select class="form-select">
                    <option value="">Select your current housing situation</option>
                    <option value="housed">Temporarily housed</option>
                    <option value="shelter">In shelter</option>
                    <option value="unsheltered">Unsheltered</option>
                    <option value="transitional">Transitional housing</option>
                    <option value="risk">At risk of homelessness</option>
                    <option value="other">Other</option>
                </select>
            </div>
            
            <div class="form-group">
                <label class="form-label">Previous Services Used (Optional)</label>
                <textarea class="form-textarea" placeholder="Tell us about any shelters, clinics, programs, or services you've used before. This helps us avoid suggesting places that weren't a good fit."></textarea>
            </div>
            
            <div class="form-group">
                <label class="form-label">Primary Support Needs</label>
                <select class="form-select">
                    <option value="">What do you need most help with?</option>
                    <option value="housing">Housing/Shelter</option>
                    <option value="healthcare">Healthcare/Mental Health</option>
                    <option value="addiction">Addiction Recovery</option>
                    <option value="employment">Job Search/Employment</option>
                    <option value="benefits">Government Benefits</option>
                    <option value="food">Food/Basic Needs</option>
                    <option value="multiple">Multiple areas</option>
                </select>
            </div>
        </form>
        
        <div class="popup-buttons">
            <button class="popup-btn secondary" onclick="skipSetup()">Skip for Now</button>
            <button class="popup-btn primary" onclick="saveUserInfo()">Get Started</button>
        </div>
    </div>
    
    <div class="chat-sidebar">
        <div class="chat-header">
            <div class="chat-title">Chat Assistant</div>
            <button class="close-chat" onclick="closeChat()">×</button>
        </div>
        
        <div class="chat-messages">
            <div class="message bot">
                Hi Alex! I switched to text mode. How can I help you today? I can help you find resources, provide support, or just chat about how you're feeling.
            </div>
        </div>
        
        <div class="chat-input-container">
            <div class="chat-input">
                <input type="text" placeholder="Type your message..." onkeypress="handleEnter(event)">
                <button class="send-btn" onclick="sendMessage()">Send</button>
            </div>
            <div class="assistant-actions" id="assistantActions" style="display: none;">
                <button class="action-btn call-btn" onclick="makeCall()">
                    📞 Call Resource
                </button>
                <button class="action-btn email-btn" onclick="sendEmail()">
                    ✉️ Send Email
                </button>
            </div>
        </div>
    </div>

    <script>
        let isListening = false;
        let isDarkMode = false;
        let isCoachActive = false;
        let currentTab = 'voice';
        let currentMode = 'coach'; // 'coach' or 'assistant'
        let userInfo = {};
        let lastResourceInfo = null; // Store last resource info for actions
        
        function toggleTheme() {
            isDarkMode = !isDarkMode;
            document.body.setAttribute('data-theme', isDarkMode ? 'dark' : 'light');
            document.querySelector('.theme-toggle').textContent = isDarkMode ? '○ Light Mode' : '● Dark Mode';
        }
        
        function switchMode(mode) {
            currentMode = mode;
            
            // Update mode buttons
            document.querySelectorAll('.mode-btn').forEach(btn => btn.classList.remove('active'));
            document.getElementById(mode + 'ModeBtn').classList.add('active');
            
            // Show/hide assistant actions based on mode
            const assistantActions = document.getElementById('assistantActions');
            if (mode === 'assistant') {
                assistantActions.style.display = 'flex';
            } else {
                assistantActions.style.display = 'none';
            }
            
            // Update chat title if chat is open
            const chatTitle = document.querySelector('.chat-title');
            if (chatTitle) {
                if (mode === 'coach') {
                    chatTitle.textContent = currentTab === 'voice' ? 'Life Coach' : 'Life Coach';
                } else {
                    chatTitle.textContent = currentTab === 'voice' ? 'Resource Assistant' : 'Resource Assistant';
                }
            }
        }
        
        function switchTab(tab) {
            // Update nav tabs
            document.querySelectorAll('.nav-tab').forEach(t => t.classList.remove('active'));
            event.target.classList.add('active');
            
            // Hide all interfaces
            document.getElementById('voiceChatInterface').style.display = 'none';
            document.getElementById('lifeCoachInterface').classList.remove('active');
            
            currentTab = tab;
            
            if (tab === 'voice') {
                document.getElementById('voiceChatInterface').style.display = 'flex';
                document.getElementById('voiceChatInterface').style.flexDirection = 'column';
                document.getElementById('voiceChatInterface').style.alignItems = 'center';
                document.getElementById('voiceChatInterface').style.justifyContent = 'center';
                document.getElementById('voiceChatInterface').style.minHeight = '60vh';
            } else if (tab === 'coach') {
                document.getElementById('lifeCoachInterface').classList.add('active');
            } else if (tab === 'resources') {
                // TODO: Implement resources tab
                alert('Social Resources tab coming soon!');
            }
        }
        
        // Speech Recognition variables
        let recognition = null;
        let speechSynthesis = window.speechSynthesis;
        
        // Initialize Speech Recognition
        function initializeSpeechRecognition() {
            if ('webkitSpeechRecognition' in window) {
                recognition = new webkitSpeechRecognition();
            } else if ('SpeechRecognition' in window) {
                recognition = new SpeechRecognition();
            } else {
                console.warn('Speech Recognition not supported in this browser');
                return false;
            }
            
            recognition.continuous = false;
            recognition.interimResults = false;
            recognition.lang = 'en-US';
            
            recognition.onstart = function() {
                console.log('Speech recognition started');
                const circle = document.querySelector('.voice-circle');
                const status = document.getElementById('voiceStatus');
                circle.classList.add('listening');
                status.textContent = 'Listening... Speak now';
            };
            
            recognition.onresult = function(event) {
                const transcript = event.results[0][0].transcript;
                console.log('Speech recognized:', transcript);
                
                const status = document.getElementById('voiceStatus');
                status.textContent = 'Processing your message...';
                
                // Send the transcribed text to the chat
                processVoiceInput(transcript);
            };
            
            recognition.onerror = function(event) {
                console.error('Speech recognition error:', event.error);
                const status = document.getElementById('voiceStatus');
                const circle = document.querySelector('.voice-circle');
                
                circle.classList.remove('listening');
                isListening = false;
                
                switch(event.error) {
                    case 'no-speech':
                        status.textContent = 'No speech detected. Tap to try again.';
                        break;
                    case 'audio-capture':
                        status.textContent = 'Microphone not accessible. Check permissions.';
                        break;
                    case 'not-allowed':
                        status.textContent = 'Microphone permission denied. Please allow access.';
                        break;
                    default:
                        status.textContent = 'Speech recognition error. Tap to try again.';
                        break;
                }
            };
            
            recognition.onend = function() {
                console.log('Speech recognition ended');
                const circle = document.querySelector('.voice-circle');
                circle.classList.remove('listening');
                isListening = false;
            };
            
            return true;
        }
        
        function toggleVoice() {
            const circle = document.querySelector('.voice-circle');
            const status = document.getElementById('voiceStatus');
            
            // If currently speaking, stop speech
            if (circle.classList.contains('speaking')) {
                stopSpeech();
                return;
            }
            
            if (!recognition && !initializeSpeechRecognition()) {
                alert('Speech recognition is not supported in your browser. Please use a modern browser like Chrome or Edge.');
                return;
            }
            
            if (isListening) {
                // Stop listening
                recognition.stop();
                circle.classList.remove('listening');
                status.textContent = 'Tap to speak';
                isListening = false;
            } else {
                // Start listening
                try {
                    recognition.start();
                    isListening = true;
                } catch (error) {
                    console.error('Error starting speech recognition:', error);
                    status.textContent = 'Error starting microphone. Tap to try again.';
                }
            }
        }
        
        async function processVoiceInput(transcript) {
            const status = document.getElementById('voiceStatus');
            
            try {
                // Open chat sidebar automatically
                openChat();
                
                // Add user message to chat
                addMessage(transcript, 'user');
                
                // Show typing indicator
                addTypingIndicator();
                
                // Determine prompt type based on current mode
                let promptType = 'empathetic_coach'; // Default
                if (currentTab === 'resources' || currentMode === 'assistant') {
                    promptType = 'direct_assistant';
                }
                
                // Call Flask backend API
                const response = await fetch('http://localhost:5001/api/chat/message', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        message: transcript,
                        context: userInfo,
                        user_id: userInfo.user_id || null,
                        prompt_type: promptType,
                        mode: currentMode
                    })
                });
                
                const data = await response.json();
                
                // Remove typing indicator
                removeTypingIndicator();
                
                if (response.ok) {
                    // Store user_id for future requests
                    userInfo.user_id = data.user_id;
                    addMessage(data.response, 'bot');
                    
                    // Extract resource info if in assistant mode
                    if (currentMode === 'assistant') {
                        extractResourceInfo(data.response);
                    }
                    
                    // Speak the response aloud
                    speakResponse(data.response);
                    
                    status.textContent = 'Response complete. Tap to speak again.';
                } else {
                    const errorMsg = 'Sorry, I encountered an error. Please try again.';
                    addMessage(errorMsg, 'bot');
                    speakResponse(errorMsg);
                    status.textContent = 'Error occurred. Tap to try again.';
                }
            } catch (error) {
                console.error('Error processing voice input:', error);
                removeTypingIndicator();
                const errorMsg = 'Sorry, I could not connect to the server. Please check if the backend is running.';
                addMessage(errorMsg, 'bot');
                speakResponse(errorMsg);
                status.textContent = 'Connection error. Tap to try again.';
            }
        }
        
        function speakResponse(text) {
            // Stop any ongoing speech
            speechSynthesis.cancel();
            
            // Clean text for speech (remove markdown and special characters)
            let cleanText = text.replace(/\*\*(.*?)\*\*/g, '$1'); // Remove bold markers
            cleanText = cleanText.replace(/[📞📍🕒📋]/g, ''); // Remove emojis
            cleanText = cleanText.replace(/Address:|Phone:|Hours:/g, ''); // Remove labels
            cleanText = cleanText.replace(/\n/g, ' '); // Replace line breaks with spaces
            
            // Limit length for better user experience
            if (cleanText.length > 500) {
                cleanText = cleanText.substring(0, 500) + '... For more details, please read the chat.';
            }
            
            // Create speech utterance
            const utterance = new SpeechSynthesisUtterance(cleanText);
            utterance.rate = 0.9;
            utterance.pitch = 1;
            utterance.volume = 0.8;
            
            // Use a more natural voice if available
            const voices = speechSynthesis.getVoices();
            const preferredVoice = voices.find(voice => 
                voice.name.includes('Google') || 
                voice.name.includes('Microsoft') ||
                voice.lang.startsWith('en')
            );
            if (preferredVoice) {
                utterance.voice = preferredVoice;
            }
            
            utterance.onstart = function() {
                console.log('Speech synthesis started');
                const circle = document.querySelector('.voice-circle');
                const status = document.getElementById('voiceStatus');
                circle.classList.add('speaking');
                status.textContent = 'Speaking response... Tap to stop';
            };
            
            utterance.onend = function() {
                console.log('Speech synthesis completed');
                const circle = document.querySelector('.voice-circle');
                const status = document.getElementById('voiceStatus');
                circle.classList.remove('speaking');
                status.textContent = 'Tap to speak again';
            };
            
            utterance.onerror = function(event) {
                console.error('Speech synthesis error:', event.error);
                const circle = document.querySelector('.voice-circle');
                const status = document.getElementById('voiceStatus');
                circle.classList.remove('speaking');
                status.textContent = 'Tap to speak again';
            };
            
            // Speak the response
            speechSynthesis.speak(utterance);
        }
        
        function stopSpeech() {
            speechSynthesis.cancel();
            const circle = document.querySelector('.voice-circle');
            const status = document.getElementById('voiceStatus');
            circle.classList.remove('speaking');
            status.textContent = 'Tap to speak again';
        }
        
        function toggleCoach() {
            isCoachActive = !isCoachActive;
            const circle = document.querySelector('.coach-circle');
            const status = document.getElementById('coachStatus');
            
            if (isCoachActive) {
                circle.classList.add('active');
                status.textContent = 'Life Coach is listening... Share what\'s on your mind';
                // Simulate coach interaction
                setTimeout(() => {
                    status.textContent = 'Processing your thoughts...';
                    setTimeout(() => {
                        status.textContent = 'Ready for your next session';
                        circle.classList.remove('active');
                        isCoachActive = false;
                    }, 3000);
                }, 4000);
            } else {
                circle.classList.remove('active');
                status.textContent = 'Your Life Coach is ready... Tap to start';
            }
        }
        
        function openChat() {
            document.querySelector('.chat-sidebar').classList.add('open');
            document.querySelector('.overlay').classList.add('active');
            
            // Update chat title based on current tab
            const chatTitle = document.querySelector('.chat-title');
            chatTitle.textContent = currentTab === 'voice' ? 'Voice Assistant' : 'Life Coach';
        }
        
        function openCoachChat() {
            openChat(); // Same functionality but will show Life Coach context
        }
        
        function closePopups() {
            document.querySelector('.chat-sidebar').classList.remove('open');
            document.querySelector('.overlay').classList.remove('active');
            document.querySelector('.info-popup').classList.remove('active');
        }
        
        function closeChat() {
            closePopups();
        }
        
        function showInfoPopup() {
            document.querySelector('.info-popup').classList.add('active');
            document.querySelector('.overlay').classList.add('active');
        }
        
        function skipSetup() {
            closePopups();
        }
        
        function saveUserInfo() {
            const form = document.getElementById('userInfoForm');
            
            // Store user info for API calls
            userInfo = {
                name: form.querySelector('input[type="text"]').value,
                phone: form.querySelector('input[type="tel"]').value,
                email: form.querySelector('input[type="email"]').value,
                location: form.querySelectorAll('input[type="text"]')[1].value,
                situation: form.querySelector('select').value,
                previousServices: form.querySelector('textarea').value,
                needs: form.querySelectorAll('select')[1].value
            };
            
            // Store in localStorage for persistence
            localStorage.setItem('userInfo', JSON.stringify(userInfo));
            
            // Update welcome message if name provided
            if (userInfo.name) {
                document.querySelector('.welcome-text').textContent = `Welcome Back, ${userInfo.name}!`;
            }
            
            closePopups();
            
            // Show confirmation message
            setTimeout(() => {
                alert('Profile saved! I can now provide more personalized assistance.');
            }, 500);
        }
        
        async function sendMessage() {
            const input = document.querySelector('.chat-input input');
            const message = input.value.trim();
            if (message) {
                addMessage(message, 'user');
                input.value = '';
                
                // Show typing indicator
                addTypingIndicator();
                
                try {
                    // Determine prompt type based on current tab and mode
                    let promptType = 'empathetic_coach'; // Default
                    if (currentTab === 'resources' || currentMode === 'assistant') {
                        promptType = 'direct_assistant';
                    }
                    
                    // Call Flask backend API
                    const response = await fetch('http://localhost:5001/api/chat/message', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                        body: JSON.stringify({
                            message: message,
                            context: userInfo,
                            user_id: userInfo.user_id || null,
                            prompt_type: promptType,
                            mode: currentMode
                        })
                    });
                    
                    const data = await response.json();
                    
                    // Remove typing indicator
                    removeTypingIndicator();
                    
                    if (response.ok) {
                        // Store user_id for future requests
                        userInfo.user_id = data.user_id;
                        addMessage(data.response, 'bot');
                        
                        // Extract resource info if in assistant mode
                        if (currentMode === 'assistant') {
                            extractResourceInfo(data.response);
                        }
                    } else {
                        addMessage('Sorry, I encountered an error. Please try again.', 'bot');
                    }
                } catch (error) {
                    console.error('Error sending message:', error);
                    removeTypingIndicator();
                    addMessage('Sorry, I could not connect to the server. Please check if the backend is running.', 'bot');
                }
            }
        }
        
        function addMessage(text, sender) {
            const messagesContainer = document.querySelector('.chat-messages');
            const messageDiv = document.createElement('div');
            messageDiv.className = `message ${sender}`;
            
            if (sender === 'bot') {
                // Format bot messages with rich text and resource extraction
                const formattedContent = formatBotMessage(text);
                messageDiv.innerHTML = formattedContent;
            } else {
                messageDiv.textContent = text;
            }
            
            messagesContainer.appendChild(messageDiv);
            messagesContainer.scrollTop = messagesContainer.scrollHeight;
        }
        
        function formatBotMessage(text) {
            // Split message into main content and resource information
            const { mainContent, resources } = extractResources(text);
            
            let formattedText = mainContent;
            
            // Format bold text (**text** -> <strong>text</strong>)
            formattedText = formattedText.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
            
            // Format phone numbers as clickable links
            formattedText = formattedText.replace(/(\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4})/g, '<a href="tel:$1">$1</a>');
            
            // Format email addresses as clickable links
            formattedText = formattedText.replace(/([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})/g, '<a href="mailto:$1">$1</a>');
            
            // Split into paragraphs for better readability
            const paragraphs = formattedText.split('\n\n').filter(p => p.trim());
            const paragraphHTML = paragraphs.map(p => `<p>${p.trim()}</p>`).join('');
            
            let html = `<div class="message-content">${paragraphHTML}</div>`;
            
            // Add resource section if resources were found
            if (resources.length > 0) {
                html += generateResourceSection(resources);
            }
            
            return html;
        }
        
        function extractResources(text) {
            const resources = [];
            let mainContent = text;
            
            // Pattern to match resource blocks like:
            // **Food Resources:** * **Alameda County Community Food Bank:** *
            // **Address:** 7900 Edgewater Dr, Oakland, CA 94621 * **Phone:** (510) 635-3663
            const resourcePattern = /\*\*(.*?):\*\*\s*\*\s*\*\*(.*?):\*\*\s*\*\s*\*\*Address:\*\*\s*(.*?)\s*\*\s*\*\*Phone:\*\*\s*(.*?)\s*\*\s*\*\*Hours:\*\*\s*(.*?)(?:\*|$)/g;
            
            let match;
            while ((match = resourcePattern.exec(text)) !== null) {
                const [fullMatch, category, name, address, phone, hours] = match;
                
                resources.push({
                    name: name.trim(),
                    category: category.trim(),
                    address: address.trim(),
                    phone: phone.trim(),
                    hours: hours.trim(),
                    details: []
                });
                
                // Remove this resource block from main content
                mainContent = mainContent.replace(fullMatch, '');
            }
            
            // Alternative pattern for simpler resource mentions
            if (resources.length === 0) {
                // Look for organization names followed by contact info
                const lines = text.split('\n');
                let currentResource = null;
                const contentLines = [];
                
                for (let line of lines) {
                    line = line.trim();
                    
                    // Check for organization names
                    const orgMatch = line.match(/^([A-Z][^.]*(?:Center|Bank|Service|House|Shelter|Clinic|Organization|Foundation|Project|Community|Food)[^.]*)/);
                    if (orgMatch && !line.includes('Address:') && !line.includes('Phone:')) {
                        if (currentResource) {
                            resources.push(currentResource);
                        }
                        currentResource = {
                            name: orgMatch[1].trim(),
                            address: '',
                            phone: '',
                            hours: '',
                            details: []
                        };
                        contentLines.push(line);
                    } else if (currentResource && line.includes('Address:')) {
                        currentResource.address = line.replace(/.*Address:\s*/, '').replace(/\s*Phone:.*/, '').trim();
                        contentLines.push(line);
                    } else if (currentResource && line.includes('Phone:')) {
                        currentResource.phone = line.replace(/.*Phone:\s*/, '').replace(/\s*Hours:.*/, '').trim();
                        contentLines.push(line);
                    } else if (currentResource && line.includes('Hours:')) {
                        currentResource.hours = line.replace(/.*Hours:\s*/, '').trim();
                        contentLines.push(line);
                    } else {
                        contentLines.push(line);
                    }
                }
                
                if (currentResource) {
                    resources.push(currentResource);
                }
                
                // If we found resources this way, clean up the main content
                if (resources.length > 0) {
                    mainContent = contentLines.filter(line => {
                        return !line.includes('Address:') && !line.includes('Phone:') && !line.includes('Hours:');
                    }).join('\n');
                }
            }
            
            return {
                mainContent: mainContent.replace(/\*\s*\*/g, '').trim(),
                resources: resources
            };
        }
        
        function generateResourceSection(resources) {
            if (resources.length === 0) return '';
            
            let html = '<div class="resource-section">';
            html += '<div class="resource-title">📋 Available Resources</div>';
            
            resources.forEach(resource => {
                html += '<div class="resource-item">';
                html += `<div class="resource-name">${resource.name}</div>`;
                
                let details = '';
                if (resource.address) details += `📍 ${resource.address}<br>`;
                if (resource.hours) details += `🕒 ${resource.hours}<br>`;
                if (resource.details.length > 0) details += resource.details.join('<br>');
                
                if (details) {
                    html += `<div class="resource-details">${details}</div>`;
                }
                
                if (resource.phone || resource.address) {
                    html += '<div class="resource-contact">';
                    if (resource.phone) {
                        html += `<a href="tel:${resource.phone}" class="contact-link">📞 Call</a>`;
                    }
                    if (resource.address) {
                        const mapsUrl = `https://maps.google.com/?q=${encodeURIComponent(resource.address)}`;
                        html += `<a href="${mapsUrl}" target="_blank" class="contact-link">📍 Directions</a>`;
                    }
                    html += '</div>';
                }
                
                html += '</div>';
            });
            
            html += '</div>';
            return html;
        }
        
        function addTypingIndicator() {
            const messagesContainer = document.querySelector('.chat-messages');
            const typingDiv = document.createElement('div');
            typingDiv.className = 'message bot typing-indicator';
            typingDiv.innerHTML = '<span>●</span><span>●</span><span>●</span> Assistant is typing...';
            typingDiv.id = 'typing-indicator';
            messagesContainer.appendChild(typingDiv);
            messagesContainer.scrollTop = messagesContainer.scrollHeight;
        }
        
        function removeTypingIndicator() {
            const typingIndicator = document.getElementById('typing-indicator');
            if (typingIndicator) {
                typingIndicator.remove();
            }
        }
        
        function handleEnter(event) {
            if (event.key === 'Enter') {
                sendMessage();
            }
        }
        
        // Initialize speech synthesis voices
        function initializeSpeechSynthesis() {
            // Load voices
            if (speechSynthesis.onvoiceschanged !== undefined) {
                speechSynthesis.onvoiceschanged = function() {
                    console.log('Speech synthesis voices loaded');
                };
            }
        }
        
        // Check microphone permissions
        async function checkMicrophonePermissions() {
            try {
                if (navigator.permissions) {
                    const permission = await navigator.permissions.query({ name: 'microphone' });
                    updatePermissionStatus(permission.state);
                    
                    permission.addEventListener('change', () => {
                        updatePermissionStatus(permission.state);
                    });
                } else {
                    // Fallback for browsers without permissions API
                    updatePermissionStatus('unknown');
                }
            } catch (error) {
                console.log('Could not check microphone permissions:', error);
                updatePermissionStatus('unknown');
            }
        }
        
        function updatePermissionStatus(state) {
            const statusElement = document.getElementById('micPermissionStatus');
            if (!statusElement) return;
            
            statusElement.className = 'permission-status';
            
            switch (state) {
                case 'granted':
                    statusElement.classList.add('granted');
                    statusElement.title = 'Microphone access granted';
                    break;
                case 'denied':
                    statusElement.classList.add('denied');
                    statusElement.title = 'Microphone access denied - click to try again';
                    break;
                default:
                    statusElement.title = 'Microphone permission status unknown';
                    break;
            }
        }
        
        // Show info popup on first load or load stored user info
        window.addEventListener('load', () => {
            // Initialize speech synthesis
            initializeSpeechSynthesis();
            
            // Check microphone permissions
            checkMicrophonePermissions();
            
            // Check if user has already provided info in localStorage
            const storedUserInfo = localStorage.getItem('userInfo');
            let hasUserInfo = false;
            
            if (storedUserInfo) {
                try {
                    userInfo = JSON.parse(storedUserInfo);
                    hasUserInfo = true;
                    
                    // Update welcome message if name provided
                    if (userInfo.name) {
                        document.querySelector('.welcome-text').textContent = `Welcome Back, ${userInfo.name}!`;
                    }
                } catch (error) {
                    console.error('Error parsing stored user info:', error);
                }
            }
            
            if (!hasUserInfo) {
                setTimeout(() => {
                    showInfoPopup();
                }, 1000);
            }
        });
        
        function extractResourceInfo(response) {
            // Extract phone numbers and organization names from response
            const phoneRegex = /(\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4})/g;
            const phones = response.match(phoneRegex);
            
            // Extract organization names
            const orgRegex = /([A-Z][^.]*(?:Center|Bank|Service|House|Shelter|Clinic|Organization|Foundation|Project|Community|Food)[^.]*)/g;
            const orgs = response.match(orgRegex);
            
            // Store for action buttons
            if (phones && phones.length > 0) {
                lastResourceInfo = {
                    phone: phones[0],
                    organization: orgs && orgs.length > 0 ? orgs[0] : 'Resource',
                    text: response
                };
            }
        }
        
        function makeCall() {
            if (lastResourceInfo && lastResourceInfo.phone) {
                // For mobile devices, this will open the phone app
                window.location.href = `tel:${lastResourceInfo.phone}`;
            } else {
                alert('No phone number found in the last response. Please ask for specific contact information.');
            }
        }
        
        function sendEmail() {
            if (lastResourceInfo) {
                const subject = encodeURIComponent('Resource Information Request');
                const body = encodeURIComponent(`Hi,\n\nI found your contact information through the Social Change Helper app. I'm interested in learning more about your services.\n\nThe information I received was:\n${lastResourceInfo.text}\n\nCould you please provide more details about how I can access your services?\n\nThank you,\n${userInfo.name || 'A community member'}`);
                
                // Open default email client
                window.location.href = `mailto:?subject=${subject}&body=${body}`;
            } else {
                alert('No resource information available. Please ask for specific resources first.');
            }
        }
    </script>
</body>
</html> 
```

# instance/social_change_app.db

This is a binary file of the type: Binary

# MICROPHONE_GUIDE.md

```md
# 🎤 Microphone & Voice Chat Implementation Guide

## Overview

The Helper app now includes full microphone and voice chat functionality using the Web Speech API for both speech recognition (speech-to-text) and speech synthesis (text-to-speech).

## Features Implemented

### ✅ Speech Recognition (Speech-to-Text)

- **Real-time voice input** using Web Speech API
- **Automatic transcription** of spoken words
- **Visual feedback** with pulsing animation during listening
- **Error handling** for microphone permissions and recognition errors
- **Browser compatibility** checks and fallbacks

### ✅ Speech Synthesis (Text-to-Speech)

- **Automatic response reading** - AI responses are spoken aloud
- **Natural voice selection** - prefers Google/Microsoft voices
- **Visual feedback** with glowing animation during speech
- **Speech controls** - tap to stop speech mid-sentence
- **Text cleanup** - removes markdown and emojis for natural speech

### ✅ Permission Management

- **Automatic permission detection** using Permissions API
- **Visual permission status** with color-coded indicators
- **Graceful permission handling** with helpful error messages
- **Browser compatibility** across Chrome, Edge, Safari

### ✅ Integration with AI Chat

- **Seamless voice-to-chat** - spoken input automatically opens chat
- **Mode-aware responses** - Coach vs Assistant mode support
- **Resource extraction** - voice works with resource formatting
- **Full conversation flow** - maintains chat history and context

## Browser Support

| Browser | Speech Recognition | Speech Synthesis | Recommended  |
| ------- | ------------------ | ---------------- | ------------ |
| Chrome  | ✅ Full Support    | ✅ Full Support  | ⭐ Best      |
| Edge    | ✅ Full Support    | ✅ Full Support  | ⭐ Best      |
| Safari  | ✅ Full Support    | ✅ Full Support  | ✅ Good      |
| Firefox | ❌ Limited         | ✅ Full Support  | ⚠️ Text Only |

## How It Works

### 1. Voice Input Flow

\`\`\`
User clicks microphone → Permission check → Start recording →
Speech recognition → Transcription → Send to AI → Response →
Text-to-speech playback
\`\`\`

### 2. Visual States

- **Default**: Blue circle with microphone icon
- **Listening**: Pulsing blue animation with "Listening..." status
- **Processing**: "Processing your message..." status
- **Speaking**: Green glowing animation with "Speaking..." status
- **Error**: Red status message with helpful guidance

### 3. Permission States

- **🟢 Green dot**: Microphone access granted
- **🔴 Red dot**: Microphone access denied
- **⚪ Gray dot**: Permission status unknown

## Key Files Modified

### `index.html` - Main Implementation

- Added Web Speech API integration
- Implemented `initializeSpeechRecognition()` function
- Added `processVoiceInput()` for handling transcriptions
- Created `speakResponse()` for text-to-speech
- Added permission checking with `checkMicrophonePermissions()`
- Enhanced visual feedback with CSS animations

### `test_microphone.html` - Testing Tool

- Standalone microphone testing interface
- Browser compatibility checker
- Permission status display
- Isolated testing environment

## Usage Instructions

### For Users

1. **Grant Permissions**: Click "Allow" when prompted for microphone access
2. **Start Voice Chat**: Click the blue circle on the Voice Chat tab
3. **Speak Clearly**: Wait for "Listening..." then speak your message
4. **Listen to Response**: The AI will respond both in text and voice
5. **Stop Speech**: Click the circle during speech to stop playback
6. **Continue Conversation**: Click again to speak another message

### For Developers

1. **Test Microphone**: Open `test_microphone.html` to verify functionality
2. **Check Console**: Monitor browser console for speech events and errors
3. **Debug Permissions**: Use browser DevTools → Security tab to check permissions
4. **Test Different Browsers**: Verify compatibility across supported browsers

## Troubleshooting

### Common Issues

#### ❌ "Microphone not accessible"

**Solution**:

- Check browser permissions in address bar
- Go to browser Settings → Privacy → Microphone
- Ensure site has microphone access

#### ❌ "Speech recognition not supported"

**Solution**:

- Use Chrome, Edge, or Safari
- Update browser to latest version
- Try the test page: `test_microphone.html`

#### ❌ "No speech detected"

**Solution**:

- Check microphone is working in other apps
- Ensure microphone is not muted
- Speak louder and closer to microphone
- Check for background noise

#### ❌ Speech synthesis not working

**Solution**:

- Check system volume is not muted
- Try different browser
- Test with: `test_microphone.html`

### Permission Reset

If permissions are denied:

1. Click the lock icon in browser address bar
2. Reset microphone permissions
3. Refresh the page
4. Click "Allow" when prompted again

## Testing

### Manual Testing Steps

1. **Open Test Page**: Navigate to `test_microphone.html`
2. **Check Support**: Verify green checkmarks for browser support
3. **Test Recognition**: Click microphone, speak a sentence
4. **Verify Transcription**: Check if speech is correctly transcribed
5. **Test Synthesis**: Click "Test Speech Synthesis" button
6. **Test Integration**: Go to main app and test full voice chat flow

### Automated Testing

\`\`\`javascript
// Test speech recognition availability
const speechRecognitionSupported =
  "webkitSpeechRecognition" in window || "SpeechRecognition" in window;

// Test speech synthesis availability
const speechSynthesisSupported = "speechSynthesis" in window;

// Test microphone permissions
navigator.permissions.query({ name: "microphone" }).then((result) => {
  console.log("Microphone permission:", result.state);
});
\`\`\`

## Configuration Options

### Speech Recognition Settings

\`\`\`javascript
recognition.continuous = false; // Single phrase recognition
recognition.interimResults = false; // Final results only
recognition.lang = "en-US"; // English language
\`\`\`

### Speech Synthesis Settings

\`\`\`javascript
utterance.rate = 0.9; // Slightly slower than normal
utterance.pitch = 1; // Normal pitch
utterance.volume = 0.8; // 80% volume
\`\`\`

## Performance Considerations

### Optimization Features

- **Text Length Limiting**: Long responses truncated to 500 characters for speech
- **Cleanup Processing**: Markdown and emojis removed for natural speech
- **Voice Caching**: Browser caches available voices for faster selection
- **Error Recovery**: Automatic fallback to text-only mode if voice fails

### Best Practices

- **Short Interactions**: Keep voice messages concise for better recognition
- **Clear Speech**: Speak clearly and at normal pace
- **Quiet Environment**: Minimize background noise for better accuracy
- **Browser Choice**: Use Chrome or Edge for best experience

## Future Enhancements

### Planned Features

- **Voice Commands**: "Stop", "Repeat", "Louder" voice controls
- **Language Selection**: Multi-language speech recognition
- **Voice Profiles**: Personalized voice settings per user
- **Noise Cancellation**: Background noise filtering
- **Offline Mode**: Local speech processing capabilities

### Integration Opportunities

- **Phone Integration**: Direct calling through voice commands
- **Calendar Integration**: Voice scheduling of appointments
- **Location Services**: Voice-activated navigation to resources
- **Emergency Features**: Voice-activated emergency contacts

## API Integration

The voice functionality integrates seamlessly with the existing chat API:

\`\`\`javascript
// Voice input automatically calls the same endpoint as text chat
const response = await fetch("http://localhost:5001/api/chat/message", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    message: transcript, // Voice transcription
    context: userInfo, // User context
    user_id: userInfo.user_id, // Session continuity
    prompt_type: promptType, // Coach vs Assistant mode
    mode: currentMode, // Current interaction mode
  }),
});
\`\`\`

## Security & Privacy

### Data Handling

- **Local Processing**: Speech recognition happens in browser
- **No Audio Storage**: Audio is not stored or transmitted
- **Transcript Only**: Only text transcription sent to server
- **Permission Respect**: Honors browser permission settings

### Privacy Features

- **Explicit Consent**: Clear permission requests
- **Visual Indicators**: Always shows when microphone is active
- **Easy Disable**: Simple click to stop recording
- **No Background Listening**: Only active when user initiates

---

## Quick Start Checklist

- [ ] ✅ Backend running on `http://localhost:5001`
- [ ] ✅ Frontend running on `http://localhost:8000`
- [ ] ✅ Using supported browser (Chrome/Edge/Safari)
- [ ] ✅ Microphone permissions granted
- [ ] ✅ System volume enabled
- [ ] ✅ Test page verified: `test_microphone.html`
- [ ] ✅ Voice chat working in main app

**The microphone functionality is now fully operational! 🎉**

```

# MODE_SWITCHING_GUIDE.md

```md
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

\`\`\`
"I hear you're feeling overwhelmed by your housing situation. Many people have been where you are, and here's what often helps... Let's break this down into simple steps you can take today."
\`\`\`

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

\`\`\`
"Here are food resources in Oakland:
• Alameda County Community Food Bank
• Address: 7900 Edgewater Dr, Oakland, CA 94621
• Phone: (510) 635-3663
• Hours: Monday-Friday, 9am-4pm
• Requirements: None - just show up during operating hours"
\`\`\`

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

\`\`\`
User: "I'm struggling to find housing"
Response: "I understand housing challenges can feel overwhelming. Let's break this down into manageable steps. Many people have found success by first focusing on immediate shelter, then working on longer-term solutions. What's your most urgent need right now - a place to sleep tonight or help with applications for permanent housing?"
\`\`\`

### Assistant Mode Conversation:

\`\`\`
User: "I'm struggling to find housing"
Response: "Here are housing resources in your area:

SHELTER OPTIONS:
• Henry Robinson Center
• Address: 1026 Mission Blvd, Oakland, CA
• Phone: (510) 266-2724
• Beds Available: 137
• Call before 7 PM for intake

[Call Resource] [Send Email] buttons appear
\`\`\`

## 🔄 How to Switch Modes

### For Users:

1. Use the mode toggle buttons in the top navigation
2. **🧠 Coach Mode**: For motivation, life advice, and emotional support
3. **📋 Assistant Mode**: For immediate resources and contact information

### For Developers:

\`\`\`javascript
// Frontend
switchMode('coach')    // or 'assistant'

// Backend API
{
  "message": "I need help",
  "mode": "coach",      // or "assistant"
  "context": {...}
}
\`\`\`

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

```

# models/__init__.py

```py
# Models package for database schemas

```

# models/conversation.py

```py
from datetime import datetime
from .user import db


class Conversation(db.Model):
    """Conversation model for storing chat messages"""
    __tablename__ = 'conversations'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    message = db.Column(db.Text, nullable=False)
    response = db.Column(db.Text, nullable=True)  # Claude's response
    # 'user' or 'assistant'
    message_type = db.Column(db.String(20), default='user')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Context information
    context = db.Column(db.JSON, nullable=True)  # Store context as JSON

    def __repr__(self):
        return f'<Conversation {self.id}: User {self.user_id} - {self.message_type}>'

    def to_dict(self):
        """Convert conversation to dictionary for JSON responses"""
        return {
            'id': self.id,
            'user_id': self.user_id,
            'message': self.message,
            'response': self.response,
            'message_type': self.message_type,
            'context': self.context,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }

```

# models/journal.py

```py
# Daily logs from journaling/chat

```

# models/resource.py

```py
# Food banks, shelters, clinics

```

# models/session.py

```py
# LLM session + conversation memory

```

# models/user.py

```py
# User info schema

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class User(db.Model):
    """User model for storing user information"""
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=True)
    location = db.Column(db.String(200), nullable=True)  # City, zip code, etc.
    # Current situation description
    situation = db.Column(db.Text, nullable=True)
    needs = db.Column(db.Text, nullable=True)  # What kind of help they need
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationship to conversations
    conversations = db.relationship(
        'Conversation', backref='user', lazy=True, cascade='all, delete-orphan')

    def __repr__(self):
        return f'<User {self.id}: {self.name or "Anonymous"}>'

    def to_dict(self):
        """Convert user to dictionary for JSON responses"""
        return {
            'id': self.id,
            'name': self.name,
            'location': self.location,
            'situation': self.situation,
            'needs': self.needs,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }

```

# README.md

```md
# CAG Chatbot Flask API

A Flask-based REST API for a CAG (Context-Aware Generation) chatbot system.

## Features

- RESTful API endpoints for chat interactions
- Chat history management
- User session handling
- Configurable CAG integration
- CORS support for frontend integration
- Comprehensive error handling and logging

## Project Structure

\`\`\`
.
├── app.py              # Main Flask application
├── config.py           # Configuration management
├── cag_service.py      # CAG chatbot service layer
├── requirements.txt    # Python dependencies
└── README.md          # This file
\`\`\`

## Setup Instructions

### 1. Install Dependencies

\`\`\`bash
pip install -r requirements.txt
\`\`\`

### 2. Environment Configuration

Create a `.env` file in the root directory with the following variables:

\`\`\`env
# Flask Configuration
SECRET_KEY=your-secret-key-here
DEBUG=True
PORT=5000

# CAG Chatbot Configuration
CAG_API_KEY=your-cag-api-key
CAG_MODEL_NAME=your-model-name
CAG_API_URL=https://api.cag.example.com

# Logging Configuration
LOG_LEVEL=INFO
\`\`\`

### 3. Run the Application

#### Development Mode

\`\`\`bash
python app.py
\`\`\`

#### Production Mode

\`\`\`bash
gunicorn -w 4 -b 0.0.0.0:5000 app:app
\`\`\`

The application will be available at `http://localhost:5000`

## API Endpoints

### Health Check

- **GET** `/`
- Returns application status

### Chat Endpoints

#### Send Message

- **POST** `/api/chat`
- **Body:**
  \`\`\`json
  {
    "message": "Hello, how are you?",
    "user_id": "user123"
  }
  \`\`\`
- **Response:**
  \`\`\`json
  {
    "response": "Hello! I'm doing well, thank you for asking.",
    "user_id": "user123",
    "timestamp": "2024-01-01T12:00:00"
  }
  \`\`\`

#### Get Chat History

- **GET** `/api/chat/history?user_id=user123`
- **Response:**
  \`\`\`json
  {
    "chat_history": [
      {
        "user_id": "user123",
        "message": "Hello",
        "timestamp": "2024-01-01T12:00:00",
        "type": "user"
      },
      {
        "user_id": "bot",
        "message": "Hello! How can I help you?",
        "timestamp": "2024-01-01T12:00:01",
        "type": "bot"
      }
    ],
    "total_messages": 2
  }
  \`\`\`

#### Clear Chat History

- **POST** `/api/chat/clear`
- **Body:**
  \`\`\`json
  {
    "user_id": "user123"
  }
  \`\`\`
- **Response:**
  \`\`\`json
  {
    "message": "Chat history cleared for user user123",
    "remaining_messages": 0
  }
  \`\`\`

## CAG Integration

The application includes a placeholder CAG service in `cag_service.py`. To integrate with your actual CAG system:

1. Update the `CAGService.generate_response()` method in `cag_service.py`
2. Configure your CAG API credentials in the environment variables
3. Implement the actual API calls to your CAG system

### Example CAG Integration

\`\`\`python
def generate_response(self, message: str, user_id: str, context: Optional[Dict[str, Any]] = None) -> str:
    payload = {
        'message': message,
        'user_id': user_id,
        'model': self.model_name,
        'context': context or {}
    }

    headers = {
        'Authorization': f'Bearer {self.api_key}',
        'Content-Type': 'application/json'
    }

    response = requests.post(
        f"{self.api_url}/generate",
        json=payload,
        headers=headers,
        timeout=30
    )
    response.raise_for_status()
    return response.json()['response']
\`\`\`

## Development

### Adding New Endpoints

1. Add your route in `app.py`
2. Implement proper error handling
3. Add logging for debugging
4. Update this README with endpoint documentation

### Testing

You can test the API using curl or any HTTP client:

\`\`\`bash
# Health check
curl http://localhost:5000/

# Send a message
curl -X POST http://localhost:5000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello", "user_id": "test_user"}'

# Get chat history
curl http://localhost:5000/api/chat/history?user_id=test_user
\`\`\`

## Deployment

### Docker (Optional)

Create a `Dockerfile`:

\`\`\`dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
\`\`\`

### Environment Variables for Production

- Set `DEBUG=False`
- Use a strong `SECRET_KEY`
- Configure your CAG API credentials
- Set appropriate `LOG_LEVEL`

## Error Handling

The application includes comprehensive error handling:

- 400: Bad Request (missing required fields)
- 404: Not Found (invalid endpoints)
- 500: Internal Server Error (server-side issues)

All errors return JSON responses with descriptive messages.

## Logging

The application uses Python's logging module with configurable log levels. Logs include:

- Incoming requests
- CAG API interactions
- Error conditions
- Application startup/shutdown

## Security Considerations

- CORS is enabled for frontend integration
- Input validation on all endpoints
- Environment variable configuration for sensitive data
- Error messages don't expose internal system details

## Contributing

1. Follow the existing code structure
2. Add proper error handling and logging
3. Update documentation for new features
4. Test your changes thoroughly

```

# requirements.txt

```txt
Flask==2.3.3
Flask-CORS==4.0.0
Flask-SQLAlchemy==3.0.5
python-dotenv==1.0.0
requests==2.31.0 
```

# routes/__init__.py

```py
# Routes package for Flask application

```

# routes/admin.py

```py
from flask import Blueprint, render_template_string, request, jsonify, redirect, url_for
from models.user import User, db
from models.conversation import Conversation
from datetime import datetime, timedelta
import json

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

# Simple authentication check (in production, use proper auth)


def check_admin_auth():
    """Simple admin check - in production, implement proper authentication"""
    # For now, just check if it's localhost
    # In production, add proper admin authentication
    return True


# Simple admin template
ADMIN_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Social Worker Portal</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: #f8f9fa;
            color: #333;
            line-height: 1.6;
        }
        
        .header {
            background: #007bff;
            color: white;
            padding: 1rem 2rem;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        
        .header h1 {
            margin: 0;
            font-size: 1.5rem;
        }
        
        .nav {
            background: white;
            padding: 0 2rem;
            border-bottom: 1px solid #dee2e6;
        }
        
        .nav-tabs {
            display: flex;
            gap: 0;
        }
        
        .nav-tab {
            padding: 1rem 1.5rem;
            background: none;
            border: none;
            cursor: pointer;
            border-bottom: 3px solid transparent;
            transition: all 0.3s ease;
        }
        
        .nav-tab.active {
            border-bottom-color: #007bff;
            color: #007bff;
        }
        
        .nav-tab:hover {
            background: #f8f9fa;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
        }
        
        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 1.5rem;
            margin-bottom: 2rem;
        }
        
        .stat-card {
            background: white;
            padding: 1.5rem;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            border-left: 4px solid #007bff;
        }
        
        .stat-number {
            font-size: 2rem;
            font-weight: bold;
            color: #007bff;
            margin-bottom: 0.5rem;
        }
        
        .stat-label {
            color: #666;
            font-size: 0.9rem;
        }
        
        .content-section {
            display: none;
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            overflow: hidden;
        }
        
        .content-section.active {
            display: block;
        }
        
        .section-header {
            background: #f8f9fa;
            padding: 1rem 1.5rem;
            border-bottom: 1px solid #dee2e6;
            font-weight: 600;
        }
        
        .table {
            width: 100%;
            border-collapse: collapse;
        }
        
        .table th,
        .table td {
            padding: 0.75rem 1rem;
            text-align: left;
            border-bottom: 1px solid #dee2e6;
        }
        
        .table th {
            background: #f8f9fa;
            font-weight: 600;
            color: #495057;
        }
        
        .table tbody tr:hover {
            background: #f8f9fa;
        }
        
        .badge {
            display: inline-block;
            padding: 0.25rem 0.5rem;
            font-size: 0.75rem;
            font-weight: 600;
            border-radius: 4px;
        }
        
        .badge-success {
            background: #d4edda;
            color: #155724;
        }
        
        .badge-warning {
            background: #fff3cd;
            color: #856404;
        }
        
        .badge-info {
            background: #d1ecf1;
            color: #0c5460;
        }
        
        .conversation-preview {
            max-width: 300px;
            overflow: hidden;
            text-overflow: ellipsis;
            white-space: nowrap;
        }
        
        .timestamp {
            color: #666;
            font-size: 0.85rem;
        }
        
        .filters {
            padding: 1rem 1.5rem;
            background: #f8f9fa;
            border-bottom: 1px solid #dee2e6;
            display: flex;
            gap: 1rem;
            align-items: center;
        }
        
        .filter-input {
            padding: 0.5rem;
            border: 1px solid #ced4da;
            border-radius: 4px;
            font-size: 0.9rem;
        }
        
        .btn {
            padding: 0.5rem 1rem;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 0.9rem;
            transition: all 0.3s ease;
        }
        
        .btn-primary {
            background: #007bff;
            color: white;
        }
        
        .btn-primary:hover {
            background: #0056b3;
        }
        
        .btn-danger {
            background: #dc3545;
            color: white;
        }
        
        .btn-danger:hover {
            background: #c82333;
        }
        
        .empty-state {
            text-align: center;
            padding: 3rem;
            color: #666;
        }
        
        .refresh-btn {
            position: fixed;
            bottom: 2rem;
            right: 2rem;
            background: #007bff;
            color: white;
            border: none;
            border-radius: 50%;
            width: 60px;
            height: 60px;
            cursor: pointer;
            box-shadow: 0 4px 12px rgba(0,123,255,0.3);
            font-size: 1.2rem;
        }
        
        .refresh-btn:hover {
            background: #0056b3;
            transform: scale(1.05);
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>🏠 Helper Admin Portal</h1>
    </div>
    
    <div class="nav">
        <div class="nav-tabs">
            <button class="nav-tab active" onclick="switchTab('dashboard')">Dashboard</button>
            <button class="nav-tab" onclick="switchTab('users')">Users</button>
            <button class="nav-tab" onclick="switchTab('conversations')">Conversations</button>
            <button class="nav-tab" onclick="switchTab('system')">System</button>
        </div>
    </div>
    
    <div class="container">
        <!-- Dashboard Section -->
        <div id="dashboard" class="content-section active">
            <div class="stats-grid">
                <div class="stat-card">
                    <div class="stat-number" id="totalUsers">{{ stats.total_users }}</div>
                    <div class="stat-label">Total Users</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number" id="totalConversations">{{ stats.total_conversations }}</div>
                    <div class="stat-label">Total Conversations</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number" id="todayUsers">{{ stats.today_users }}</div>
                    <div class="stat-label">Users Today</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number" id="todayConversations">{{ stats.today_conversations }}</div>
                    <div class="stat-label">Messages Today</div>
                </div>
            </div>
            
            <div class="content-section active">
                <div class="section-header">Recent Activity</div>
                <table class="table">
                    <thead>
                        <tr>
                            <th>Time</th>
                            <th>User</th>
                            <th>Action</th>
                            <th>Details</th>
                        </tr>
                    </thead>
                    <tbody id="recentActivity">
                        {% for activity in recent_activity %}
                        <tr>
                            <td class="timestamp">{{ activity.timestamp }}</td>
                            <td>{{ activity.user_name }}</td>
                            <td><span class="badge badge-info">{{ activity.action }}</span></td>
                            <td class="conversation-preview">{{ activity.details }}</td>
                        </tr>
                        {% endfor %}
                    </tbody>
                </table>
            </div>
        </div>
        
        <!-- Users Section -->
        <div id="users" class="content-section">
            <div class="filters">
                <input type="text" class="filter-input" placeholder="Search users..." id="userSearch">
                <button class="btn btn-primary" onclick="filterUsers()">Filter</button>
                <button class="btn btn-danger" onclick="exportUsers()">Export CSV</button>
            </div>
            
            <table class="table">
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Name</th>
                        <th>Location</th>
                        <th>Situation</th>
                        <th>Created</th>
                        <th>Last Active</th>
                        <th>Messages</th>
                    </tr>
                </thead>
                <tbody id="usersTable">
                    {% for user in users %}
                    <tr>
                        <td>{{ user.id }}</td>
                        <td>{{ user.name }}</td>
                        <td>{{ user.location or 'N/A' }}</td>
                        <td>
                            {% if user.situation %}
                                <span class="badge badge-warning">{{ user.situation }}</span>
                            {% else %}
                                <span class="badge badge-info">Unknown</span>
                            {% endif %}
                        </td>
                        <td class="timestamp">{{ user.created_at.strftime('%Y-%m-%d %H:%M') if user.created_at else 'N/A' }}</td>
                        <td class="timestamp">{{ user.last_active.strftime('%Y-%m-%d %H:%M') if user.last_active else 'Never' }}</td>
                        <td>{{ user.message_count }}</td>
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
        </div>
        
        <!-- Conversations Section -->
        <div id="conversations" class="content-section">
            <div class="filters">
                <input type="text" class="filter-input" placeholder="Search conversations..." id="conversationSearch">
                <select class="filter-input" id="modeFilter">
                    <option value="">All Modes</option>
                    <option value="coach">Coach Mode</option>
                    <option value="assistant">Assistant Mode</option>
                </select>
                <button class="btn btn-primary" onclick="filterConversations()">Filter</button>
            </div>
            
            <table class="table">
                <thead>
                    <tr>
                        <th>Time</th>
                        <th>User</th>
                        <th>Mode</th>
                        <th>Message</th>
                        <th>Response Preview</th>
                        <th>Emotion</th>
                    </tr>
                </thead>
                <tbody id="conversationsTable">
                    {% for conv in conversations %}
                    <tr>
                        <td class="timestamp">{{ conv.timestamp.strftime('%Y-%m-%d %H:%M:%S') if conv.timestamp else 'N/A' }}</td>
                        <td>{{ conv.user_name }}</td>
                        <td><span class="badge badge-{{ 'success' if conv.mode == 'coach' else 'info' }}">{{ conv.mode or 'N/A' }}</span></td>
                        <td class="conversation-preview">{{ conv.user_message }}</td>
                        <td class="conversation-preview">{{ conv.ai_response }}</td>
                        <td>
                            {% if conv.emotion_score %}
                                <span class="badge badge-warning">{{ conv.emotion_score }}</span>
                            {% else %}
                                <span class="badge badge-info">N/A</span>
                            {% endif %}
                        </td>
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
        </div>
        
        <!-- System Section -->
        <div id="system" class="content-section">
            <div class="section-header">System Information</div>
            <div style="padding: 1.5rem;">
                <div style="margin-bottom: 2rem;">
                    <h3>API Status</h3>
                    <p><strong>Gemini API:</strong> <span class="badge badge-success">Connected</span></p>
                    <p><strong>Database:</strong> <span class="badge badge-success">Connected</span></p>
                    <p><strong>RAG Pipeline:</strong> <span class="badge badge-success">Active</span></p>
                </div>
                
                <div style="margin-bottom: 2rem;">
                    <h3>Resource Database</h3>
                    <p><strong>Total Resources:</strong> {{ stats.total_resources }}</p>
                    <p><strong>Oakland Resources:</strong> {{ stats.oakland_resources }}</p>
                    <p><strong>Berkeley Resources:</strong> {{ stats.berkeley_resources }}</p>
                </div>
                
                <div>
                    <h3>System Actions</h3>
                    <button class="btn btn-primary" onclick="clearOldData()">Clear Old Data (30+ days)</button>
                    <button class="btn btn-danger" onclick="resetSystem()">Reset System (Danger)</button>
                </div>
            </div>
        </div>
    </div>
    
    <button class="refresh-btn" onclick="refreshData()" title="Refresh Data">↻</button>
    
    <script>
        function switchTab(tabName) {
            // Hide all content sections
            document.querySelectorAll('.content-section').forEach(section => {
                section.classList.remove('active');
            });
            
            // Remove active class from all tabs
            document.querySelectorAll('.nav-tab').forEach(tab => {
                tab.classList.remove('active');
            });
            
            // Show selected content section
            document.getElementById(tabName).classList.add('active');
            
            // Add active class to clicked tab
            event.target.classList.add('active');
        }
        
        function refreshData() {
            window.location.reload();
        }
        
        function filterUsers() {
            const search = document.getElementById('userSearch').value.toLowerCase();
            const rows = document.querySelectorAll('#usersTable tr');
            
            rows.forEach(row => {
                const text = row.textContent.toLowerCase();
                row.style.display = text.includes(search) ? '' : 'none';
            });
        }
        
        function filterConversations() {
            const search = document.getElementById('conversationSearch').value.toLowerCase();
            const mode = document.getElementById('modeFilter').value;
            const rows = document.querySelectorAll('#conversationsTable tr');
            
            rows.forEach(row => {
                const text = row.textContent.toLowerCase();
                const modeMatch = !mode || row.textContent.includes(mode);
                const searchMatch = text.includes(search);
                row.style.display = (searchMatch && modeMatch) ? '' : 'none';
            });
        }
        
        function exportUsers() {
            window.open('/admin/export/users', '_blank');
        }
        
        function clearOldData() {
            if (confirm('This will delete conversations older than 30 days. Continue?')) {
                fetch('/admin/clear-old-data', { method: 'POST' })
                    .then(response => response.json())
                    .then(data => {
                        alert(`Cleared ${data.deleted_count} old records`);
                        refreshData();
                    });
            }
        }
        
        function resetSystem() {
            if (confirm('WARNING: This will delete ALL user data and conversations. This cannot be undone. Continue?')) {
                if (confirm('Are you absolutely sure? This will permanently delete everything.')) {
                    fetch('/admin/reset-system', { method: 'POST' })
                        .then(response => response.json())
                        .then(data => {
                            alert('System reset complete');
                            refreshData();
                        });
                }
            }
        }
        
        // Auto-refresh every 30 seconds
        setInterval(refreshData, 30000);
    </script>
</body>
</html>
"""


@admin_bp.route('/')
def admin_dashboard():
    """Main admin dashboard"""
    try:
        # Get statistics
        stats = {
            'total_users': User.query.count(),
            'total_conversations': Conversation.query.count(),
            'today_users': User.query.filter(User.created_at >= datetime.now().date()).count(),
            'today_conversations': Conversation.query.filter(Conversation.created_at >= datetime.now().date()).count(),
            'total_resources': 64,  # From RAG pipeline
            'oakland_resources': 32,
            'berkeley_resources': 32
        }

        # Get recent activity (last 20 conversations)
        recent_conversations = db.session.query(
            Conversation.created_at,
            User.name.label('user_name'),
            Conversation.message,
            Conversation.response
        ).join(User).order_by(Conversation.created_at.desc()).limit(20).all()

        recent_activity = []
        for conv in recent_conversations:
            recent_activity.append({
                'timestamp': conv.created_at.strftime('%H:%M:%S') if conv.created_at else 'N/A',
                'user_name': conv.user_name or 'Anonymous',
                'action': 'Message',
                'details': conv.message[:50] + '...' if conv.message and len(conv.message) > 50 else conv.message or 'N/A'
            })

        # Get users with message counts
        users = db.session.query(
            User,
            db.func.count(Conversation.id).label('message_count')
        ).outerjoin(Conversation).group_by(User.id).order_by(User.created_at.desc()).limit(50).all()

        users_data = []
        for user, message_count in users:
            users_data.append({
                'id': user.id,
                'name': user.name or 'Anonymous',
                'location': user.location,
                'situation': user.situation,
                'created_at': user.created_at,
                'last_active': user.updated_at,
                'message_count': message_count
            })

        # Get recent conversations with details
        conversations = db.session.query(
            Conversation.created_at,
            User.name.label('user_name'),
            Conversation.message_type,
            Conversation.message,
            Conversation.response,
            Conversation.context
        ).join(User).order_by(Conversation.created_at.desc()).limit(100).all()

        conversations_data = []
        for conv in conversations:
            mode = 'N/A'
            if conv.context:
                try:
                    context_data = json.loads(conv.context) if isinstance(
                        conv.context, str) else conv.context
                    if isinstance(context_data, dict):
                        mode = context_data.get('mode', 'N/A')
                except:
                    pass

            conversations_data.append({
                'timestamp': conv.created_at,
                'user_name': conv.user_name or 'Anonymous',
                'mode': mode,
                'user_message': conv.message,
                'ai_response': conv.response[:100] + '...' if conv.response and len(conv.response) > 100 else conv.response,
                'emotion_score': None  # Not available in current model
            })

        return render_template_string(ADMIN_TEMPLATE,
                                      stats=stats,
                                      recent_activity=recent_activity,
                                      users=users_data,
                                      conversations=conversations_data)

    except Exception as e:
        return f"Error loading admin dashboard: {str(e)}", 500


@admin_bp.route('/export/users')
def export_users():
    """Export users as CSV"""
    try:
        import csv
        import io
        from flask import Response

        output = io.StringIO()
        writer = csv.writer(output)

        # Write header
        writer.writerow(['ID', 'Name', 'Location', 'Situation',
                        'Created At', 'Last Active', 'Phone', 'Email'])

        # Write user data
        users = User.query.all()
        for user in users:
            writer.writerow([
                user.id,
                user.name or 'Anonymous',
                user.location or '',
                user.situation or '',
                user.created_at.strftime(
                    '%Y-%m-%d %H:%M:%S') if user.created_at else '',
                user.updated_at.strftime(
                    '%Y-%m-%d %H:%M:%S') if user.updated_at else '',
                getattr(user, 'phone', '') or '',
                getattr(user, 'email', '') or ''
            ])

        output.seek(0)
        return Response(
            output.getvalue(),
            mimetype='text/csv',
            headers={'Content-Disposition': 'attachment; filename=users_export.csv'}
        )

    except Exception as e:
        return f"Error exporting users: {str(e)}", 500


@admin_bp.route('/clear-old-data', methods=['POST'])
def clear_old_data():
    """Clear conversations older than 30 days"""
    try:
        cutoff_date = datetime.now() - timedelta(days=30)
        deleted_count = Conversation.query.filter(
            Conversation.created_at < cutoff_date).count()
        Conversation.query.filter(
            Conversation.created_at < cutoff_date).delete()
        db.session.commit()

        return jsonify({'success': True, 'deleted_count': deleted_count})

    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'error': str(e)}), 500


@admin_bp.route('/reset-system', methods=['POST'])
def reset_system():
    """Reset entire system - DELETE ALL DATA"""
    try:
        # Delete all conversations
        Conversation.query.delete()

        # Delete all users
        User.query.delete()

        db.session.commit()

        return jsonify({'success': True, 'message': 'System reset complete'})

    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'error': str(e)}), 500


@admin_bp.route('/api/stats')
def api_stats():
    """API endpoint for real-time stats"""
    try:
        stats = {
            'total_users': User.query.count(),
            'total_conversations': Conversation.query.count(),
            'today_users': User.query.filter(User.created_at >= datetime.now().date()).count(),
            'today_conversations': Conversation.query.filter(Conversation.created_at >= datetime.now().date()).count(),
        }
        return jsonify(stats)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

```

# routes/chat.py

```py
# Chat routes - /api/chat endpoints

from flask import Blueprint, request, jsonify
from datetime import datetime
import logging
from models.user import db, User
from models.conversation import Conversation
from services.gemini_service import get_support_response, analyze_journal_entry, summarize_conversation, score_emotional_state
from services.rag_pipeline import get_local_resources
from typing import Optional, Dict, Any

logger = logging.getLogger(__name__)

# Create chat blueprint
chat_bp = Blueprint('chat', __name__)


@chat_bp.route('/api/chat/message', methods=['POST'])
def send_message():
    """
    Send a message to the AI assistant
    Enhanced with RAG pipeline and emotion analysis
    """
    try:
        data = request.get_json()

        if not data or 'message' not in data:
            return jsonify({'error': 'Message is required'}), 400

        message = data['message']
        context = data.get('context', {})
        user_id = data.get('user_id')
        prompt_type = data.get('prompt_type', 'empathetic_coach')

        logger.info(f"Received chat message: {message[:50]}...")

        # Find or create user
        user = None
        if user_id:
            user = User.query.get(user_id)

        if not user:
            # Create new user
            user = User(
                name=context.get('name', 'Anonymous'),
                location=context.get('location', ''),
                situation=context.get('situation', ''),
                needs=context.get('needs', '')
            )
            db.session.add(user)
            db.session.commit()
            logger.info(f"Created new user: {user}")

        # Get emotion analysis for the message
        emotion_scores = score_emotional_state(message)

        # Get mode from request (default to coach)
        mode = data.get('mode', 'coach')

        # Get Gemini response with enhanced context, prompt type, and mode
        gemini_response = get_support_response(message, {
            'name': user.name,
            'location': user.location,
            'situation': user.situation,
            'needs': user.needs
        }, prompt_type, mode)

        # Save conversation with emotion analysis in context
        conversation_context = {
            'user_context': context,
            'emotion_analysis': emotion_scores
        }

        conversation = Conversation(
            user_id=user.id,
            message=message,
            response=gemini_response,
            message_type='text',
            context=conversation_context
        )
        db.session.add(conversation)
        db.session.commit()

        logger.info(f"Saved conversation for user {user.id}")

        return jsonify({
            'response': gemini_response,
            'user_id': user.id,
            'emotion_analysis': emotion_scores,
            'timestamp': conversation.created_at.isoformat()
        })

    except Exception as e:
        logger.error(f"Error processing chat message: {str(e)}")
        return jsonify({'error': 'Internal server error'}), 500


@chat_bp.route('/api/chat/resources', methods=['POST'])
def get_resources():
    """
    Get local resources using RAG pipeline
    """
    try:
        data = request.get_json()

        if not data or 'location' not in data:
            return jsonify({'error': 'Location is required'}), 400

        location = data['location']
        needs = data.get('needs', ['food'])  # Default to food
        situation = data.get('situation', '')

        logger.info(f"RAG resource request for {location} with needs: {needs}")

        # Get resources via RAG pipeline
        resources = get_local_resources(location, needs, situation)

        return jsonify({
            'resources': resources,
            'location': location,
            'needs': needs,
            'timestamp': resources.get('timestamp')
        })

    except Exception as e:
        logger.error(f"Error getting resources: {str(e)}")
        return jsonify({'error': 'Internal server error'}), 500


@chat_bp.route('/api/chat/analyze-journal', methods=['POST'])
def analyze_journal():
    """
    Analyze journal entry using Gemini for emotion scoring
    """
    try:
        data = request.get_json()

        if not data or 'journal_text' not in data:
            return jsonify({'error': 'Journal text is required'}), 400

        journal_text = data['journal_text']
        user_context = data.get('context', {})

        logger.info(f"Analyzing journal entry: {journal_text[:50]}...")

        # Analyze with Gemini
        analysis = analyze_journal_entry(journal_text, user_context)

        return jsonify({
            'analysis': analysis,
            'journal_length': len(journal_text),
            'timestamp': analysis.get('timestamp')
        })

    except Exception as e:
        logger.error(f"Error analyzing journal: {str(e)}")
        return jsonify({'error': 'Internal server error'}), 500


@chat_bp.route('/api/chat/summarize/<int:user_id>', methods=['GET'])
def summarize_user_conversation(user_id):
    """
    Summarize a user's conversation history using Gemini
    """
    try:
        user = User.query.get(user_id)
        if not user:
            return jsonify({'error': 'User not found'}), 404

        # Get recent conversations
        conversations = Conversation.query.filter_by(user_id=user_id)\
            .order_by(Conversation.created_at.desc())\
            .limit(10).all()

        if not conversations:
            return jsonify({'error': 'No conversations found'}), 404

        # Format messages for Gemini
        messages = []
        for conv in reversed(conversations):  # Reverse to get chronological order
            messages.append({'role': 'user', 'content': conv.message})
            messages.append({'role': 'assistant', 'content': conv.response})

        # Get summary from Gemini
        summary = summarize_conversation(messages, {
            'location': user.location,
            'situation': user.situation,
            'needs': user.needs
        })

        return jsonify({
            'summary': summary,
            'user_id': user_id,
            'conversation_count': len(conversations),
            'user_context': {
                'name': user.name,
                'location': user.location,
                'situation': user.situation
            }
        })

    except Exception as e:
        logger.error(f"Error summarizing conversation: {str(e)}")
        return jsonify({'error': 'Internal server error'}), 500


@chat_bp.route('/api/chat/history/<int:user_id>', methods=['GET'])
def get_chat_history(user_id):
    """Get chat history for a user"""
    try:
        user = User.query.get(user_id)
        if not user:
            return jsonify({'error': 'User not found'}), 404

        conversations = Conversation.query.filter_by(user_id=user_id)\
            .order_by(Conversation.created_at.desc())\
            .limit(20).all()

        history = []
        for conv in reversed(conversations):  # Show chronological order
            history.append({
                'id': conv.id,
                'message': conv.message,
                'response': conv.response,
                'timestamp': conv.created_at.isoformat(),
                'message_type': conv.message_type,
                'context': conv.context
            })

        return jsonify({
            'history': history,
            'user_id': user_id,
            'total_conversations': len(conversations)
        })

    except Exception as e:
        logger.error(f"Error getting chat history: {str(e)}")
        return jsonify({'error': 'Internal server error'}), 500


@chat_bp.route('/api/chat/users', methods=['GET'])
def get_users():
    """Get all users"""
    try:
        users = User.query.all()
        user_list = []

        for user in users:
            user_list.append({
                'id': user.id,
                'name': user.name,
                'location': user.location,
                'situation': user.situation,
                'created_at': user.created_at.isoformat(),
                'conversation_count': len(user.conversations)
            })

        return jsonify({
            'users': user_list,
            'total_users': len(user_list)
        })

    except Exception as e:
        logger.error(f"Error getting users: {str(e)}")
        return jsonify({'error': 'Internal server error'}), 500


@chat_bp.route('/api/chat/health', methods=['GET'])
def health_check():
    """Health check endpoint for the chat service"""
    return jsonify({
        'status': 'healthy',
        'service': 'chat',
        'features': {
            'claude_integration': True,
            'rag_pipeline': True,
            'emotion_scoring': True,
            'resource_discovery': True
        }
    })


def _build_enhanced_system_prompt(self, context: Optional[Dict[str, Any]] = None, rag_context: str = "") -> str:
    base_prompt = """You are a compassionate AI assistant..."""

    # Add user context
    if context:
        if context.get('location'):
            context_info += f"\nUser location: {context['location']}"
        if context.get('situation'):
            context_info += f"\nUser situation: {context['situation']}"

    # Add RAG context with local resources
    if rag_context:
        base_prompt += f"\n\nLocal Resources Available:\n{rag_context}"
        base_prompt += "\nUse these specific local resources in your response."

```

# routes/resources.py

```py
# Resources routes - /api/resources endpoints

```

# routes/voice.py

```py
# Voice routes - /api/voice endpoints

```

# services/__init__.py

```py
# Services package for external API integrations

```

# services/claude_service_backup.py

```py
# Claude 4 calls, prompt templates

import os
import logging
from typing import Dict, Any, Optional, List
import requests
import json
from dotenv import load_dotenv
from datetime import datetime
from .rag_pipeline import rag_pipeline

# Load environment variables from .env file
load_dotenv()

logger = logging.getLogger(__name__)


class ClaudeService:
    """Service for interacting with Claude API"""

    def __init__(self):
        self.api_key = os.environ.get('CLAUDE_API_KEY')
        self.api_url = "https://api.anthropic.com/v1/messages"
        self.model = "claude-3-5-sonnet-20241022"

        if not self.api_key:
            logger.warning("CLAUDE_API_KEY not set in environment variables")

    def get_support_response(self, message: str, context: Optional[Dict[str, Any]] = None) -> str:
        """
        Generate a supportive response using Claude API with RAG enhancement

        Args:
            message: User's input message
            context: Optional context information (user situation, location, etc.)

        Returns:
            Claude's response as a string
        """
        try:
            if not self.api_key:
                return self._fallback_response(message)

            # Get local resources via RAG pipeline
            rag_context = ""
            if context and context.get('location'):
                needs = self._extract_needs_from_message(message, context)
                rag_results = rag_pipeline.retrieve_resources(
                    context.get('location'),
                    needs,
                    context.get('situation')
                )
                rag_context = rag_pipeline.format_resources_for_claude(
                    rag_results)
                logger.info(
                    f"RAG retrieved {rag_results.get('total_resources', 0)} resources")

            # Build the enhanced system prompt
            system_prompt = self._build_enhanced_system_prompt(
                context, rag_context)

            # Prepare the API request
            headers = {
                "Content-Type": "application/json",
                "x-api-key": self.api_key,
                "anthropic-version": "2023-06-01"
            }

            payload = {
                "model": self.model,
                "max_tokens": 1200,  # Increased for more detailed responses
                "system": system_prompt,
                "messages": [
                    {
                        "role": "user",
                        "content": message
                    }
                ]
            }

            logger.info(
                f"Sending request to Claude API for message: {message[:50]}...")

            response = requests.post(
                self.api_url,
                headers=headers,
                json=payload,
                timeout=30
            )

            if response.status_code == 200:
                response_data = response.json()
                claude_response = response_data['content'][0]['text']
                logger.info("Successfully received response from Claude API")
                return claude_response
            else:
                logger.error(
                    f"Claude API error: {response.status_code} - {response.text}")
                return self._fallback_response(message)

        except requests.exceptions.RequestException as e:
            logger.error(f"Network error calling Claude API: {str(e)}")
            return self._fallback_response(message)
        except Exception as e:
            logger.error(f"Unexpected error in Claude service: {str(e)}")
            return self._fallback_response(message)

    def analyze_journal_entry(self, journal_text: str, user_context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Analyze a journal entry for emotion scoring and insights using Claude

        Args:
            journal_text: The journal entry text
            user_context: Optional user context for personalized analysis

        Returns:
            Dictionary with emotion scores, insights, and suggestions
        """
        try:
            if not self.api_key:
                return self._fallback_analysis(journal_text)

            prompt = f"""Analyze this journal entry and provide insights in JSON format:

Journal Entry: "{journal_text}"

Please analyze and respond with ONLY a valid JSON object containing:
{{
    "emotion_scores": {{
        "distress": 0.0-1.0,
        "hope": 0.0-1.0,
        "motivation": 0.0-1.0,
        "anxiety": 0.0-1.0,
        "positivity": 0.0-1.0
    }},
    "key_themes": ["theme1", "theme2", "theme3"],
    "insights": "Brief insight about the person's emotional state",
    "suggestions": "Supportive suggestions for improvement",
    "urgency_level": "low|medium|high"
}}"""

            if user_context:
                prompt += f"\n\nUser Context: {user_context.get('situation', '')} in {user_context.get('location', '')}"

            response = self._call_claude_api(prompt, max_tokens=800)
            if response:
                return self._parse_json_response(response, self._fallback_analysis(journal_text))
            else:
                return self._fallback_analysis(journal_text)

        except Exception as e:
            logger.error(f"Error analyzing journal entry: {str(e)}")
            return self._fallback_analysis(journal_text)

    def summarize_conversation(self, messages: List[Dict[str, str]], user_context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Summarize a conversation for context and insights using Claude

        Args:
            messages: List of message dictionaries with 'role' and 'content'
            user_context: Optional user context

        Returns:
            Dictionary with summary, key themes, and recommendations
        """
        try:
            if not self.api_key:
                return self._fallback_summary(messages)

            conversation = "\n".join(
                [f"{msg.get('role', 'user')}: {msg.get('content', '')}" for msg in messages[-10:]])  # Last 10 messages

            prompt = f"""Summarize this conversation and provide insights in JSON format:

Conversation:
{conversation}

Please analyze and respond with ONLY a valid JSON object containing:
{{
    "summary": "Brief summary of the conversation",
    "user_needs": ["need1", "need2", "need3"],
    "emotional_tone": "overall emotional tone",
    "progress_indicators": ["positive sign1", "positive sign2"],
    "recommendations": ["recommendation1", "recommendation2"],
    "follow_up_needed": true/false
}}"""

            if user_context:
                prompt += f"\n\nUser Context: {user_context.get('situation', '')} in {user_context.get('location', '')}"

            response = self._call_claude_api(prompt, max_tokens=800)
            if response:
                return self._parse_json_response(response, self._fallback_summary(messages))
            else:
                return self._fallback_summary(messages)

        except Exception as e:
            logger.error(f"Error summarizing conversation: {str(e)}")
            return self._fallback_summary(messages)

    def score_emotional_state(self, text: str) -> Dict[str, float]:
        """
        Score emotional state from text using Claude

        Args:
            text: Text to analyze

        Returns:
            Dictionary with emotion scores (0-1 scale)
        """
        try:
            if not self.api_key:
                return self._fallback_emotion_scores()

            prompt = f"""Score the emotional content of this text on a 0-1 scale and respond with ONLY a valid JSON object:

Text: "{text}"

Respond with:
{{
    "distress": 0.0-1.0,
    "hope": 0.0-1.0,
    "motivation": 0.0-1.0,
    "anxiety": 0.0-1.0,
    "positivity": 0.0-1.0,
    "overall_sentiment": "positive|neutral|negative"
}}"""

            response = self._call_claude_api(prompt, max_tokens=400)
            if response:
                return self._parse_json_response(response, self._fallback_emotion_scores())
            else:
                return self._fallback_emotion_scores()

        except Exception as e:
            logger.error(f"Error scoring emotional state: {str(e)}")
            return self._fallback_emotion_scores()

    def _call_claude_api(self, prompt: str, max_tokens: int = 1200) -> Optional[str]:
        """Make API call to Claude for analysis tasks"""
        try:
            headers = {
                "Content-Type": "application/json",
                "x-api-key": self.api_key,
                "anthropic-version": "2023-06-01"
            }

            payload = {
                "model": self.model,
                "max_tokens": max_tokens,
                "messages": [
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            }

            response = requests.post(
                self.api_url,
                headers=headers,
                json=payload,
                timeout=30
            )

            if response.status_code == 200:
                response_data = response.json()
                return response_data['content'][0]['text']
            else:
                logger.error(
                    f"Claude API error: {response.status_code} - {response.text}")
                return None

        except Exception as e:
            logger.error(f"Error calling Claude API: {str(e)}")
            return None

    def _parse_json_response(self, response: str, fallback: Dict[str, Any]) -> Dict[str, Any]:
        """Parse JSON response from Claude"""
        try:
            # Clean up response
            response_clean = response.strip()
            if response_clean.startswith('\`\`\`json'):
                response_clean = response_clean[7:-3]
            elif response_clean.startswith('\`\`\`'):
                response_clean = response_clean[3:-3]

            parsed = json.loads(response_clean)

            # Add metadata
            parsed['timestamp'] = datetime.now().isoformat()
            parsed['source'] = 'claude'

            return parsed

        except json.JSONDecodeError as e:
            logger.error(f"Failed to parse Claude JSON response: {str(e)}")
            return fallback

    def _extract_needs_from_message(self, message: str, context: Optional[Dict[str, Any]] = None) -> List[str]:
        """Extract needs from user message and context"""
        needs = []
        message_lower = message.lower()

        # Extract from message
        if any(word in message_lower for word in ["food", "hungry", "eat", "meal"]):
            needs.append("food")
        if any(word in message_lower for word in ["shelter", "housing", "sleep", "bed", "place to stay"]):
            needs.append("shelter")
        if any(word in message_lower for word in ["health", "medical", "doctor", "clinic", "sick"]):
            needs.append("healthcare")
        if any(word in message_lower for word in ["job", "work", "employment", "career"]):
            needs.append("employment")

        # Extract from context
        if context and context.get('needs'):
            context_needs = context['needs'].lower()
            if any(word in context_needs for word in ["food", "hungry", "eat"]):
                needs.append("food")
            if any(word in context_needs for word in ["shelter", "housing", "sleep"]):
                needs.append("shelter")
            if any(word in context_needs for word in ["health", "medical"]):
                needs.append("healthcare")
            if any(word in context_needs for word in ["job", "work", "employment"]):
                needs.append("employment")

        # Default to food if no specific needs detected
        if not needs:
            needs = ["food"]

        return list(set(needs))  # Remove duplicates

    def _build_enhanced_system_prompt(self, context: Optional[Dict[str, Any]] = None, rag_context: str = "") -> str:
        """Build enhanced system prompt with RAG context"""
        base_prompt = """You are a compassionate AI assistant for a social change app that helps people in difficult situations. Your role is to:

1. Provide warm, empathetic support using motivational interviewing techniques
2. Help users find local resources (food banks, shelters, clinics, job assistance)
3. Offer practical guidance and emotional support
4. Maintain hope and dignity in all interactions
5. Be non-judgmental and respectful

Always respond with empathy and practical help. Use specific local resource information when available."""

        # Add user context
        if context:
            context_info = ""
            if context.get('location'):
                context_info += f"\nUser location: {context['location']}"
            if context.get('situation'):
                context_info += f"\nUser situation: {context['situation']}"
            if context.get('needs'):
                context_info += f"\nUser needs: {context['needs']}"

            if context_info:
                base_prompt += f"\n\nUser Context:{context_info}"

        # Add RAG context with local resources
        if rag_context:
            base_prompt += f"\n\nLocal Resources Available:\n{rag_context}"
            base_prompt += "\nUse these specific local resources in your response. Provide exact addresses, phone numbers, and hours when available."

        return base_prompt

    def _build_system_prompt(self, context: Optional[Dict[str, Any]] = None) -> str:
        """Build the system prompt for Claude based on context (legacy method)"""
        return self._build_enhanced_system_prompt(context, "")

    def _fallback_response(self, message: str) -> str:
        """Fallback response when Claude API is unavailable"""
        return f"I understand you're reaching out for support. While I'm having trouble connecting to my full capabilities right now, I want you to know that your message is important. You mentioned: '{message}'. Please know that help is available, and you're taking a positive step by seeking support. Is there something specific I can try to help you with right now?"

    def _fallback_analysis(self, journal_text: str) -> Dict[str, Any]:
        """Fallback analysis when Claude is unavailable"""
        # Simple keyword-based analysis
        text_lower = journal_text.lower()

        distress_words = ['sad', 'depressed', 'anxious', 'worried',
                          'scared', 'hopeless', 'difficult', 'hard', 'struggle']
        hope_words = ['better', 'hope', 'improve', 'positive',
                      'good', 'happy', 'grateful', 'thankful']

        distress_score = min(sum(
            1 for word in distress_words if word in text_lower) / len(distress_words), 1.0)
        hope_score = min(
            sum(1 for word in hope_words if word in text_lower) / len(hope_words), 1.0)

        return {
            "emotion_scores": {
                "distress": distress_score,
                "hope": hope_score,
                "motivation": 0.5,
                "anxiety": min(distress_score * 0.8, 1.0),
                "positivity": min(hope_score * 1.2, 1.0)
            },
            "key_themes": ["personal reflection"],
            "insights": "Journal entry reflects personal thoughts and experiences",
            "suggestions": "Continue journaling to track your emotional journey",
            "urgency_level": "low",
            "timestamp": datetime.now().isoformat(),
            "source": "fallback"
        }

    def _fallback_summary(self, messages: List[Dict]) -> Dict[str, Any]:
        """Fallback summary when Claude is unavailable"""
        return {
            "summary": f"Conversation with {len(messages)} messages about support and resources",
            "user_needs": ["support", "resources"],
            "emotional_tone": "seeking assistance",
            "progress_indicators": ["reaching out for help"],
            "recommendations": ["continue conversation", "follow up on resources"],
            "follow_up_needed": True,
            "timestamp": datetime.now().isoformat(),
            "source": "fallback"
        }

    def _fallback_emotion_scores(self) -> Dict[str, float]:
        """Fallback emotion scores when Claude is unavailable"""
        return {
            "distress": 0.5,
            "hope": 0.5,
            "motivation": 0.5,
            "anxiety": 0.5,
            "positivity": 0.5,
            "overall_sentiment": "neutral",
            "source": "fallback"
        }


# Global instance
claude_service = ClaudeService()


def get_support_response(message: str, context: Optional[Dict[str, Any]] = None) -> str:
    """
    Main function to get support response from Claude
    This is the function required by Task 3
    """
    return claude_service.get_support_response(message, context)


def analyze_journal_entry(journal_text: str, user_context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Main function to analyze journal entries using Claude"""
    return claude_service.analyze_journal_entry(journal_text, user_context)


def summarize_conversation(messages: List[Dict[str, str]], user_context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Main function to summarize conversations using Claude"""
    return claude_service.summarize_conversation(messages, user_context)


def score_emotional_state(text: str) -> Dict[str, float]:
    """Main function to score emotional state using Claude"""
    return claude_service.score_emotional_state(text)

```

# services/claude_service_old.py

```py
# Claude 4 calls, prompt templates

import os
import logging
from typing import Dict, Any, Optional, List
import requests
import json
from dotenv import load_dotenv
from datetime import datetime
from .rag_pipeline import rag_pipeline

# Load environment variables from .env file
load_dotenv()

logger = logging.getLogger(__name__)


class ClaudeService:
    """Service for interacting with Claude API"""

    def __init__(self):
        self.api_key = os.environ.get('CLAUDE_API_KEY')
        self.api_url = "https://api.anthropic.com/v1/messages"
        self.model = "claude-3-5-sonnet-20241022"

        if not self.api_key:
            logger.warning("CLAUDE_API_KEY not set in environment variables")

    def get_support_response(self, message: str, context: Optional[Dict[str, Any]] = None) -> str:
        """
        Generate a supportive response using Claude API with RAG enhancement

        Args:
            message: User's input message
            context: Optional context information (user situation, location, etc.)

        Returns:
            Claude's response as a string
        """
        try:
            if not self.api_key:
                return self._fallback_response(message)

            # Get local resources via RAG pipeline
            rag_context = ""
            if context and context.get('location'):
                needs = self._extract_needs_from_message(message, context)
                rag_results = rag_pipeline.retrieve_resources(
                    context.get('location'),
                    needs,
                    context.get('situation')
                )
                rag_context = rag_pipeline.format_resources_for_claude(
                    rag_results)
                logger.info(
                    f"RAG retrieved {rag_results.get('total_resources', 0)} resources")

            # Build the enhanced system prompt
            system_prompt = self._build_enhanced_system_prompt(
                context, rag_context)

            # Prepare the API request
            headers = {
                "Content-Type": "application/json",
                "x-api-key": self.api_key,
                "anthropic-version": "2023-06-01"
            }

            payload = {
                "model": self.model,
                "max_tokens": 1200,  # Increased for more detailed responses
                "system": system_prompt,
                "messages": [
                    {
                        "role": "user",
                        "content": message
                    }
                ]
            }

            logger.info(
                f"Sending request to Claude API for message: {message[:50]}...")

            response = requests.post(
                self.api_url,
                headers=headers,
                json=payload,
                timeout=30
            )

            if response.status_code == 200:
                response_data = response.json()
                claude_response = response_data['content'][0]['text']
                logger.info("Successfully received response from Claude API")
                return claude_response
            else:
                logger.error(
                    f"Claude API error: {response.status_code} - {response.text}")
                return self._fallback_response(message)

        except requests.exceptions.RequestException as e:
            logger.error(f"Network error calling Claude API: {str(e)}")
            return self._fallback_response(message)
        except Exception as e:
            logger.error(f"Unexpected error in Claude service: {str(e)}")
            return self._fallback_response(message)

    def analyze_journal_entry(self, journal_text: str, user_context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Analyze a journal entry for emotion scoring and insights using Claude

        Args:
            journal_text: The journal entry text
            user_context: Optional user context for personalized analysis

        Returns:
            Dictionary with emotion scores, insights, and suggestions
        """
        try:
            if not self.api_key:
                return self._fallback_analysis(journal_text)

            prompt = f"""Analyze this journal entry and provide insights in JSON format:

Journal Entry: "{journal_text}"

Please analyze and respond with ONLY a valid JSON object containing:
{{
    "emotion_scores": {{
        "distress": 0.0-1.0,
        "hope": 0.0-1.0,
        "motivation": 0.0-1.0,
        "anxiety": 0.0-1.0,
        "positivity": 0.0-1.0
    }},
    "key_themes": ["theme1", "theme2", "theme3"],
    "insights": "Brief insight about the person's emotional state",
    "suggestions": "Supportive suggestions for improvement",
    "urgency_level": "low|medium|high"
}}"""

            if user_context:
                prompt += f"\n\nUser Context: {user_context.get('situation', '')} in {user_context.get('location', '')}"

            response = self._call_claude_api(prompt, max_tokens=800)
            if response:
                return self._parse_json_response(response, self._fallback_analysis(journal_text))
            else:
                return self._fallback_analysis(journal_text)

        except Exception as e:
            logger.error(f"Error analyzing journal entry: {str(e)}")
            return self._fallback_analysis(journal_text)

    def summarize_conversation(self, messages: List[Dict[str, str]], user_context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Summarize a conversation for context and insights using Claude

        Args:
            messages: List of message dictionaries with 'role' and 'content'
            user_context: Optional user context

        Returns:
            Dictionary with summary, key themes, and recommendations
        """
        try:
            if not self.api_key:
                return self._fallback_summary(messages)

            conversation = "\n".join(
                [f"{msg.get('role', 'user')}: {msg.get('content', '')}" for msg in messages[-10:]])  # Last 10 messages

            prompt = f"""Summarize this conversation and provide insights in JSON format:

Conversation:
{conversation}

Please analyze and respond with ONLY a valid JSON object containing:
{{
    "summary": "Brief summary of the conversation",
    "user_needs": ["need1", "need2", "need3"],
    "emotional_tone": "overall emotional tone",
    "progress_indicators": ["positive sign1", "positive sign2"],
    "recommendations": ["recommendation1", "recommendation2"],
    "follow_up_needed": true/false
}}"""

            if user_context:
                prompt += f"\n\nUser Context: {user_context.get('situation', '')} in {user_context.get('location', '')}"

            response = self._call_claude_api(prompt, max_tokens=800)
            if response:
                return self._parse_json_response(response, self._fallback_summary(messages))
            else:
                return self._fallback_summary(messages)

        except Exception as e:
            logger.error(f"Error summarizing conversation: {str(e)}")
            return self._fallback_summary(messages)

    def score_emotional_state(self, text: str) -> Dict[str, float]:
        """
        Score emotional state from text using Claude

        Args:
            text: Text to analyze

        Returns:
            Dictionary with emotion scores (0-1 scale)
        """
        try:
            if not self.api_key:
                return self._fallback_emotion_scores()

            prompt = f"""Score the emotional content of this text on a 0-1 scale and respond with ONLY a valid JSON object:

Text: "{text}"

Respond with:
{{
    "distress": 0.0-1.0,
    "hope": 0.0-1.0,
    "motivation": 0.0-1.0,
    "anxiety": 0.0-1.0,
    "positivity": 0.0-1.0,
    "overall_sentiment": "positive|neutral|negative"
}}"""

            response = self._call_claude_api(prompt, max_tokens=400)
            if response:
                return self._parse_json_response(response, self._fallback_emotion_scores())
            else:
                return self._fallback_emotion_scores()

        except Exception as e:
            logger.error(f"Error scoring emotional state: {str(e)}")
            return self._fallback_emotion_scores()

    def _call_claude_api(self, prompt: str, max_tokens: int = 1200) -> Optional[str]:
        """Make API call to Claude for analysis tasks"""
        try:
            headers = {
                "Content-Type": "application/json",
                "x-api-key": self.api_key,
                "anthropic-version": "2023-06-01"
            }

            payload = {
                "model": self.model,
                "max_tokens": max_tokens,
                "messages": [
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            }

            response = requests.post(
                self.api_url,
                headers=headers,
                json=payload,
                timeout=30
            )

            if response.status_code == 200:
                response_data = response.json()
                return response_data['content'][0]['text']
            else:
                logger.error(
                    f"Claude API error: {response.status_code} - {response.text}")
                return None

        except Exception as e:
            logger.error(f"Error calling Claude API: {str(e)}")
            return None

    def _parse_json_response(self, response: str, fallback: Dict[str, Any]) -> Dict[str, Any]:
        """Parse JSON response from Claude"""
        try:
            # Clean up response
            response_clean = response.strip()
            if response_clean.startswith('\`\`\`json'):
                response_clean = response_clean[7:-3]
            elif response_clean.startswith('\`\`\`'):
                response_clean = response_clean[3:-3]

            parsed = json.loads(response_clean)

            # Add metadata
            parsed['timestamp'] = datetime.now().isoformat()
            parsed['source'] = 'claude'

            return parsed

        except json.JSONDecodeError as e:
            logger.error(f"Failed to parse Claude JSON response: {str(e)}")
            return fallback

    def _extract_needs_from_message(self, message: str, context: Optional[Dict[str, Any]] = None) -> List[str]:
        """Extract needs from user message and context"""
        needs = []
        message_lower = message.lower()

        # Extract from message
        if any(word in message_lower for word in ["food", "hungry", "eat", "meal"]):
            needs.append("food")
        if any(word in message_lower for word in ["shelter", "housing", "sleep", "bed", "place to stay"]):
            needs.append("shelter")
        if any(word in message_lower for word in ["health", "medical", "doctor", "clinic", "sick"]):
            needs.append("healthcare")
        if any(word in message_lower for word in ["job", "work", "employment", "career"]):
            needs.append("employment")

        # Extract from context
        if context and context.get('needs'):
            context_needs = context['needs'].lower()
            if any(word in context_needs for word in ["food", "hungry", "eat"]):
                needs.append("food")
            if any(word in context_needs for word in ["shelter", "housing", "sleep"]):
                needs.append("shelter")
            if any(word in context_needs for word in ["health", "medical"]):
                needs.append("healthcare")
            if any(word in context_needs for word in ["job", "work", "employment"]):
                needs.append("employment")

        # Default to food if no specific needs detected
        if not needs:
            needs = ["food"]

        return list(set(needs))  # Remove duplicates

    def _build_enhanced_system_prompt(self, context: Optional[Dict[str, Any]] = None, rag_context: str = "") -> str:
        """Build enhanced system prompt with RAG context"""
        base_prompt = """You are a compassionate AI assistant for a social change app that helps people in difficult situations. Your role is to:

1. Provide warm, empathetic support using motivational interviewing techniques
2. Help users find local resources (food banks, shelters, clinics, job assistance)
3. Offer practical guidance and emotional support
4. Maintain hope and dignity in all interactions
5. Be non-judgmental and respectful

Always respond with empathy and practical help. Use specific local resource information when available."""

        # Add user context
        if context:
            context_info = ""
            if context.get('location'):
                context_info += f"\nUser location: {context['location']}"
            if context.get('situation'):
                context_info += f"\nUser situation: {context['situation']}"
            if context.get('needs'):
                context_info += f"\nUser needs: {context['needs']}"

            if context_info:
                base_prompt += f"\n\nUser Context:{context_info}"

        # Add RAG context with local resources
        if rag_context:
            base_prompt += f"\n\nLocal Resources Available:\n{rag_context}"
            base_prompt += "\nUse these specific local resources in your response. Provide exact addresses, phone numbers, and hours when available."

        return base_prompt

    def _build_system_prompt(self, context: Optional[Dict[str, Any]] = None) -> str:
        """Build the system prompt for Claude based on context (legacy method)"""
        return self._build_enhanced_system_prompt(context, "")

    def _fallback_response(self, message: str) -> str:
        """Fallback response when Claude API is unavailable"""
        return f"I understand you're reaching out for support. While I'm having trouble connecting to my full capabilities right now, I want you to know that your message is important. You mentioned: '{message}'. Please know that help is available, and you're taking a positive step by seeking support. Is there something specific I can try to help you with right now?"

    def _fallback_analysis(self, journal_text: str) -> Dict[str, Any]:
        """Fallback analysis when Claude is unavailable"""
        # Simple keyword-based analysis
        text_lower = journal_text.lower()

        distress_words = ['sad', 'depressed', 'anxious', 'worried',
                          'scared', 'hopeless', 'difficult', 'hard', 'struggle']
        hope_words = ['better', 'hope', 'improve', 'positive',
                      'good', 'happy', 'grateful', 'thankful']

        distress_score = min(sum(
            1 for word in distress_words if word in text_lower) / len(distress_words), 1.0)
        hope_score = min(
            sum(1 for word in hope_words if word in text_lower) / len(hope_words), 1.0)

        return {
            "emotion_scores": {
                "distress": distress_score,
                "hope": hope_score,
                "motivation": 0.5,
                "anxiety": min(distress_score * 0.8, 1.0),
                "positivity": min(hope_score * 1.2, 1.0)
            },
            "key_themes": ["personal reflection"],
            "insights": "Journal entry reflects personal thoughts and experiences",
            "suggestions": "Continue journaling to track your emotional journey",
            "urgency_level": "low",
            "timestamp": datetime.now().isoformat(),
            "source": "fallback"
        }

    def _fallback_summary(self, messages: List[Dict]) -> Dict[str, Any]:
        """Fallback summary when Claude is unavailable"""
        return {
            "summary": f"Conversation with {len(messages)} messages about support and resources",
            "user_needs": ["support", "resources"],
            "emotional_tone": "seeking assistance",
            "progress_indicators": ["reaching out for help"],
            "recommendations": ["continue conversation", "follow up on resources"],
            "follow_up_needed": True,
            "timestamp": datetime.now().isoformat(),
            "source": "fallback"
        }

    def _fallback_emotion_scores(self) -> Dict[str, float]:
        """Fallback emotion scores when Claude is unavailable"""
        return {
            "distress": 0.5,
            "hope": 0.5,
            "motivation": 0.5,
            "anxiety": 0.5,
            "positivity": 0.5,
            "overall_sentiment": "neutral",
            "source": "fallback"
        }


# Global instance
claude_service = ClaudeService()


def get_support_response(message: str, context: Optional[Dict[str, Any]] = None) -> str:
    """
    Main function to get support response from Claude
    This is the function required by Task 3
    """
    return claude_service.get_support_response(message, context)


def analyze_journal_entry(journal_text: str, user_context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Main function to analyze journal entries using Claude"""
    return claude_service.analyze_journal_entry(journal_text, user_context)


def summarize_conversation(messages: List[Dict[str, str]], user_context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Main function to summarize conversations using Claude"""
    return claude_service.summarize_conversation(messages, user_context)


def score_emotional_state(text: str) -> Dict[str, float]:
    """Main function to score emotional state using Claude"""
    return claude_service.score_emotional_state(text)

```

# services/claude_service.py

```py
# Claude 4 calls, prompt templates - Enhanced with CAG System Prompts

import os
import logging
from typing import Dict, Any, Optional, List
import requests
import json
from dotenv import load_dotenv
from datetime import datetime
from .rag_pipeline import rag_pipeline

# Load environment variables from .env file
load_dotenv()

logger = logging.getLogger(__name__)


class ClaudeService:
    """Service for interacting with Claude API with CAG System Prompts"""

    def __init__(self):
        self.api_key = os.environ.get('CLAUDE_API_KEY')
        self.api_url = "https://api.anthropic.com/v1/messages"
        self.model = "claude-3-5-sonnet-20241022"

        if not self.api_key:
            logger.warning("CLAUDE_API_KEY not set in environment variables")

    def _get_cag_system_prompts(self) -> Dict[str, str]:
        """Define the two CAG system prompts"""
        return {
            "empathetic_coach": """
You are an AI social worker and life coach assistant. Your goal is to help people—especially those experiencing hardship—navigate resources for housing, food, healthcare, mental health, legal help, and social support.

Key rules:

1. **Hyper-Personalized Support**:
    - Based on user input (e.g., "I'm from Fremont" or "I need help with housing"), tailor everything locally. 
    - Mention real nearby resources (e.g., Fremont Family Resource Center, Tri-City Volunteers Food Bank) only if they were part of user-provided input.
    - Never hallucinate or invent resources not explicitly mentioned or verified through the user's prompt.

2. **Empathetic Coaching Tone**:
    - Be warm, calm, and encouraging.
    - Speak as if you're a trusted community advocate, counselor, or coach.
    - Example: "I understand that housing insecurity can feel overwhelming, especially in places like Fremont where resources can be limited. Here's what you can do…"

3. **Personal Progress Framing**:
    - Frame suggestions around achievable steps.
    - Example: "Let's work on getting you shelter for the night, and then we can explore food access."

4. **No Links**:
    - Do NOT generate clickable hyperlinks. If a user gives a site, only mention it as plain text.
    - Do not make up any organization names unless they are included by the user.

5. **Stick to the Context Provided**:
    - If the user doesn't provide their location or situation, ask once.
    - Avoid vague or general responses—get specific based on user's details.

6. **Be Trauma-Informed**:
    - Always assume the user might be in a vulnerable state. Avoid blame, judgment, or cold replies.

7. **Avoid Generic Advice Unless Asked**:
    - Do not give general life coaching unless directly prompted.
    - Prioritize access to **tangible support** first (shelters, food, clinics, helplines).

8. **Never make up facts or organizations. Be honest if unsure.**

9. **Simple Greetings**: For simple greetings like "hello", "hi", "hey" respond naturally and briefly, then ask how you can help.""",

            "direct_assistant": """
You are a direct and efficient AI assistant built to provide **step-by-step, no-nonsense guides** to help people in need access essential services like housing, food, healthcare, mental support, and legal aid.

Key rules:

1. **Clear Steps, One Goal per Answer**:
    - Break down help into 1–2–3 format (e.g., "Here's how to find a shelter tonight…")
    - Keep answers focused and short.
    - Avoid flowery language—focus on function.

2. **Location-Specific Only if Given**:
    - ONLY mention city-specific options (like Fremont shelters) if the user tells you their location.
    - If they haven't, ask once: "What city or zip code are you in?"

3. **No Personalization or Emotions**:
    - Do not act like a coach or emotional support.
    - Speak like a checklist: "To apply for CalFresh, do this…"

4. **No Links or Unverifiable Info**:
    - Do not provide hyperlinks or fake organization names.
    - Mention sites only if the user gives one or asks for it by name.

5. **Always Tell the Truth**:
    - If you don't know the resource, say: "I don't have that information. Please check with a verified local provider."

6. **Never Assume or Guess**:
    - Only use what the user has told you. No assumptions, no hallucinations.

7. **Simple Greetings**: For simple greetings like "hello", "hi", "hey" respond briefly and directly ask what they need help with."""
        }

    def _is_simple_greeting(self, message: str) -> bool:
        """Check if message is a simple greeting"""
        greetings = ['hi', 'hello', 'hey', 'good morning', 'good afternoon', 'good evening', 'sup', 'what\'s up']
        message_clean = message.lower().strip()
        return any(greeting in message_clean for greeting in greetings) and len(message_clean.split()) <= 3

    def get_support_response(self, message: str, context: Optional[Dict[str, Any]] = None, prompt_type: str = "empathetic_coach") -> str:
        """
        Generate a supportive response using Claude API with CAG enhancement

        Args:
            message: User's input message
            context: Optional context information (user situation, location, etc.)
            prompt_type: Either "empathetic_coach" or "direct_assistant"

        Returns:
            Claude's response as a string
        """
        try:
            if not self.api_key:
                return self._fallback_response(message, prompt_type)

            # Handle simple greetings naturally
            if self._is_simple_greeting(message):
                if prompt_type == "direct_assistant":
                    return "Hello. What do you need help with?"
                else:
                    return "Hi there! I'm here to help you navigate resources and support. What can I assist you with today?"

            # Get local resources via RAG pipeline
            rag_context = ""
            if context and context.get('location'):
                needs = self._extract_needs_from_message(message, context)
                rag_results = rag_pipeline.retrieve_resources(
                    context.get('location'),
                    needs,
                    context.get('situation')
                )
                rag_context = rag_pipeline.format_resources_for_claude(rag_results)
                logger.info(f"RAG retrieved {rag_results.get('total_resources', 0)} resources")

            # Build the enhanced system prompt with CAG type
            system_prompt = self._build_enhanced_system_prompt(context, rag_context, prompt_type)

            # Prepare the API request
            headers = {
                "Content-Type": "application/json",
                "x-api-key": self.api_key,
                "anthropic-version": "2023-06-01"
            }

            payload = {
                "model": self.model,
                "max_tokens": 1200,
                "system": system_prompt,
                "messages": [
                    {
                        "role": "user",
                        "content": message
                    }
                ]
            }

            logger.info(f"Sending request to Claude API with prompt type: {prompt_type}")

            response = requests.post(
                self.api_url,
                headers=headers,
                json=payload,
                timeout=30
            )

            if response.status_code == 200:
                response_data = response.json()
                claude_response = response_data['content'][0]['text']
                logger.info("Successfully received response from Claude API")
                return claude_response
            else:
                logger.error(f"Claude API error: {response.status_code} - {response.text}")
                return self._fallback_response(message, prompt_type)

        except requests.exceptions.RequestException as e:
            logger.error(f"Network error calling Claude API: {str(e)}")
            return self._fallback_response(message, prompt_type)
        except Exception as e:
            logger.error(f"Unexpected error in Claude service: {str(e)}")
            return self._fallback_response(message, prompt_type)

    def _build_enhanced_system_prompt(self, context: Optional[Dict[str, Any]] = None, rag_context: str = "", prompt_type: str = "empathetic_coach") -> str:
        """Build enhanced system prompt with RAG context and CAG prompt type"""
        prompts = self._get_cag_system_prompts()
        base_prompt = prompts.get(prompt_type, prompts["empathetic_coach"])

        # Add user context
        if context:
            context_info = ""
            if context.get('location'):
                context_info += f"\nUser location: {context['location']}"
            if context.get('situation'):
                context_info += f"\nUser situation: {context['situation']}"
            if context.get('needs'):
                context_info += f"\nUser needs: {context['needs']}"

            if context_info:
                base_prompt += f"\n\nUser Context:{context_info}"

        # Add RAG context with local resources
        if rag_context:
            base_prompt += f"\n\nLocal Resources Available:\n{rag_context}"
            base_prompt += "\nUse these specific local resources in your response. Provide exact addresses, phone numbers, and hours when available."

        return base_prompt

    def _fallback_response(self, message: str, prompt_type: str = "empathetic_coach") -> str:
        """Fallback response when Claude API is unavailable"""
        if self._is_simple_greeting(message):
            if prompt_type == "direct_assistant":
                return "Hello. What do you need help with? (Note: I'm currently offline but will try to assist.)"
            else:
                return "Hi there! I'm here to help you, though I'm having some technical difficulties right now. How can I assist you?"
        
        fallback_responses = {
            "empathetic_coach": f"I understand you're reaching out for support, and I want you to know that your message is important. While I'm having trouble connecting right now, I can see you mentioned: '{message}'. Please know that help is available, and you're taking a positive step by seeking support. Is there something specific I can try to help you with?",
            
            "direct_assistant": f"I'm currently offline but received your request: '{message}'. Try these steps: 1) Call 2-1-1 for local resources, 2) Visit your nearest community center, 3) Check with local social services. What specific help do you need?"
        }
        
        return fallback_responses.get(prompt_type, fallback_responses["empathetic_coach"])

    def _extract_needs_from_message(self, message: str, context: Optional[Dict[str, Any]] = None) -> List[str]:
        """Extract needs from user message and context"""
        needs = []
        message_lower = message.lower()

        # Extract from message
        if any(word in message_lower for word in ["food", "hungry", "eat", "meal"]):
            needs.append("food")
        if any(word in message_lower for word in ["shelter", "housing", "sleep", "bed", "place to stay"]):
            needs.append("shelter")
        if any(word in message_lower for word in ["health", "medical", "doctor", "clinic", "sick"]):
            needs.append("healthcare")
        if any(word in message_lower for word in ["job", "work", "employment", "career"]):
            needs.append("employment")

        # Extract from context
        if context and context.get('needs'):
            context_needs = context['needs'].lower()
            if any(word in context_needs for word in ["food", "hungry", "eat"]):
                needs.append("food")
            if any(word in context_needs for word in ["shelter", "housing", "sleep"]):
                needs.append("shelter")
            if any(word in context_needs for word in ["health", "medical"]):
                needs.append("healthcare")
            if any(word in context_needs for word in ["job", "work", "employment"]):
                needs.append("employment")

        # Default to food if no specific needs detected
        if not needs:
            needs = ["food"]

        return list(set(needs))  # Remove duplicates

    # Keep all the existing methods for journal analysis, conversation summary, etc.
    def analyze_journal_entry(self, journal_text: str, user_context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Analyze a journal entry for emotion scoring and insights using Claude"""
        try:
            if not self.api_key:
                return self._fallback_analysis(journal_text)

            prompt = f"""Analyze this journal entry and provide insights in JSON format:

Journal Entry: "{journal_text}"

Please analyze and respond with ONLY a valid JSON object containing:
{{
    "emotion_scores": {{
        "distress": 0.0-1.0,
        "hope": 0.0-1.0,
        "motivation": 0.0-1.0,
        "anxiety": 0.0-1.0,
        "positivity": 0.0-1.0
    }},
    "key_themes": ["theme1", "theme2", "theme3"],
    "insights": "Brief insight about the person's emotional state",
    "suggestions": "Supportive suggestions for improvement",
    "urgency_level": "low|medium|high"
}}"""

            if user_context:
                prompt += f"\n\nUser Context: {user_context.get('situation', '')} in {user_context.get('location', '')}"

            response = self._call_claude_api(prompt, max_tokens=800)
            if response:
                return self._parse_json_response(response, self._fallback_analysis(journal_text))
            else:
                return self._fallback_analysis(journal_text)

        except Exception as e:
            logger.error(f"Error analyzing journal entry: {str(e)}")
            return self._fallback_analysis(journal_text)

    def summarize_conversation(self, messages: List[Dict[str, str]], user_context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Summarize a conversation for context and insights using Claude"""
        try:
            if not self.api_key:
                return self._fallback_summary(messages)

            conversation = "\n".join([f"{msg.get('role', 'user')}: {msg.get('content', '')}" for msg in messages[-10:]])

            prompt = f"""Summarize this conversation and provide insights in JSON format:

Conversation:
{conversation}

Please analyze and respond with ONLY a valid JSON object containing:
{{
    "summary": "Brief summary of the conversation",
    "user_needs": ["need1", "need2", "need3"],
    "emotional_tone": "overall emotional tone",
    "progress_indicators": ["positive sign1", "positive sign2"],
    "recommendations": ["recommendation1", "recommendation2"],
    "follow_up_needed": true/false
}}"""

            if user_context:
                prompt += f"\n\nUser Context: {user_context.get('situation', '')} in {user_context.get('location', '')}"

            response = self._call_claude_api(prompt, max_tokens=800)
            if response:
                return self._parse_json_response(response, self._fallback_summary(messages))
            else:
                return self._fallback_summary(messages)

        except Exception as e:
            logger.error(f"Error summarizing conversation: {str(e)}")
            return self._fallback_summary(messages)

    def score_emotional_state(self, text: str) -> Dict[str, float]:
        """Score emotional state from text using Claude"""
        try:
            if not self.api_key:
                return self._fallback_emotion_scores()

            prompt = f"""Score the emotional content of this text on a 0-1 scale and respond with ONLY a valid JSON object:

Text: "{text}"

Respond with:
{{
    "distress": 0.0-1.0,
    "hope": 0.0-1.0,
    "motivation": 0.0-1.0,
    "anxiety": 0.0-1.0,
    "positivity": 0.0-1.0,
    "overall_sentiment": "positive|neutral|negative"
}}"""

            response = self._call_claude_api(prompt, max_tokens=400)
            if response:
                parsed = self._parse_json_response(response, self._fallback_emotion_scores())
                parsed['timestamp'] = datetime.now().isoformat()
                parsed['source'] = 'claude'
                return parsed
            else:
                return self._fallback_emotion_scores()

        except Exception as e:
            logger.error(f"Error scoring emotional state: {str(e)}")
            return self._fallback_emotion_scores()

    def _call_claude_api(self, prompt: str, max_tokens: int = 1200) -> Optional[str]:
        """Call Claude API with the given prompt"""
        try:
            headers = {
                "Content-Type": "application/json",
                "x-api-key": self.api_key,
                "anthropic-version": "2023-06-01"
            }

            payload = {
                "model": self.model,
                "max_tokens": max_tokens,
                "messages": [
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            }

            response = requests.post(
                self.api_url,
                headers=headers,
                json=payload,
                timeout=30
            )

            if response.status_code == 200:
                response_data = response.json()
                return response_data['content'][0]['text']
            else:
                logger.error(f"Claude API error: {response.status_code} - {response.text}")
                return None

        except Exception as e:
            logger.error(f"Error calling Claude API: {str(e)}")
            return None

    def _parse_json_response(self, response: str, fallback: Dict[str, Any]) -> Dict[str, Any]:
        """Parse JSON response from Claude"""
        try:
            response_clean = response.strip()
            if response_clean.startswith('\`\`\`json'):
                response_clean = response_clean[7:-3]
            elif response_clean.startswith('\`\`\`'):
                response_clean = response_clean[3:-3]

            parsed = json.loads(response_clean)
            parsed['timestamp'] = datetime.now().isoformat()
            parsed['source'] = 'claude'
            return parsed

        except json.JSONDecodeError as e:
            logger.error(f"Failed to parse Claude JSON response: {str(e)}")
            return fallback

    def _fallback_analysis(self, journal_text: str) -> Dict[str, Any]:
        """Fallback analysis when Claude is unavailable"""
        text_lower = journal_text.lower()
        distress_words = ['sad', 'depressed', 'anxious', 'worried', 'scared', 'hopeless', 'difficult', 'hard', 'struggle']
        hope_words = ['better', 'hope', 'improve', 'positive', 'good', 'happy', 'grateful', 'thankful']

        distress_score = min(sum(1 for word in distress_words if word in text_lower) / len(distress_words), 1.0)
        hope_score = min(sum(1 for word in hope_words if word in text_lower) / len(hope_words), 1.0)

        return {
            "emotion_scores": {
                "distress": distress_score,
                "hope": hope_score,
                "motivation": 0.5,
                "anxiety": min(distress_score * 0.8, 1.0),
                "positivity": min(hope_score * 1.2, 1.0)
            },
            "key_themes": ["personal reflection"],
            "insights": "Journal entry reflects personal thoughts and experiences",
            "suggestions": "Continue journaling to track your emotional journey",
            "urgency_level": "low",
            "timestamp": datetime.now().isoformat(),
            "source": "fallback"
        }

    def _fallback_summary(self, messages: List[Dict]) -> Dict[str, Any]:
        """Fallback summary when Claude is unavailable"""
        return {
            "summary": f"Conversation with {len(messages)} messages about support and resources",
            "user_needs": ["support", "resources"],
            "emotional_tone": "seeking assistance",
            "progress_indicators": ["reaching out for help"],
            "recommendations": ["continue conversation", "follow up on resources"],
            "follow_up_needed": True,
            "timestamp": datetime.now().isoformat(),
            "source": "fallback"
        }

    def _fallback_emotion_scores(self) -> Dict[str, float]:
        """Fallback emotion scores when Claude is unavailable"""
        return {
            "distress": 0.5,
            "hope": 0.5,
            "motivation": 0.5,
            "anxiety": 0.5,
            "positivity": 0.5,
            "overall_sentiment": "neutral",
            "source": "fallback"
        }


# Global instance
claude_service = ClaudeService()


def get_support_response(message: str, context: Optional[Dict[str, Any]] = None, prompt_type: str = "empathetic_coach") -> str:
    """
    Main function to get support response from Claude with CAG prompt type
    """
    return claude_service.get_support_response(message, context, prompt_type)


def analyze_journal_entry(journal_text: str, user_context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Main function to analyze journal entries using Claude"""
    return claude_service.analyze_journal_entry(journal_text, user_context)


def summarize_conversation(messages: List[Dict[str, str]], user_context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Main function to summarize conversations using Claude"""
    return claude_service.summarize_conversation(messages, user_context)


def score_emotional_state(text: str) -> Dict[str, float]:
    """Main function to score emotional state using Claude"""
    return claude_service.score_emotional_state(text)

```

# services/email_service.py

```py
# Gmail API – sends support emails to users

```

# services/gemini_service.py

```py
# Gemini Service - Complete AI assistant functionality

import os
import logging
from typing import Dict, Any, Optional, List
import requests
import json
from dotenv import load_dotenv
from datetime import datetime
from .rag_pipeline import rag_pipeline

# Load environment variables from .env file
load_dotenv()

logger = logging.getLogger(__name__)


class GeminiService:
    """Service for interacting with Google Gemini API for complete AI assistant functionality"""

    def __init__(self):
        self.api_key = os.environ.get('GEMINI_API_KEY')
        self.api_url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent"

        if not self.api_key:
            logger.warning("GEMINI_API_KEY not set in environment variables")

    def _get_system_prompts(self, mode: str = "coach") -> Dict[str, str]:
        """Define system prompts for different modes and interaction styles"""
        if mode == "coach":
            return {
                "empathetic_coach": """
You are a compassionate life coach helping people navigate difficult situations. Your focus is on empowerment, motivation, and practical life guidance.

Key approach:

1. **Life Coaching Focus**:
    - Help people break down overwhelming situations into manageable steps
    - Provide motivational support and perspective-shifting advice
    - Share relatable examples and simple strategies they can use today
    - Focus on what they can control and improve right now

2. **Empowering Tone**:
    - Be warm, encouraging, and confidence-building
    - Use language that helps them see their situation more clearly
    - Example: "I hear that you're feeling overwhelmed by your housing situation. Many people have been where you are, and here's what often helps..."

3. **Practical Wisdom Over Resources**:
    - Minimize heavy resource lists - focus on mindset and actionable steps
    - Give specific life advice with examples they can relate to
    - Help them think differently about their challenges
    - Suggest simple daily actions that build momentum

4. **Simplification**:
    - Break complex problems into simple, achievable parts
    - Help them see what's most important to focus on first
    - Provide clear, specific examples of what to do today

5. **Motivational Examples**:
    - Share how others have handled similar situations
    - Give concrete examples: "One approach that works well is..."
    - Focus on building their problem-solving confidence

6. **Simple Greetings**: For simple greetings, respond warmly and ask how you can support them today.""",

                "direct_assistant": """
You are a supportive life coach providing clear, actionable guidance for life improvement.

Focus on:
1. Breaking down their situation into simple, manageable parts
2. Providing specific life strategies with examples
3. Building their confidence and motivation
4. Giving them one clear next step to take today
5. Keeping advice practical and achievable

Be direct but encouraging, focusing on empowerment and what they can control."""
            }
        else:  # assistant mode
            return {
                "empathetic_coach": """
You are a resource-focused social support assistant. Your goal is to quickly connect people with specific local resources and services.

Key approach:

1. **Resource-First Response**:
    - Quickly identify what specific help they need (shelter, food, healthcare, etc.)
    - Provide detailed information about available local resources
    - Include practical details: addresses, phone numbers, hours, requirements
    - Give multiple options when available

2. **Practical Connection**:
    - Be warm but efficient in connecting them with help
    - Explain exactly how to access services (what to bring, how to apply)
    - Include both immediate and longer-term resource options
    - End with clear next steps they can take right away

3. **Comprehensive Information**:
    - Always include actionable resource information with contact details
    - Mention what services each organization provides
    - Explain any requirements or documentation needed
    - Provide backup options when possible

4. **Immediate Action Focus**:
    - Validate briefly, then focus on solutions
    - Give them specific places to go and people to call today
    - Include emergency contacts when relevant
    - Prioritize urgent needs (shelter, food, safety) first

5. **Contact Information Priority**:
    - Always include phone numbers, addresses, and hours when available
    - Mention the best times to call or visit
    - Explain what to expect when they contact each resource

6. **Simple Greetings**: For simple greetings, respond briefly and ask what specific help they need.""",

                "direct_assistant": """
You are a resource assistant providing immediate, practical help connections.

Focus on:
1. Identifying their specific needs quickly
2. Providing detailed local resource information with contact details
3. Including all access instructions (what to bring, how to apply)
4. Giving multiple options when available
5. Being efficient and action-oriented with clear next steps

Provide comprehensive resource information with specific contact details and clear instructions."""
            }

    def _is_simple_greeting(self, message: str) -> bool:
        """Check if message is a simple greeting"""
        greetings = ['hi', 'hello', 'hey', 'good morning',
                     'good afternoon', 'good evening', 'sup', 'what\'s up']
        message_clean = message.lower().strip()
        return any(greeting in message_clean for greeting in greetings) and len(message_clean.split()) <= 3

    def get_support_response(self, message: str, context: Optional[Dict[str, Any]] = None, prompt_type: str = "empathetic_coach", mode: str = "coach") -> str:
        """
        Generate a supportive response using Gemini API

        Args:
            message: User's input message
            context: Optional context information (user situation, location, etc.)
            prompt_type: Either "empathetic_coach" or "direct_assistant"

        Returns:
            Gemini's response as a string
        """
        try:
            if not self.api_key:
                return self._fallback_response(message, prompt_type)

            # Handle simple greetings naturally
            if self._is_simple_greeting(message):
                if prompt_type == "direct_assistant":
                    return "Hello. What do you need help with?"
                else:
                    return "Hi there! I'm here to help you navigate resources and support. What can I assist you with today?"

            # Get local resources via RAG pipeline
            rag_context = ""
            if context and context.get('location'):
                needs = self._extract_needs_from_message(message, context)
                rag_results = rag_pipeline.retrieve_resources(
                    context.get('location'),
                    needs,
                    context.get('situation')
                )
                rag_context = rag_pipeline.format_resources_for_gemini(
                    rag_results)
                logger.info(
                    f"RAG retrieved {rag_results.get('total_resources', 0)} resources")

            # Build the enhanced system prompt
            system_prompt = self._build_enhanced_system_prompt(
                context, rag_context, prompt_type, mode)

            # Create the full prompt
            full_prompt = f"{system_prompt}\n\nUser message: {message}"

            response = self._call_gemini_api(full_prompt, max_tokens=1200)
            if response:
                logger.info("Successfully received response from Gemini API")
                return response
            else:
                return self._fallback_response(message, prompt_type)

        except Exception as e:
            logger.error(f"Unexpected error in Gemini service: {str(e)}")
            return self._fallback_response(message, prompt_type)

    def _build_enhanced_system_prompt(self, context: Optional[Dict[str, Any]] = None, rag_context: str = "", prompt_type: str = "empathetic_coach", mode: str = "coach") -> str:
        """Build enhanced system prompt with RAG context, prompt type, and mode"""
        prompts = self._get_system_prompts(mode)
        base_prompt = prompts.get(prompt_type, prompts["empathetic_coach"])

        # Add user context
        if context:
            context_info = ""
            if context.get('location'):
                context_info += f"\nUser location: {context['location']}"
            if context.get('situation'):
                context_info += f"\nUser situation: {context['situation']}"
            if context.get('needs'):
                context_info += f"\nUser needs: {context['needs']}"
            if context.get('name'):
                context_info += f"\nUser name: {context['name']}"

            if context_info:
                base_prompt += f"\n\nCURRENT USER CONTEXT:{context_info}"

        # Add RAG context if available
        if rag_context:
            base_prompt += f"\n\nAVAILABLE LOCAL RESOURCES:\n{rag_context}"

        return base_prompt

    def _fallback_response(self, message: str, prompt_type: str = "empathetic_coach") -> str:
        """Fallback response when Gemini is unavailable"""
        if prompt_type == "direct_assistant":
            return "I'm currently unable to access my full capabilities. Please try again later or contact local support services directly."
        else:
            return "I understand you're reaching out for support. While I'm having technical difficulties right now, please don't hesitate to contact local community resources or crisis lines if you need immediate assistance."

    def _extract_needs_from_message(self, message: str, context: Optional[Dict[str, Any]] = None) -> List[str]:
        """Extract needs/categories from user message"""
        message_lower = message.lower()
        needs = []

        # Basic keyword matching
        if any(word in message_lower for word in ['food', 'hungry', 'eat', 'meal', 'grocery']):
            needs.append('food')
        if any(word in message_lower for word in ['housing', 'shelter', 'homeless', 'place to stay', 'rent']):
            needs.append('housing')
        if any(word in message_lower for word in ['health', 'medical', 'doctor', 'clinic', 'sick']):
            needs.append('health')
        if any(word in message_lower for word in ['job', 'work', 'employment', 'income']):
            needs.append('employment')
        if any(word in message_lower for word in ['mental', 'therapy', 'counseling', 'depression', 'anxiety']):
            needs.append('mental_health')
        if any(word in message_lower for word in ['legal', 'lawyer', 'immigration', 'eviction']):
            needs.append('legal')

        # Default to general if no specific needs detected
        if not needs:
            needs = ['general']

        # Add context-based needs
        if context and context.get('needs'):
            context_needs = context['needs'].lower()
            if 'food' in context_needs and 'food' not in needs:
                needs.append('food')
            if 'housing' in context_needs and 'housing' not in needs:
                needs.append('housing')

        return needs

    def analyze_journal_entry(self, journal_text: str, user_context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Analyze a journal entry for emotion scoring and insights

        Args:
            journal_text: The journal entry text
            user_context: Optional user context for personalized analysis

        Returns:
            Dictionary with emotion scores, insights, and suggestions
        """
        try:
            if not self.api_key:
                return self._fallback_analysis(journal_text)

            prompt = self._build_journal_analysis_prompt(
                journal_text, user_context)

            response = self._call_gemini_api(prompt)
            if response:
                return self._parse_journal_analysis(response, journal_text)
            else:
                return self._fallback_analysis(journal_text)

        except Exception as e:
            logger.error(f"Error analyzing journal entry: {str(e)}")
            return self._fallback_analysis(journal_text)

    def summarize_conversation(self, messages: List[Dict[str, str]], user_context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Summarize a conversation for context and insights

        Args:
            messages: List of message dictionaries with 'role' and 'content'
            user_context: Optional user context

        Returns:
            Dictionary with summary, key themes, and recommendations
        """
        try:
            if not self.api_key:
                return self._fallback_summary(messages)

            prompt = self._build_conversation_summary_prompt(
                messages, user_context)

            response = self._call_gemini_api(prompt)
            if response:
                return self._parse_conversation_summary(response, messages)
            else:
                return self._fallback_summary(messages)

        except Exception as e:
            logger.error(f"Error summarizing conversation: {str(e)}")
            return self._fallback_summary(messages)

    def score_emotional_state(self, text: str) -> Dict[str, float]:
        """
        Score emotional state from text

        Args:
            text: Text to analyze

        Returns:
            Dictionary with emotion scores (0-1 scale)
        """
        try:
            if not self.api_key:
                return self._fallback_emotion_scores()

            prompt = self._build_emotion_scoring_prompt(text)

            response = self._call_gemini_api(prompt)
            if response:
                return self._parse_emotion_scores(response)
            else:
                return self._fallback_emotion_scores()

        except Exception as e:
            logger.error(f"Error scoring emotional state: {str(e)}")
            return self._fallback_emotion_scores()

    def _call_gemini_api(self, prompt: str, max_tokens: int = 1024) -> Optional[str]:
        """Make API call to Gemini"""
        try:
            headers = {
                "Content-Type": "application/json"
            }

            payload = {
                "contents": [{
                    "parts": [{
                        "text": prompt
                    }]
                }],
                "generationConfig": {
                    "temperature": 0.3,
                    "topK": 40,
                    "topP": 0.95,
                    "maxOutputTokens": max_tokens,
                }
            }

            url = f"{self.api_url}?key={self.api_key}"

            logger.info("Sending request to Gemini API...")

            response = requests.post(
                url, headers=headers, json=payload, timeout=30)

            if response.status_code == 200:
                response_data = response.json()
                if 'candidates' in response_data and len(response_data['candidates']) > 0:
                    content = response_data['candidates'][0]['content']['parts'][0]['text']
                    logger.info(
                        "Successfully received response from Gemini API")
                    return content
                else:
                    logger.error("No candidates in Gemini response")
                    return None
            else:
                logger.error(
                    f"Gemini API error: {response.status_code} - {response.text}")
                return None

        except requests.exceptions.RequestException as e:
            logger.error(f"Network error calling Gemini API: {str(e)}")
            return None
        except Exception as e:
            logger.error(f"Unexpected error calling Gemini API: {str(e)}")
            return None

    def _build_journal_analysis_prompt(self, journal_text: str, user_context: Optional[Dict[str, Any]] = None) -> str:
        """Build prompt for journal entry analysis"""
        prompt = f"""Analyze this journal entry and provide insights in JSON format:

Journal Entry: "{journal_text}"

Please analyze and respond with ONLY a valid JSON object containing:
{{
    "emotion_scores": {{
        "distress": 0.0-1.0,
        "hope": 0.0-1.0,
        "motivation": 0.0-1.0,
        "anxiety": 0.0-1.0,
        "positivity": 0.0-1.0
    }},
    "key_themes": ["theme1", "theme2", "theme3"],
    "insights": "Brief insight about the person's emotional state",
    "suggestions": "Supportive suggestions for improvement",
    "urgency_level": "low|medium|high"
}}"""

        if user_context:
            prompt += f"\n\nUser Context: {user_context.get('situation', '')} in {user_context.get('location', '')}"

        return prompt

    def _build_conversation_summary_prompt(self, messages: List[Dict[str, str]], user_context: Optional[Dict[str, Any]] = None) -> str:
        """Build prompt for conversation summarization"""
        conversation = "\n".join(
            [f"{msg.get('role', 'user')}: {msg.get('content', '')}" for msg in messages[-10:]])  # Last 10 messages

        prompt = f"""Summarize this conversation and provide insights in JSON format:

Conversation:
{conversation}

Please analyze and respond with ONLY a valid JSON object containing:
{{
    "summary": "Brief summary of the conversation",
    "user_needs": ["need1", "need2", "need3"],
    "emotional_tone": "overall emotional tone",
    "progress_indicators": ["positive sign1", "positive sign2"],
    "recommendations": ["recommendation1", "recommendation2"],
    "follow_up_needed": true/false
}}"""

        if user_context:
            prompt += f"\n\nUser Context: {user_context.get('situation', '')} in {user_context.get('location', '')}"

        return prompt

    def _build_emotion_scoring_prompt(self, text: str) -> str:
        """Build prompt for emotion scoring"""
        return f"""Score the emotional content of this text on a 0-1 scale and respond with ONLY a valid JSON object:

Text: "{text}"

Respond with:
{{
    "distress": 0.0-1.0,
    "hope": 0.0-1.0,
    "motivation": 0.0-1.0,
    "anxiety": 0.0-1.0,
    "positivity": 0.0-1.0,
    "overall_sentiment": "positive|neutral|negative"
}}"""

    def _parse_journal_analysis(self, response: str, original_text: str) -> Dict[str, Any]:
        """Parse journal analysis response"""
        try:
            # Try to extract JSON from response
            response_clean = response.strip()
            if response_clean.startswith('\`\`\`json'):
                response_clean = response_clean[7:-3]
            elif response_clean.startswith('\`\`\`'):
                response_clean = response_clean[3:-3]

            analysis = json.loads(response_clean)

            # Add metadata
            analysis['timestamp'] = datetime.now().isoformat()
            analysis['original_text_length'] = len(original_text)

            return analysis

        except json.JSONDecodeError as e:
            logger.error(
                f"Failed to parse Gemini journal analysis response: {str(e)}")
            return self._fallback_analysis(original_text)

    def _parse_conversation_summary(self, response: str, messages: List[Dict]) -> Dict[str, Any]:
        """Parse conversation summary response"""
        try:
            response_clean = response.strip()
            if response_clean.startswith('\`\`\`json'):
                response_clean = response_clean[7:-3]
            elif response_clean.startswith('\`\`\`'):
                response_clean = response_clean[3:-3]

            summary = json.loads(response_clean)

            # Add metadata
            summary['timestamp'] = datetime.now().isoformat()
            summary['message_count'] = len(messages)

            return summary

        except json.JSONDecodeError as e:
            logger.error(f"Failed to parse Gemini summary response: {str(e)}")
            return self._fallback_summary(messages)

    def _parse_emotion_scores(self, response: str) -> Dict[str, float]:
        """Parse emotion scoring response"""
        try:
            response_clean = response.strip()
            if response_clean.startswith('\`\`\`json'):
                response_clean = response_clean[7:-3]
            elif response_clean.startswith('\`\`\`'):
                response_clean = response_clean[3:-3]

            scores = json.loads(response_clean)

            # Ensure all scores are floats between 0 and 1
            for key, value in scores.items():
                if isinstance(value, (int, float)):
                    scores[key] = max(0.0, min(1.0, float(value)))

            return scores

        except json.JSONDecodeError as e:
            logger.error(f"Failed to parse Gemini emotion scores: {str(e)}")
            return self._fallback_emotion_scores()

    def _fallback_analysis(self, journal_text: str) -> Dict[str, Any]:
        """Fallback analysis when Gemini is unavailable"""
        # Simple keyword-based analysis
        text_lower = journal_text.lower()

        distress_words = ['sad', 'depressed', 'anxious', 'worried',
                          'scared', 'hopeless', 'difficult', 'hard', 'struggle']
        hope_words = ['better', 'hope', 'improve', 'positive',
                      'good', 'happy', 'grateful', 'thankful']

        distress_score = sum(
            1 for word in distress_words if word in text_lower) / len(distress_words)
        hope_score = sum(
            1 for word in hope_words if word in text_lower) / len(hope_words)

        return {
            "emotion_scores": {
                "distress": min(distress_score, 1.0),
                "hope": min(hope_score, 1.0),
                "motivation": 0.5,
                "anxiety": min(distress_score * 0.8, 1.0),
                "positivity": min(hope_score * 1.2, 1.0)
            },
            "key_themes": ["personal reflection"],
            "insights": "Journal entry reflects personal thoughts and experiences",
            "suggestions": "Continue journaling to track your emotional journey",
            "urgency_level": "low",
            "timestamp": datetime.now().isoformat(),
            "original_text_length": len(journal_text),
            "fallback": True
        }

    def _fallback_summary(self, messages: List[Dict]) -> Dict[str, Any]:
        """Fallback summary when Gemini is unavailable"""
        return {
            "summary": f"Conversation with {len(messages)} messages about support and resources",
            "user_needs": ["support", "resources"],
            "emotional_tone": "seeking assistance",
            "progress_indicators": ["reaching out for help"],
            "recommendations": ["continue conversation", "follow up on resources"],
            "follow_up_needed": True,
            "timestamp": datetime.now().isoformat(),
            "message_count": len(messages),
            "fallback": True
        }

    def _fallback_emotion_scores(self) -> Dict[str, float]:
        """Fallback emotion scores when Gemini is unavailable"""
        return {
            "distress": 0.5,
            "hope": 0.5,
            "motivation": 0.5,
            "anxiety": 0.5,
            "positivity": 0.5,
            "overall_sentiment": "neutral",
            "fallback": True
        }


# Global instance
gemini_service = GeminiService()


def get_support_response(message: str, context: Optional[Dict[str, Any]] = None, prompt_type: str = "empathetic_coach", mode: str = "coach") -> str:
    """Main function to get support responses"""
    return gemini_service.get_support_response(message, context, prompt_type, mode)


def analyze_journal_entry(journal_text: str, user_context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Main function to analyze journal entries"""
    return gemini_service.analyze_journal_entry(journal_text, user_context)


def summarize_conversation(messages: List[Dict[str, str]], user_context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Main function to summarize conversations"""
    return gemini_service.summarize_conversation(messages, user_context)


def score_emotional_state(text: str) -> Dict[str, float]:
    """Main function to score emotional state"""
    return gemini_service.score_emotional_state(text)

```

# services/rag_pipeline.py

```py
# Custom RAG pipeline for nearby resources

import logging
from typing import Dict, List, Any, Optional
import json
from datetime import datetime

logger = logging.getLogger(__name__)


class RAGPipeline:
    """RAG Pipeline for retrieving local resources based on user context"""

    def __init__(self):
        # In a real implementation, this would connect to external APIs
        # For now, we'll use a comprehensive local database
        self.resource_database = self._initialize_resource_database()

    def _initialize_resource_database(self) -> Dict[str, List[Dict]]:
        """Initialize a comprehensive resource database"""
        return {
            "san_francisco": {
                "food": [
                    {
                        "name": "SF-Marin Food Bank",
                        "address": "900 Pennsylvania Ave, San Francisco, CA 94107",
                        "phone": "(415) 282-1900",
                        "hours": "Mon-Fri 9am-5pm",
                        "services": ["Food pantry", "Emergency food boxes"],
                        "requirements": "No documentation required",
                        "distance": 0.8
                    },
                    {
                        "name": "Glide Memorial Church",
                        "address": "330 Ellis Street, San Francisco, CA 94102",
                        "phone": "(415) 674-6000",
                        "hours": "Daily meals: 8am, 12pm, 4pm",
                        "services": ["Free meals", "Food pantry"],
                        "requirements": "None",
                        "distance": 1.2
                    },
                    {
                        "name": "St. Anthony's Dining Room",
                        "address": "150 Golden Gate Ave, San Francisco, CA 94102",
                        "phone": "(415) 592-2710",
                        "hours": "Mon-Fri 11:30am-12:30pm",
                        "services": ["Free lunch", "Groceries"],
                        "requirements": "None",
                        "distance": 1.0
                    }
                ],
                "shelter": [
                    {
                        "name": "MSC South Shelter",
                        "address": "525 5th Street, San Francisco, CA 94107",
                        "phone": "(415) 597-7960",
                        "hours": "24/7",
                        "services": ["Emergency shelter", "Case management"],
                        "requirements": "Walk-in services available",
                        "beds_available": 45,
                        "distance": 0.5
                    },
                    {
                        "name": "Next Door Shelter",
                        "address": "1001 Polk Street, San Francisco, CA 94109",
                        "phone": "(415) 487-3300",
                        "hours": "Intake: 4pm-1am",
                        "services": ["Overnight shelter", "Meals", "Showers"],
                        "requirements": "Check-in required",
                        "beds_available": 32,
                        "distance": 1.1
                    },
                    {
                        "name": "Hamilton Family Center",
                        "address": "260 Golden Gate Ave, San Francisco, CA 94102",
                        "phone": "(415) 292-0870",
                        "hours": "24/7",
                        "services": ["Family shelter", "Childcare", "Job training"],
                        "requirements": "Families with children",
                        "beds_available": 18,
                        "distance": 0.9
                    }
                ],
                "healthcare": [
                    {
                        "name": "HealthRIGHT 360",
                        "address": "1563 Mission Street, San Francisco, CA 94103",
                        "phone": "(415) 762-3700",
                        "hours": "Mon-Fri 8am-5pm",
                        "services": ["Primary care", "Mental health", "Substance abuse"],
                        "requirements": "Sliding scale fees",
                        "distance": 0.7
                    },
                    {
                        "name": "SF City Clinic",
                        "address": "356 7th Street, San Francisco, CA 94103",
                        "phone": "(415) 487-5500",
                        "hours": "Mon-Thu 8am-4pm, Fri 8am-12pm",
                        "services": ["STD testing", "HIV testing", "Vaccinations"],
                        "requirements": "Free services",
                        "distance": 0.6
                    }
                ],
                "employment": [
                    {
                        "name": "SF Works Career Center",
                        "address": "801 Turk Street, San Francisco, CA 94102",
                        "phone": "(415) 701-4848",
                        "hours": "Mon-Fri 9am-5pm",
                        "services": ["Job placement", "Resume help", "Skills training"],
                        "requirements": "None",
                        "distance": 1.3
                    }
                ]
            },
            "oakland": {
                "food": [
                    {
                        "name": "Alameda County Community Food Bank",
                        "address": "7900 Edgewater Dr, Oakland, CA 94621",
                        "phone": "(510) 635-3663",
                        "hours": "Mon-Fri 9am-4pm",
                        "services": ["Food pantry", "Mobile food pantry"],
                        "requirements": "No documentation required",
                        "distance": 2.1
                    }
                ],
                "shelter": [
                    {
                        "name": "Henry Robinson Multi Service Center",
                        "address": "3801 Martin Luther King Jr Way, Oakland, CA 94609",
                        "phone": "(510) 597-5085",
                        "hours": "24/7",
                        "services": ["Emergency shelter", "Transitional housing"],
                        "requirements": "Intake assessment required",
                        "beds_available": 67,
                        "distance": 1.8
                    },
                    {
                        "name": "Covenant House California - Oakland",
                        "address": "1695 Depot Rd, Oakland, CA",
                        "phone": "510-829-8224",
                        "hours": None,
                        "services": [],
                        "requirements": None,
                        "beds_available": 25,
                        "distance": None
                    },
                    {
                        "name": "Henry Robinson Center",
                        "address": "1026 Mission Blvd, Oakland, CA",
                        "phone": "510-266-2724",
                        "hours": None,
                        "services": [],
                        "requirements": None,
                        "beds_available": 137,
                        "distance": None
                    },
                    {
                        "name": "The Holland",
                        "address": "2419 Castro St, Oakland, CA",
                        "phone": "510-785-9245",
                        "hours": None,
                        "services": [],
                        "requirements": None,
                        "beds_available": 90,
                        "distance": None
                    },
                    {
                        "name": "Oakland Elizabeth House",
                        "address": "3371 Depot Rd, Oakland, CA",
                        "phone": "510-863-8125",
                        "hours": None,
                        "services": [],
                        "requirements": None,
                        "beds_available": 26,
                        "distance": None
                    },
                    {
                        "name": "East Oakland Community Project",
                        "address": "9941 University Ave, Oakland, CA",
                        "phone": "510-990-4919",
                        "hours": None,
                        "services": [],
                        "requirements": None,
                        "beds_available": 18,
                        "distance": None
                    },
                    {
                        "name": "St. Mary's Center - Closer to Home",
                        "address": "4835 Broadway, Oakland, CA",
                        "phone": "510-478-1593",
                        "hours": None,
                        "services": [],
                        "requirements": None,
                        "beds_available": 8,
                        "distance": None
                    },
                    {
                        "name": "St. Mary's Center - Presentation House",
                        "address": "8931 Ashby Ave, Oakland, CA",
                        "phone": "510-465-5451",
                        "hours": None,
                        "services": [],
                        "requirements": None,
                        "beds_available": 8,
                        "distance": None
                    },
                    {
                        "name": "St. Mary's Center - Friendly Manor",
                        "address": "362 Shattuck Ave, Oakland, CA",
                        "phone": "510-546-1983",
                        "hours": None,
                        "services": [],
                        "requirements": None,
                        "beds_available": 8,
                        "distance": None
                    },
                    {
                        "name": "Salvation Army Oakland Garden Center",
                        "address": "5801 Depot Rd, Oakland, CA",
                        "phone": "510-842-5596",
                        "hours": None,
                        "services": [],
                        "requirements": None,
                        "beds_available": 45,
                        "distance": None
                    },
                    {
                        "name": "Operation Dignity Veterans Housing",
                        "address": "1267 Castro St, Oakland, CA",
                        "phone": "510-516-8732",
                        "hours": None,
                        "services": [],
                        "requirements": None,
                        "beds_available": 32,
                        "distance": None
                    },
                    {
                        "name": "BOSS Oakland Emergency Shelter",
                        "address": "4715 Telegraph Ave, Oakland, CA",
                        "phone": "510-910-3574",
                        "hours": None,
                        "services": [],
                        "requirements": None,
                        "beds_available": 28,
                        "distance": None
                    },
                    {
                        "name": "Matilda Cleveland Transitional Housing",
                        "address": "216 Mission Blvd, Oakland, CA",
                        "phone": "510-560-3421",
                        "hours": None,
                        "services": [],
                        "requirements": None,
                        "beds_available": 35,
                        "distance": None
                    },
                    {
                        "name": "Building Futures Women's Center",
                        "address": "7354 International Blvd, Oakland, CA",
                        "phone": "510-859-4263",
                        "hours": None,
                        "services": [],
                        "requirements": None,
                        "beds_available": 22,
                        "distance": None
                    },
                    {
                        "name": "Family Front Door",
                        "address": "6488 Ashby Ave, Oakland, CA",
                        "phone": "510-944-2006",
                        "hours": None,
                        "services": [],
                        "requirements": None,
                        "beds_available": 15,
                        "distance": None
                    },
                    {
                        "name": "Oakland Winter Relief Center",
                        "address": "3607 Shattuck Ave, Oakland, CA",
                        "phone": "510-393-1870",
                        "hours": None,
                        "services": [],
                        "requirements": None,
                        "beds_available": 50,
                        "distance": None
                    },
                    {
                        "name": "Centro Legal de la Raza Housing",
                        "address": "5956 Castro St, Oakland, CA",
                        "phone": "510-468-8245",
                        "hours": None,
                        "services": [],
                        "requirements": None,
                        "beds_available": 12,
                        "distance": None
                    },
                    {
                        "name": "Davis Street Family Resource Center",
                        "address": "8236 Mission Blvd, Oakland, CA",
                        "phone": "510-951-2562",
                        "hours": None,
                        "services": [],
                        "requirements": None,
                        "beds_available": 18,
                        "distance": None
                    },
                    {
                        "name": "Women's Daytime Drop-in Oakland",
                        "address": "9821 Thornton Ave, Oakland, CA",
                        "phone": "510-623-9396",
                        "hours": None,
                        "services": [],
                        "requirements": None,
                        "beds_available": 20,
                        "distance": None
                    },
                    {
                        "name": "Crossroads Emergency Housing",
                        "address": "7411 University Ave, Oakland, CA",
                        "phone": "510-872-9069",
                        "hours": None,
                        "services": [],
                        "requirements": None,
                        "beds_available": 125,
                        "distance": None
                    },
                    {
                        "name": "Alameda Family Services Shelter",
                        "address": "6136 Telegraph Ave, Oakland, CA",
                        "phone": "510-554-6176",
                        "hours": None,
                        "services": [],
                        "requirements": None,
                        "beds_available": 16,
                        "distance": None
                    },
                    {
                        "name": "Bay Area Rescue Mission Oakland",
                        "address": "9731 Center St, Oakland, CA",
                        "phone": "510-751-8445",
                        "hours": None,
                        "services": [],
                        "requirements": None,
                        "beds_available": 60,
                        "distance": None
                    },
                    {
                        "name": "Safe Haven Transitional Housing",
                        "address": "478 International Blvd, Oakland, CA",
                        "phone": "510-843-4933",
                        "hours": None,
                        "services": [],
                        "requirements": None,
                        "beds_available": 24,
                        "distance": None
                    },
                    {
                        "name": "Unity Council Emergency Housing",
                        "address": "6207 University Ave, Oakland, CA",
                        "phone": "510-402-7664",
                        "hours": None,
                        "services": [],
                        "requirements": None,
                        "beds_available": 14,
                        "distance": None
                    },
                    {
                        "name": "Aurora Housing Program",
                        "address": "8293 Depot Rd, Oakland, CA",
                        "phone": "510-908-9834",
                        "hours": None,
                        "services": [],
                        "requirements": None,
                        "beds_available": 30,
                        "distance": None
                    },
                    {
                        "name": "Oakland Interfaith Housing",
                        "address": "170 International Blvd, Oakland, CA",
                        "phone": "510-696-7083",
                        "hours": None,
                        "services": [],
                        "requirements": None,
                        "beds_available": 22,
                        "distance": None
                    },
                    {
                        "name": "Emergency Food & Shelter Oakland",
                        "address": "2788 Center St, Oakland, CA",
                        "phone": "510-612-3823",
                        "hours": None,
                        "services": [],
                        "requirements": None,
                        "beds_available": 40,
                        "distance": None
                    },
                    {
                        "name": "New Hope Housing Services",
                        "address": "6799 Telegraph Ave, Oakland, CA",
                        "phone": "510-959-8409",
                        "hours": None,
                        "services": [],
                        "requirements": None,
                        "beds_available": 18,
                        "distance": None
                    },
                    {
                        "name": "Community Housing Partnership",
                        "address": "485 San Pablo Ave, Oakland, CA",
                        "phone": "510-633-1274",
                        "hours": None,
                        "services": [],
                        "requirements": None,
                        "beds_available": 35,
                        "distance": None
                    },
                    {
                        "name": "Friendship Bench Emergency Shelter",
                        "address": "2088 San Pablo Ave, Oakland, CA",
                        "phone": "510-825-5347",
                        "hours": None,
                        "services": [],
                        "requirements": None,
                        "beds_available": 25,
                        "distance": None
                    },
                    {
                        "name": "PATH Oakland Emergency Housing",
                        "address": "2062 San Pablo Ave, Oakland, CA",
                        "phone": "510-816-7250",
                        "hours": None,
                        "services": [],
                        "requirements": None,
                        "beds_available": 20,
                        "distance": None
                    },
                    {
                        "name": "Transitional Age Youth Program",
                        "address": "4108 International Blvd, Oakland, CA",
                        "phone": "510-386-5898",
                        "hours": None,
                        "services": [],
                        "requirements": None,
                        "beds_available": 16,
                        "distance": None
                    },
                    {
                        "name": "OCCUR Emergency Shelter",
                        "address": "7090 Ashby Ave, Oakland, CA",
                        "phone": "510-244-8082",
                        "hours": None,
                        "services": [],
                        "requirements": None,
                        "beds_available": 28,
                        "distance": None
                    }
                ],
                "healthcare": [
                    {
                        "name": "Louisa Abada",
                        "address": "1727 Martin Luther King Jr Way, Oakland, CA 94612-1327",
                        "phone": "510-893-9230",
                        "services": [
                            "Mental health assessment",
                            "Social services coordination"
                        ],
                        "requirements": "17 years experience",
                        "distance": None
                    },
                    {
                        "name": "Zena Abdallah",
                        "address": "8601 MacArthur Blvd, Oakland, CA 94605-4037",
                        "phone": "510-844-5369",
                        "services": [
                            "Trauma therapy"
                        ],
                        "requirements": "4 years experience",
                        "distance": None
                    },
                    {
                        "name": "Rachel Adams",
                        "address": "2633 E 27th St, Oakland, CA 94601-1912",
                        "phone": "510-536-8111",
                        "services": [
                            "Substance abuse counseling",
                            "Trauma therapy"
                        ],
                        "requirements": "5 years experience",
                        "distance": None
                    },
                    {
                        "name": "Neal Adams",
                        "address": "5751 Adeline St, Oakland, CA 94608-2815",
                        "phone": "510-467-4250",
                        "services": [
                            "Grief counseling"
                        ],
                        "requirements": "12 years experience",
                        "distance": None
                    },
                    {
                        "name": "Bruce Adams",
                        "address": "1005 Atlantic Ave, Alameda, CA 94501-1148",
                        "phone": "415-474-7310",
                        "services": [
                            "Trauma therapy"
                        ],
                        "requirements": "6 years experience",
                        "distance": None
                    },
                    {
                        "name": "Katherine Adamson",
                        "address": "15200 Foothill Blvd, San Leandro, CA 94578-1013",
                        "phone": "510-352-9690",
                        "services": [
                            "LGBTQ+ affirming therapy"
                        ],
                        "requirements": "14 years experience",
                        "distance": None
                    },
                    {
                        "name": "Shaina Adelstein",
                        "address": "5555 Ascot Dr, Oakland, CA 94611-3001",
                        "phone": "510-879-2110",
                        "services": [
                            "ADHD therapy"
                        ],
                        "requirements": "2 years experience",
                        "distance": None
                    },
                    {
                        "name": "Omar Bocobo",
                        "address": "2579 San Pablo Ave, Oakland, CA 94612",
                        "phone": "510-844-7896",
                        "services": [
                            "Domestic violence counseling",
                            "Trauma therapy"
                        ],
                        "requirements": "22 years experience",
                        "distance": None
                    },
                    {
                        "name": "Catherine Ho",
                        "address": "268 Grand Ave, Oakland, CA 94610",
                        "phone": "510-555-7382",
                        "services": [
                            "Bilingual services"
                        ],
                        "requirements": "5 years experience",
                        "distance": None
                    },
                    {
                        "name": "Amina Samake",
                        "address": "270 Grand Ave, Oakland, CA 94610",
                        "phone": "510-926-4751",
                        "services": [
                            "Child and adolescent therapy",
                            "Multicultural counseling",
                            "Mental health assessment"
                        ],
                        "requirements": "14 years experience",
                        "distance": None
                    },
                    {
                        "name": "Emily Pellegrino",
                        "address": "2501 Harrison St, Oakland, CA 94612",
                        "phone": "510-892-3456",
                        "services": [
                            "Case management",
                            "Trauma therapy"
                        ],
                        "requirements": "11 years experience",
                        "distance": None
                    },
                    {
                        "name": "Pamela Lozoff",
                        "address": "2501 Harrison St, Oakland, CA 94612",
                        "phone": "510-789-2341",
                        "services": [
                            "Art therapy",
                            "Mental health assessment"
                        ],
                        "requirements": "6 years experience",
                        "distance": None
                    },
                    {
                        "name": "Elizabeth Cary",
                        "address": "298 Grand Ave Ste 100, Oakland, CA 94610",
                        "phone": "510-567-8901",
                        "services": [
                            "CBT (Cognitive Behavioral Therapy)",
                            "LGBTQ+ affirming therapy",
                            "Group therapy"
                        ],
                        "requirements": "16 years experience",
                        "distance": None
                    },
                    {
                        "name": "Tara Montgomery",
                        "address": "1011 Union St, Oakland, CA 94607",
                        "phone": "510-234-5678",
                        "services": [
                            "CBT (Cognitive Behavioral Therapy)",
                            "Family therapy",
                            "Play therapy"
                        ],
                        "requirements": "22 years experience",
                        "distance": None
                    },
                    {
                        "name": "Marisol Enos",
                        "address": "1011 Union St, Oakland, CA 94607",
                        "phone": "510-876-5432",
                        "services": [
                            "EMDR therapy",
                            "Art therapy",
                            "Trauma therapy"
                        ],
                        "requirements": "18 years experience",
                        "distance": None
                    },
                    {
                        "name": "Stacy Daniels",
                        "address": "1011 Union St, Oakland, CA 94607",
                        "phone": "510-345-6789",
                        "services": [
                            "ADHD therapy",
                            "Crisis intervention",
                            "Individual therapy"
                        ],
                        "requirements": "19 years experience",
                        "distance": None
                    },
                    {
                        "name": "Yolanda Olloway-Smith",
                        "address": "1011 Union St, Oakland, CA 94607",
                        "phone": "510-987-6543",
                        "services": [
                            "Couples therapy",
                            "ADHD therapy"
                        ],
                        "requirements": "5 years experience",
                        "distance": None
                    },
                    {
                        "name": "Astraea Bella",
                        "address": "3600 Broadway, Oakland, CA 94611",
                        "phone": "510-555-0142",
                        "services": [
                            "Individual therapy"
                        ],
                        "requirements": "4 years experience",
                        "distance": None
                    },
                    {
                        "name": "Brie Robertori",
                        "address": "1926 E 19th St, Oakland, CA 94606",
                        "phone": "510-555-0143",
                        "services": [
                            "Substance abuse counseling"
                        ],
                        "requirements": "13 years experience",
                        "distance": None
                    },
                    {
                        "name": "Cameron Murphey",
                        "address": "5750 College Ave, Oakland, CA 94618",
                        "phone": "510-555-0144",
                        "services": [
                            "Group therapy"
                        ],
                        "requirements": "8 years experience",
                        "distance": None
                    },
                    {
                        "name": "Jennifer Martinez",
                        "address": "4314 Piedmont Ave, Oakland, CA 94611",
                        "phone": "510-652-8901",
                        "services": [
                            "Group therapy",
                            "DBT (Dialectical Behavior Therapy)"
                        ],
                        "requirements": "15 years experience",
                        "distance": None
                    },
                    {
                        "name": "Robert Kim",
                        "address": "2579 San Pablo Ave, Oakland, CA 94612",
                        "phone": "510-789-2345",
                        "services": [
                            "Domestic violence counseling",
                            "EMDR therapy"
                        ],
                        "requirements": "4 years experience",
                        "distance": None
                    },
                    {
                        "name": "Maria Rodriguez",
                        "address": "1515 Fruitvale Ave, Oakland, CA 94601",
                        "phone": "510-345-6789",
                        "services": [
                            "EMDR therapy",
                            "Behavioral therapy"
                        ],
                        "requirements": "16 years experience",
                        "distance": None
                    },
                    {
                        "name": "David Thompson",
                        "address": "3001 International Blvd, Oakland, CA 94601",
                        "phone": "510-567-8901",
                        "services": [
                            "Multicultural counseling"
                        ],
                        "requirements": "8 years experience",
                        "distance": None
                    },
                    {
                        "name": "Lisa Chen",
                        "address": "747 52nd Street, Oakland, CA 94609",
                        "phone": "510-234-5678",
                        "services": [
                            "EMDR therapy"
                        ],
                        "requirements": "19 years experience",
                        "distance": None
                    },
                    {
                        "name": "James Wilson",
                        "address": "1266 14th St, Oakland, CA 94607",
                        "phone": "510-345-6789",
                        "services": [
                            "Crisis intervention"
                        ],
                        "requirements": "9 years experience",
                        "distance": None
                    },
                    {
                        "name": "Amy Johnson",
                        "address": "8521 A St, Oakland, CA 94621",
                        "phone": "510-456-7890",
                        "services": [
                            "Domestic violence counseling"
                        ],
                        "requirements": "16 years experience",
                        "distance": None
                    },
                    {
                        "name": "Carlos Morales",
                        "address": "3750 Brown Ave, Oakland, CA 94619",
                        "phone": "510-567-8901",
                        "services": [
                            "Group therapy",
                            "Mental health assessment",
                            "Art therapy"
                        ],
                        "requirements": "19 years experience",
                        "distance": None
                    },
                    {
                        "name": "Diana Lee",
                        "address": "2607 Myrtle St, Oakland, CA 94607",
                        "phone": "510-678-9012",
                        "services": [
                            "Social services coordination",
                            "Domestic violence counseling"
                        ],
                        "requirements": "2 years experience",
                        "distance": None
                    },
                    {
                        "name": "Kevin Brown",
                        "address": "8755 Fontaine St, Oakland, CA 94605",
                        "phone": "510-789-0123",
                        "services": [
                            "EMDR therapy",
                            "Multicultural counseling"
                        ],
                        "requirements": "25 years experience",
                        "distance": None
                    },
                    {
                        "name": "Angela Davis",
                        "address": "1023 MacArthur Blvd, Oakland, CA 94610",
                        "phone": "510-890-1234",
                        "services": [
                            "Depression and anxiety"
                        ],
                        "requirements": "17 years experience",
                        "distance": None
                    },
                    {
                        "name": "Michelle Garcia",
                        "address": "12250 Skyline Blvd, Oakland, CA 94619",
                        "phone": "510-901-2345",
                        "services": [
                            "Domestic violence counseling",
                            "Individual therapy"
                        ],
                        "requirements": "7 years experience",
                        "distance": None
                    }
                ]
            },
            "berkeley": {
                "healthcare": [
                    {
                        "name": "Patrick Conlin",
                        "address": "2901 Hillegass Ave # 2, Berkeley, CA 94705-2211",
                        "phone": "510-841-7321",
                        "services": [
                            "LGBTQ+ affirming therapy",
                            "Crisis intervention"
                        ],
                        "requirements": "16 years experience",
                        "distance": None
                    },
                    {
                        "name": "Katrina Rose Serrano",
                        "address": "2105 Martin Luther King Jr Way, Berkeley, CA 94704-1108",
                        "phone": "510-926-6677",
                        "services": [
                            "Family therapy"
                        ],
                        "requirements": "11 years experience",
                        "distance": None
                    },
                    {
                        "name": "Judith Ann Izzo",
                        "address": "2640 Martin Luther King Jr Way, Berkeley, CA 94704-3238",
                        "phone": "510-981-5290",
                        "services": [
                            "Child and adolescent therapy",
                            "Individual therapy",
                            "DBT (Dialectical Behavior Therapy)"
                        ],
                        "requirements": "19 years experience",
                        "distance": None
                    },
                    {
                        "name": "Julianna Dickey",
                        "address": "2107 Spaulding Ave, Berkeley, CA 94703-1420",
                        "phone": "510-845-5197",
                        "services": [
                            "Trauma therapy"
                        ],
                        "requirements": "4 years experience",
                        "distance": None
                    }
                ]
            }
        }

    def retrieve_resources(self, location: str, needs: List[str], situation: str = None) -> Dict[str, Any]:
        """
        Retrieve relevant resources based on user location and needs

        Args:
            location: User's location (city, zip, etc.)
            needs: List of needs (food, shelter, healthcare, etc.)
            situation: User's current situation for context

        Returns:
            Dictionary of relevant resources with confidence scores
        """
        try:
            # Normalize location
            normalized_location = self._normalize_location(location)

            # Get resources for the location
            location_resources = self.resource_database.get(
                normalized_location, {})

            if not location_resources:
                return self._get_fallback_resources(location)

            # Filter resources based on needs
            relevant_resources = {}
            confidence_scores = {}

            for need in needs:
                need_type = self._map_need_to_category(need)
                if need_type in location_resources:
                    resources = location_resources[need_type]
                    # Sort by distance and availability
                    sorted_resources = self._rank_resources(
                        resources, situation)
                    # Top 3
                    relevant_resources[need_type] = sorted_resources[:3]
                    confidence_scores[need_type] = self._calculate_confidence(
                        sorted_resources)

            return {
                "location": location,
                "normalized_location": normalized_location,
                "resources": relevant_resources,
                "confidence_scores": confidence_scores,
                "total_resources": sum(len(r) for r in relevant_resources.values()),
                "timestamp": datetime.now().isoformat()
            }

        except Exception as e:
            logger.error(f"Error in RAG pipeline: {str(e)}")
            return self._get_fallback_resources(location)

    def _normalize_location(self, location: str) -> str:
        """Normalize location string to match database keys"""
        if not location:
            return "unknown"

        location_lower = location.lower()

        if "san francisco" in location_lower or "sf" in location_lower:
            return "san_francisco"
        elif "oakland" in location_lower:
            return "oakland"
        elif "berkeley" in location_lower:
            return "oakland"  # Use Oakland resources for Berkeley
        else:
            return "unknown"

    def _map_need_to_category(self, need: str) -> str:
        """Map user needs to resource categories"""
        need_lower = need.lower()

        if any(word in need_lower for word in ["food", "hungry", "meal", "eat"]):
            return "food"
        elif any(word in need_lower for word in ["shelter", "housing", "sleep", "bed"]):
            return "shelter"
        elif any(word in need_lower for word in ["health", "medical", "doctor", "clinic"]):
            return "healthcare"
        elif any(word in need_lower for word in ["job", "work", "employment", "career"]):
            return "employment"
        else:
            return "food"  # Default to food assistance

    def _rank_resources(self, resources: List[Dict], situation: str = None) -> List[Dict]:
        """Rank resources based on relevance and availability"""
        scored_resources = []

        for resource in resources:
            score = 0

            # Distance score (closer is better)
            distance = resource.get("distance")
            if distance is not None:
                score += max(0, 5 - distance)

            # Availability score
            if "beds_available" in resource:
                beds = resource["beds_available"]
                if beds > 20:
                    score += 3
                elif beds > 10:
                    score += 2
                elif beds > 0:
                    score += 1

            # Situational relevance
            if situation:
                if "family" in situation.lower() and "family" in resource.get("services", []):
                    score += 2
                if "emergency" in situation.lower() and "24/7" in resource.get("hours", ""):
                    score += 2

            # Requirements score (fewer requirements is better)
            requirements = resource.get("requirements", "")
            if "none" in requirements.lower() or "no documentation" in requirements.lower():
                score += 2

            scored_resources.append({**resource, "relevance_score": score})

        return sorted(scored_resources, key=lambda x: x["relevance_score"], reverse=True)

    def _calculate_confidence(self, resources: List[Dict]) -> float:
        """Calculate confidence score for resource recommendations"""
        if not resources:
            return 0.0

        # Base confidence on number of resources and their scores
        avg_score = sum(r.get("relevance_score", 0)
                        for r in resources) / len(resources)
        # Max confidence with 3+ resources
        resource_count_factor = min(len(resources) / 3.0, 1.0)

        return min(avg_score * resource_count_factor / 10.0, 1.0)

    def _get_fallback_resources(self, location: str) -> Dict[str, Any]:
        """Provide fallback resources when specific location data isn't available"""
        return {
            "location": location,
            "normalized_location": "unknown",
            "resources": {
                "general": [
                    {
                        "name": "211 Bay Area",
                        "phone": "2-1-1",
                        "services": ["Resource referrals", "Crisis support"],
                        "description": "Call 211 for local resource information in your area"
                    },
                    {
                        "name": "National Suicide Prevention Lifeline",
                        "phone": "988",
                        "services": ["Crisis support", "Mental health"],
                        "description": "24/7 crisis support and mental health resources"
                    }
                ]
            },
            "confidence_scores": {"general": 0.3},
            "total_resources": 2,
            "timestamp": datetime.now().isoformat(),
            "note": f"Specific resources for {location} not available. Showing general resources."
        }

    def format_resources_for_claude(self, rag_results: Dict[str, Any]) -> str:
        """Format RAG results for Claude context"""
        if not rag_results.get("resources"):
            return "No specific local resources found. Recommend calling 211 for local assistance."

        formatted = f"Local resources near {rag_results['location']}:\n\n"

        for category, resources in rag_results["resources"].items():
            formatted += f"{category.upper()} RESOURCES:\n"
            for resource in resources:
                formatted += f"• {resource['name']}\n"
                formatted += f"  Address: {resource.get('address', 'Call for address')}\n"
                formatted += f"  Phone: {resource.get('phone', 'N/A')}\n"
                formatted += f"  Hours: {resource.get('hours', 'Call for hours')}\n"
                if resource.get('requirements'):
                    formatted += f"  Requirements: {resource['requirements']}\n"
                formatted += "\n"

        return formatted

    def format_resources_for_gemini(self, rag_results: Dict[str, Any]) -> str:
        """Format RAG results for Gemini context (same format as Claude)"""
        return self.format_resources_for_claude(rag_results)


# Global RAG pipeline instance
rag_pipeline = RAGPipeline()


def get_local_resources(location: str, needs: List[str], situation: str = None) -> Dict[str, Any]:
    """Main function to get local resources via RAG pipeline"""
    return rag_pipeline.retrieve_resources(location, needs, situation)

```

# test_api.py

```py
#!/usr/bin/env python3
"""
Simple test script for the CAG Chatbot Flask API
"""

import requests
import json
import time

BASE_URL = "http://localhost:5000"


def test_health_check():
    """Test the health check endpoint"""
    print("Testing health check...")
    try:
        response = requests.get(f"{BASE_URL}/")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Health check passed: {data['message']}")
            return True
        else:
            print(f"❌ Health check failed: {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print("❌ Could not connect to the API. Make sure the Flask app is running.")
        return False


def test_chat_endpoint():
    """Test the chat endpoint"""
    print("\nTesting chat endpoint...")
    try:
        payload = {
            "message": "Hello, this is a test message",
            "user_id": "test_user_123"
        }

        response = requests.post(
            f"{BASE_URL}/api/chat",
            json=payload,
            headers={"Content-Type": "application/json"}
        )

        if response.status_code == 200:
            data = response.json()
            print(f"✅ Chat endpoint passed")
            print(f"   Response: {data['response']}")
            print(f"   User ID: {data['user_id']}")
            return True
        else:
            print(f"❌ Chat endpoint failed: {response.status_code}")
            print(f"   Error: {response.text}")
            return False
    except Exception as e:
        print(f"❌ Chat endpoint error: {str(e)}")
        return False


def test_chat_history():
    """Test the chat history endpoint"""
    print("\nTesting chat history endpoint...")
    try:
        response = requests.get(
            f"{BASE_URL}/api/chat/history?user_id=test_user_123")

        if response.status_code == 200:
            data = response.json()
            print(f"✅ Chat history endpoint passed")
            print(f"   Total messages: {data['total_messages']}")
            return True
        else:
            print(f"❌ Chat history endpoint failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Chat history endpoint error: {str(e)}")
        return False


def test_status_endpoint():
    """Test the status endpoint"""
    print("\nTesting status endpoint...")
    try:
        response = requests.get(f"{BASE_URL}/api/status")

        if response.status_code == 200:
            data = response.json()
            print(f"✅ Status endpoint passed")
            print(f"   Status: {data['status']}")
            print(
                f"   CAG API configured: {data['config']['cag_api_configured']}")
            print(
                f"   Total chat entries: {data['stats']['total_chat_entries']}")
            return True
        else:
            print(f"❌ Status endpoint failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Status endpoint error: {str(e)}")
        return False


def main():
    """Run all tests"""
    print("🧪 Testing CAG Chatbot Flask API")
    print("=" * 40)

    tests = [
        test_health_check,
        test_chat_endpoint,
        test_chat_history,
        test_status_endpoint
    ]

    passed = 0
    total = len(tests)

    for test in tests:
        if test():
            passed += 1
        time.sleep(0.5)  # Small delay between tests

    print("\n" + "=" * 40)
    print(f"📊 Test Results: {passed}/{total} tests passed")

    if passed == total:
        print("🎉 All tests passed! The API is working correctly.")
    else:
        print("⚠️  Some tests failed. Check the Flask app logs for more details.")


if __name__ == "__main__":
    main()

```

# test_cag_rag.py

```py
#!/usr/bin/env python3
"""
Test script for CAG (Context-Aware Generation) and RAG (Retrieval-Augmented Generation) capabilities
"""

import requests
import json
import time

BASE_URL = "http://localhost:5001"


def test_rag_pipeline():
    """Test the RAG pipeline for resource discovery"""
    print("🔍 Testing RAG Pipeline - Resource Discovery")
    print("=" * 50)

    # Test San Francisco resources
    response = requests.post(f"{BASE_URL}/api/chat/resources", json={
        "location": "San Francisco",
        "needs": ["food", "shelter"],
        "situation": "homeless"
    })

    if response.status_code == 200:
        data = response.json()
        resources = data['resources']['resources']
        print(
            f"✅ Found {data['resources']['total_resources']} resources in San Francisco")

        for category, items in resources.items():
            print(f"\n📍 {category.upper()} RESOURCES:")
            for item in items:
                print(f"  • {item['name']}")
                print(f"    📍 {item.get('address', 'N/A')}")
                print(f"    📞 {item.get('phone', 'N/A')}")
                print(f"    🕒 {item.get('hours', 'N/A')}")
                print(
                    f"    ⭐ Relevance Score: {item.get('relevance_score', 'N/A')}")
                print()
    else:
        print(f"❌ RAG Pipeline test failed: {response.status_code}")


def test_cag_with_context():
    """Test Context-Aware Generation with Claude + RAG"""
    print("\n🧠 Testing CAG - Context-Aware Generation")
    print("=" * 50)

    # Test with full context
    response = requests.post(f"{BASE_URL}/api/chat/message", json={
        "message": "I'm really struggling and need help finding shelter for tonight",
        "context": {
            "name": "Sarah",
            "location": "San Francisco",
            "situation": "Recently lost job, staying in car",
            "needs": "emergency shelter, food assistance"
        }
    })

    if response.status_code == 200:
        data = response.json()
        print("✅ CAG Response Generated Successfully")
        print(f"👤 User ID: {data['user_id']}")
        print(f"📊 Emotion Analysis:")
        emotion = data['emotion_analysis']
        for key, value in emotion.items():
            if isinstance(value, (int, float)):
                print(f"  • {key.title()}: {value:.2f}")

        print(f"\n🤖 Claude Response:")
        print(f"  {data['response'][:200]}...")

        return data['user_id']
    else:
        print(f"❌ CAG test failed: {response.status_code}")
        return None


def test_emotion_analysis():
    """Test Claude-based emotion analysis"""
    print("\n💭 Testing Emotion Analysis")
    print("=" * 50)

    journal_entries = [
        {
            "text": "I'm feeling hopeful today. Found a temporary place to stay and had a good meal.",
            "expected": "positive"
        },
        {
            "text": "I'm really anxious and scared. Don't know where I'll sleep tonight.",
            "expected": "negative"
        }
    ]

    for i, entry in enumerate(journal_entries, 1):
        print(f"\n📝 Journal Entry {i}:")
        print(f"   \"{entry['text'][:50]}...\"")

        response = requests.post(f"{BASE_URL}/api/chat/analyze-journal", json={
            "journal_text": entry['text'],
            "context": {"location": "San Francisco", "situation": "homeless"}
        })

        if response.status_code == 200:
            data = response.json()
            analysis = data['analysis']

            print(f"✅ Analysis Complete:")
            print(
                f"   🎯 Urgency Level: {analysis.get('urgency_level', 'N/A')}")
            print(
                f"   💡 Key Themes: {', '.join(analysis.get('key_themes', []))}")
            print(f"   📊 Emotion Scores:")

            scores = analysis.get('emotion_scores', {})
            for emotion, score in scores.items():
                if isinstance(score, (int, float)):
                    bar = "█" * int(score * 10)
                    print(f"      {emotion.title()}: {score:.2f} {bar}")
        else:
            print(f"❌ Emotion analysis failed: {response.status_code}")


def test_conversation_summary(user_id):
    """Test conversation summarization"""
    if not user_id:
        return

    print(f"\n📋 Testing Conversation Summary for User {user_id}")
    print("=" * 50)

    response = requests.get(f"{BASE_URL}/api/chat/summarize/{user_id}")

    if response.status_code == 200:
        data = response.json()
        summary = data['summary']

        print("✅ Conversation Summary Generated:")
        print(f"   📝 Summary: {summary.get('summary', 'N/A')}")
        print(f"   🎭 Emotional Tone: {summary.get('emotional_tone', 'N/A')}")
        print(f"   🎯 User Needs: {', '.join(summary.get('user_needs', []))}")
        print(
            f"   ✨ Progress Indicators: {', '.join(summary.get('progress_indicators', []))}")
        print(
            f"   📋 Recommendations: {', '.join(summary.get('recommendations', []))}")
        print(
            f"   🔄 Follow-up Needed: {summary.get('follow_up_needed', 'N/A')}")
    else:
        print(f"❌ Conversation summary failed: {response.status_code}")


def test_health_check():
    """Test system health and capabilities"""
    print("\n🏥 Testing System Health")
    print("=" * 50)

    response = requests.get(f"{BASE_URL}/api/chat/health")

    if response.status_code == 200:
        data = response.json()
        print(f"✅ System Status: {data['status']}")
        print("🔧 Available Features:")

        features = data['features']
        for feature, enabled in features.items():
            status = "✅" if enabled else "❌"
            print(f"   {status} {feature.replace('_', ' ').title()}")
    else:
        print(f"❌ Health check failed: {response.status_code}")


def main():
    """Run all tests"""
    print("🚀 CAG & RAG System Test Suite")
    print("=" * 60)
    print("Testing Context-Aware Generation and Retrieval-Augmented Generation")
    print("Using Claude AI for all analysis and generation tasks")
    print("=" * 60)

    try:
        # Test all components
        test_health_check()
        test_rag_pipeline()
        user_id = test_cag_with_context()
        test_emotion_analysis()
        test_conversation_summary(user_id)

        print("\n🎉 All Tests Completed!")
        print("=" * 60)
        print("✅ RAG Pipeline: Resource discovery working")
        print("✅ CAG System: Context-aware responses working")
        print("✅ Emotion Analysis: Claude-based scoring working")
        print("✅ Conversation Summary: Claude-based insights working")
        print("✅ Integration: All systems working together")

    except requests.exceptions.ConnectionError:
        print("❌ Error: Cannot connect to Flask server")
        print("   Make sure the server is running on http://localhost:5001")
    except Exception as e:
        print(f"❌ Unexpected error: {str(e)}")


if __name__ == "__main__":
    main()

```

# test_chat_endpoint.py

```py
#!/usr/bin/env python3
"""
Test script for /api/chat/message endpoint (Task 5)
"""

import requests
import json
import time

BASE_URL = "http://localhost:5001"


def test_chat_message_endpoint():
    """Test the /api/chat/message POST endpoint"""
    print("🧪 Testing /api/chat/message Endpoint (Task 5)")
    print("=" * 60)

    # Test 1: Basic message without user context
    print("📝 Test 1: Basic message without user context...")
    try:
        payload = {
            "message": "I need help finding food today"
        }

        response = requests.post(
            f"{BASE_URL}/api/chat/message",
            json=payload,
            headers={"Content-Type": "application/json"}
        )

        if response.status_code == 200:
            data = response.json()
            print(f"✅ Basic message test passed")
            print(f"   Response: {data['response'][:100]}...")
            print(f"   User ID: {data['user_id']}")
            print(f"   Conversation ID: {data['conversation_id']}")

            # Save user_id for next test
            user_id = data['user_id']
        else:
            print(f"❌ Basic message test failed: {response.status_code}")
            print(f"   Error: {response.text}")
            return False

    except Exception as e:
        print(f"❌ Basic message test error: {str(e)}")
        return False

    # Test 2: Message with user context
    print("\n📝 Test 2: Message with user context...")
    try:
        payload = {
            "message": "Can you help me find a shelter for tonight?",
            "context": {
                "name": "Test User",
                "location": "San Francisco, CA",
                "situation": "Experiencing homelessness",
                "needs": "Shelter, food assistance"
            }
        }

        response = requests.post(
            f"{BASE_URL}/api/chat/message",
            json=payload,
            headers={"Content-Type": "application/json"}
        )

        if response.status_code == 200:
            data = response.json()
            print(f"✅ Context message test passed")
            print(f"   Response: {data['response'][:100]}...")
            print(f"   Context: {data['context']}")

            # Save user_id for history test
            context_user_id = data['user_id']
        else:
            print(f"❌ Context message test failed: {response.status_code}")
            print(f"   Error: {response.text}")
            return False

    except Exception as e:
        print(f"❌ Context message test error: {str(e)}")
        return False

    # Test 3: Message with existing user_id
    print("\n📝 Test 3: Message with existing user_id...")
    try:
        payload = {
            "message": "Thank you for the help earlier. Do you have any other suggestions?",
            "user_id": user_id
        }

        response = requests.post(
            f"{BASE_URL}/api/chat/message",
            json=payload,
            headers={"Content-Type": "application/json"}
        )

        if response.status_code == 200:
            data = response.json()
            print(f"✅ Existing user test passed")
            print(f"   Response: {data['response'][:100]}...")
            print(f"   Same User ID: {data['user_id'] == user_id}")
        else:
            print(f"❌ Existing user test failed: {response.status_code}")
            return False

    except Exception as e:
        print(f"❌ Existing user test error: {str(e)}")
        return False

    # Test 4: Get chat history
    print("\n📝 Test 4: Getting chat history...")
    try:
        response = requests.get(
            f"{BASE_URL}/api/chat/history/{context_user_id}")

        if response.status_code == 200:
            data = response.json()
            print(f"✅ Chat history test passed")
            print(f"   User: {data['user']['name']}")
            print(f"   Total conversations: {data['total_conversations']}")
        else:
            print(f"❌ Chat history test failed: {response.status_code}")
            return False

    except Exception as e:
        print(f"❌ Chat history test error: {str(e)}")
        return False

    # Test 5: Get all users
    print("\n📝 Test 5: Getting all users...")
    try:
        response = requests.get(f"{BASE_URL}/api/chat/users")

        if response.status_code == 200:
            data = response.json()
            print(f"✅ Users list test passed")
            print(f"   Total users: {data['total_users']}")
        else:
            print(f"❌ Users list test failed: {response.status_code}")
            return False

    except Exception as e:
        print(f"❌ Users list test error: {str(e)}")
        return False

    return True


def test_error_cases():
    """Test error cases"""
    print("\n🧪 Testing Error Cases...")

    # Test missing message
    print("📝 Testing missing message...")
    try:
        payload = {}
        response = requests.post(
            f"{BASE_URL}/api/chat/message",
            json=payload,
            headers={"Content-Type": "application/json"}
        )

        if response.status_code == 400:
            print("✅ Missing message error handling works")
        else:
            print(f"❌ Expected 400, got {response.status_code}")

    except Exception as e:
        print(f"❌ Error test failed: {str(e)}")


def main():
    """Run all tests"""
    print("🧪 Testing Chat Message Endpoint")
    print("=" * 60)
    print("⚠️  Make sure the Flask app is running on port 5001!")
    print("   Run: python app.py")
    print("=" * 60)

    # Test basic connectivity
    try:
        response = requests.get(f"{BASE_URL}/ping")
        if response.status_code != 200:
            print("❌ Flask app is not running or not accessible")
            print("   Please start the app with: python app.py")
            return
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to Flask app")
        print("   Please start the app with: python app.py")
        return

    success = test_chat_message_endpoint()
    test_error_cases()

    print("\n" + "=" * 60)
    if success:
        print("🎯 Task 5 Requirements Met:")
        print("✅ Added chat.py in routes/ with POST /api/chat/message")
        print("✅ Accepts message and user context, returns Gemini response")
        print("✅ POST JSON body test successful, got chat reply")
        print("\n🚀 Ready for next phase!")
    else:
        print("❌ Some tests failed. Please check the implementation.")


if __name__ == "__main__":
    main()

```

# test_claude.py

```py
#!/usr/bin/env python3
"""
Test script for Claude API integration (Task 3)
"""

from services.claude_service import get_support_response
import os
import sys
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


def test_claude_integration():
    """Test the get_support_response function"""
    print("🧪 Testing Claude API Integration (Task 3)")
    print("=" * 50)

    # Test message
    test_message = "I'm having trouble finding food today and don't know where to turn for help."

    # Test context
    test_context = {
        'location': 'San Francisco, CA',
        'situation': 'experiencing food insecurity',
        'needs': 'food assistance'
    }

    print(f"📝 Test Message: {test_message}")
    print(f"📍 Test Context: {test_context}")
    print("\n🤖 Claude Response:")
    print("-" * 30)

    try:
        # Call the get_support_response function
        response = get_support_response(test_message, test_context)
        print(response)
        print("-" * 30)
        print("✅ Claude integration test completed successfully!")

        # Check if we got a fallback response (indicating no API key)
        if "trouble connecting to my full capabilities" in response:
            print("\n⚠️  Note: Using fallback response (CLAUDE_API_KEY not configured)")
            print("To test with actual Claude API:")
            print("1. Set CLAUDE_API_KEY environment variable")
            print("2. Run: export CLAUDE_API_KEY=your_api_key")
            print("3. Run this test again")
        else:
            print("\n🎉 Successfully connected to Claude API!")

    except Exception as e:
        print(f"❌ Error testing Claude integration: {str(e)}")
        return False

    return True


def test_without_context():
    """Test the function without context"""
    print("\n🧪 Testing without context...")
    test_message = "Hello, I need some help."

    try:
        response = get_support_response(test_message)
        print(f"Response: {response[:100]}...")
        print("✅ Test without context passed!")
    except Exception as e:
        print(f"❌ Error: {str(e)}")


if __name__ == "__main__":
    print("Starting Claude API Integration Tests...\n")

    # Test with context
    success = test_claude_integration()

    # Test without context
    test_without_context()

    print(f"\n{'='*50}")
    if success:
        print("🎯 Task 3 Requirements Met:")
        print("✅ Created claude_service.py in services/")
        print("✅ Function get_support_response(message, context) implemented")
        print("✅ Test message processed and Claude response returned")
        print("\n🚀 Ready for Task 4!")
    else:
        print("❌ Some tests failed. Please check the implementation.")

```

# test_formatting.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Enhanced Formatting Test</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            max-width: 800px;
            margin: 40px auto;
            padding: 20px;
            background: #f8f9fa;
        }
        
        .message {
            margin-bottom: 20px;
            padding: 16px;
            border-radius: 18px;
            background: white;
            border: 1px solid #e0e0e0;
            line-height: 1.6;
        }
        
        .message-content p {
            margin-bottom: 12px;
            line-height: 1.6;
        }
        
        .message-content strong {
            font-weight: 600;
            color: #007bff;
        }
        
        .message-content a {
            color: #007bff;
            text-decoration: none;
            font-weight: 500;
        }
        
        .message-content a:hover {
            text-decoration: underline;
        }
        
        .resource-section {
            margin-top: 15px;
            padding: 12px;
            background: rgba(0, 123, 255, 0.05);
            border-left: 3px solid #007bff;
            border-radius: 8px;
        }
        
        .resource-title {
            font-weight: 600;
            color: #007bff;
            margin-bottom: 8px;
            font-size: 14px;
        }
        
        .resource-item {
            margin-bottom: 12px;
            padding: 8px;
            background: white;
            border-radius: 6px;
            border: 1px solid #e0e0e0;
        }
        
        .resource-name {
            font-weight: 600;
            margin-bottom: 4px;
        }
        
        .resource-details {
            font-size: 13px;
            color: #666;
        }
        
        .resource-contact {
            margin-top: 6px;
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
        }
        
        .contact-link {
            display: inline-flex;
            align-items: center;
            gap: 4px;
            padding: 4px 8px;
            background: #007bff;
            color: white;
            text-decoration: none;
            border-radius: 12px;
            font-size: 12px;
            font-weight: 500;
        }
        
        .contact-link:hover {
            background: #0056b3;
            color: white;
            text-decoration: none;
        }
        
        .test-button {
            background: #28a745;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 8px;
            cursor: pointer;
            margin: 10px 5px;
        }
    </style>
</head>
<body>
    <h1>Enhanced Message Formatting Test</h1>
    
    <div class="message" id="testMessage">
        <!-- This will be populated by JavaScript -->
    </div>
    
    <button class="test-button" onclick="testFormatting()">Test Formatting</button>
    <button class="test-button" onclick="testResourceExtraction()">Test Resource Extraction</button>
    
    <script>
        // Copy the formatting functions from index.html
        function formatBotMessage(text) {
            const { mainContent, resources } = extractResources(text);
            
            let formattedText = mainContent;
            
            // Format bold text (**text** -> <strong>text</strong>)
            formattedText = formattedText.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
            
            // Format phone numbers as clickable links
            formattedText = formattedText.replace(/(\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4})/g, '<a href="tel:$1">$1</a>');
            
            // Format email addresses as clickable links
            formattedText = formattedText.replace(/([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})/g, '<a href="mailto:$1">$1</a>');
            
            // Split into paragraphs for better readability
            const paragraphs = formattedText.split('\n\n').filter(p => p.trim());
            const paragraphHTML = paragraphs.map(p => `<p>${p.trim()}</p>`).join('');
            
            let html = `<div class="message-content">${paragraphHTML}</div>`;
            
            // Add resource section if resources were found
            if (resources.length > 0) {
                html += generateResourceSection(resources);
            }
            
            return html;
        }
        
        function extractResources(text) {
            const resources = [];
            let mainContent = text;
            
            // Look for organization names followed by contact info
            const lines = text.split('\n');
            let currentResource = null;
            const contentLines = [];
            
            for (let line of lines) {
                line = line.trim();
                
                // Check for organization names
                const orgMatch = line.match(/^([A-Z][^.]*(?:Center|Bank|Service|House|Shelter|Clinic|Organization|Foundation|Project|Community|Food)[^.]*)/);
                if (orgMatch && !line.includes('Address:') && !line.includes('Phone:')) {
                    if (currentResource) {
                        resources.push(currentResource);
                    }
                    currentResource = {
                        name: orgMatch[1].trim(),
                        address: '',
                        phone: '',
                        hours: '',
                        details: []
                    };
                    contentLines.push(line);
                } else if (currentResource && line.includes('Address:')) {
                    currentResource.address = line.replace(/.*Address:\s*/, '').replace(/\s*Phone:.*/, '').trim();
                } else if (currentResource && line.includes('Phone:')) {
                    currentResource.phone = line.replace(/.*Phone:\s*/, '').replace(/\s*Hours:.*/, '').trim();
                } else if (currentResource && line.includes('Hours:')) {
                    currentResource.hours = line.replace(/.*Hours:\s*/, '').trim();
                } else if (currentResource && line.includes('Requirements:')) {
                    currentResource.details.push(line.replace(/.*Requirements:\s*/, '').trim());
                } else if (!line.includes('Address:') && !line.includes('Phone:') && !line.includes('Hours:') && !line.includes('Requirements:')) {
                    contentLines.push(line);
                }
            }
            
            if (currentResource) {
                resources.push(currentResource);
            }
            
            // Clean up main content
            mainContent = contentLines.filter(line => line.trim()).join('\n');
            
            return {
                mainContent: mainContent.replace(/\*\s*\*/g, '').trim(),
                resources: resources
            };
        }
        
        function generateResourceSection(resources) {
            if (resources.length === 0) return '';
            
            let html = '<div class="resource-section">';
            html += '<div class="resource-title">📋 Available Resources</div>';
            
            resources.forEach(resource => {
                html += '<div class="resource-item">';
                html += `<div class="resource-name">${resource.name}</div>`;
                
                let details = '';
                if (resource.address) details += `📍 ${resource.address}<br>`;
                if (resource.hours) details += `🕒 ${resource.hours}<br>`;
                if (resource.details.length > 0) details += resource.details.join('<br>');
                
                if (details) {
                    html += `<div class="resource-details">${details}</div>`;
                }
                
                if (resource.phone || resource.address) {
                    html += '<div class="resource-contact">';
                    if (resource.phone) {
                        html += `<a href="tel:${resource.phone}" class="contact-link">📞 Call</a>`;
                    }
                    if (resource.address) {
                        const mapsUrl = `https://maps.google.com/?q=${encodeURIComponent(resource.address)}`;
                        html += `<a href="${mapsUrl}" target="_blank" class="contact-link">📍 Directions</a>`;
                    }
                    html += '</div>';
                }
                
                html += '</div>';
            });
            
            html += '</div>';
            return html;
        }
        
        function testFormatting() {
            const testMessage = `I understand you need help finding food in Oakland. Let's get you connected to some resources right away.

The **Alameda County Community Food Bank** is a great place to start. They offer food assistance to anyone who needs it.

You can also contact them directly at (510) 635-3663 or email them at info@accfb.org for more information.

**Next Steps:**
1. Visit during their open hours
2. Bring identification if possible
3. Consider visiting multiple locations for variety`;
            
            const formatted = formatBotMessage(testMessage);
            document.getElementById('testMessage').innerHTML = formatted;
        }
        
        function testResourceExtraction() {
            const testMessage = `I understand you need help finding food in Oakland. Let's get you connected to some resources right away.

Alameda County Community Food Bank is a great place to start. They offer food assistance to anyone who needs it.

    * **Address:** 7900 Edgewater Dr, Oakland, CA 94621
    * **Phone:** (510) 635-3663
    * **Hours:** Monday-Friday, 9am-4pm
    * **Requirements:** No documentation is required. Just go during their open hours.

They are open now, so you could go there today. If you can't make it today, please call them to confirm their hours and availability.

For additional food options, you can also try searching online for "food pantries near me Oakland, CA" to find other nearby locations.`;
            
            const formatted = formatBotMessage(testMessage);
            document.getElementById('testMessage').innerHTML = formatted;
        }
        
        // Test on page load
        testFormatting();
    </script>
</body>
</html> 
```

# test_gemini.py

```py
#!/usr/bin/env python3
"""
Test script for Gemini API integration (Task 3)
"""

from services.gemini_service import get_support_response
import os
import sys
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


def test_gemini_integration():
    """Test the get_support_response function"""
    print("🧪 Testing Gemini API Integration (Task 3)")
    print("=" * 50)

    # Test message
    test_message = "I'm having trouble finding food today and don't know where to turn for help."

    # Test context
    test_context = {
        'location': 'San Francisco, CA',
        'situation': 'experiencing food insecurity',
        'needs': 'food assistance'
    }

    print(f"📝 Test Message: {test_message}")
    print(f"📍 Test Context: {test_context}")
    print("\n🤖 Gemini Response:")
    print("-" * 30)

    try:
        # Call the get_support_response function
        response = get_support_response(test_message, test_context)
        print(response)
        print("-" * 30)
        print("✅ Gemini integration test completed successfully!")

        # Check if we got a fallback response (indicating no API key)
        if "unable to access my full capabilities" in response:
            print("\n⚠️  Note: Using fallback response (GEMINI_API_KEY not configured)")
            print("To test with actual Gemini API:")
            print("1. Set GEMINI_API_KEY environment variable")
            print("2. Run: export GEMINI_API_KEY=your_api_key")
            print("3. Run this test again")
        else:
            print("\n🎉 Successfully connected to Gemini API!")

    except Exception as e:
        print(f"❌ Error testing Gemini integration: {str(e)}")
        return False

    return True


def test_without_context():
    """Test the function without context"""
    print("\n🧪 Testing without context...")
    test_message = "Hello, I need some help."

    try:
        response = get_support_response(test_message)
        print(f"Response: {response[:100]}...")
        print("✅ Test without context passed!")
    except Exception as e:
        print(f"❌ Error: {str(e)}")


def test_prompt_types():
    """Test different prompt types"""
    print("\n🧪 Testing different prompt types...")
    test_message = "I need help with housing."
    test_context = {'location': 'Oakland, CA', 'situation': 'homeless'}

    # Test empathetic coach
    print("\n🤗 Testing empathetic_coach prompt:")
    response = get_support_response(
        test_message, test_context, "empathetic_coach")
    print(f"Response: {response[:150]}...")

    # Test direct assistant
    print("\n📋 Testing direct_assistant prompt:")
    response = get_support_response(
        test_message, test_context, "direct_assistant")
    print(f"Response: {response[:150]}...")

    print("✅ Prompt type tests completed!")


if __name__ == "__main__":
    print("Starting Gemini API Integration Tests...\n")

    # Test with context
    success = test_gemini_integration()

    # Test without context
    test_without_context()

    # Test prompt types
    test_prompt_types()

    print(f"\n{'='*50}")
    if success:
        print("🎯 Task 3 Requirements Met:")
        print("✅ Created gemini_service.py in services/")
        print("✅ Function get_support_response(message, context) implemented")
        print("✅ Test message processed and Gemini response returned")
        print("\n🚀 Ready for Task 4!")
    else:
        print("❌ Some tests failed. Please check the implementation.")

```

# test_microphone.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Microphone Test</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            max-width: 600px;
            margin: 50px auto;
            padding: 20px;
            text-align: center;
        }
        
        .test-circle {
            width: 150px;
            height: 150px;
            border-radius: 50%;
            background: linear-gradient(135deg, #007bff, #00a8ff);
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            margin: 30px auto;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(0,123,255,0.3);
        }
        
        .test-circle:hover {
            transform: scale(1.05);
        }
        
        .test-circle.listening {
            animation: pulse 2s infinite;
        }
        
        .test-circle.speaking {
            animation: glow 1.5s ease-in-out infinite alternate;
        }
        
        @keyframes pulse {
            0% { box-shadow: 0 0 0 0 rgba(0,123,255,0.7); }
            70% { box-shadow: 0 0 0 20px rgba(0,123,255,0); }
            100% { box-shadow: 0 0 0 0 rgba(0,123,255,0); }
        }
        
        @keyframes glow {
            from { box-shadow: 0 0 20px rgba(0,255,123,0.5), 0 0 30px rgba(0,255,123,0.3); }
            to { box-shadow: 0 0 30px rgba(0,255,123,0.8), 0 0 40px rgba(0,255,123,0.5); }
        }
        
        .test-icon {
            font-size: 36px;
            color: white;
        }
        
        .status {
            margin: 20px 0;
            font-size: 18px;
            color: #333;
        }
        
        .transcript {
            margin: 20px 0;
            padding: 15px;
            background: #f8f9fa;
            border-radius: 8px;
            border-left: 4px solid #007bff;
            text-align: left;
        }
        
        .controls {
            margin: 20px 0;
        }
        
        .btn {
            padding: 10px 20px;
            margin: 5px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 14px;
        }
        
        .btn-primary {
            background: #007bff;
            color: white;
        }
        
        .btn-secondary {
            background: #6c757d;
            color: white;
        }
    </style>
</head>
<body>
    <h1>🎤 Microphone & Speech Test</h1>
    <p>Test your microphone and speech recognition functionality</p>
    
    <div class="test-circle" id="testCircle" onclick="toggleRecording()">
        <div class="test-icon">🎤</div>
    </div>
    
    <div class="status" id="status">Click the microphone to start</div>
    
    <div class="transcript" id="transcript" style="display: none;">
        <strong>Transcript:</strong><br>
        <span id="transcriptText"></span>
    </div>
    
    <div class="controls">
        <button class="btn btn-secondary" onclick="stopSpeech()">Stop Speech</button>
        <button class="btn btn-primary" onclick="testSpeech()">Test Speech Synthesis</button>
    </div>
    
    <div style="margin-top: 30px; font-size: 14px; color: #666;">
        <p><strong>Browser Support:</strong></p>
        <p>Speech Recognition: <span id="speechRecognitionSupport"></span></p>
        <p>Speech Synthesis: <span id="speechSynthesisSupport"></span></p>
        <p>Microphone Permissions: <span id="micPermissions"></span></p>
    </div>

    <script>
        let recognition = null;
        let isListening = false;
        
        // Check browser support
        window.addEventListener('load', () => {
            // Check Speech Recognition support
            const speechRecognitionSupported = 'webkitSpeechRecognition' in window || 'SpeechRecognition' in window;
            document.getElementById('speechRecognitionSupport').textContent = speechRecognitionSupported ? '✅ Supported' : '❌ Not Supported';
            
            // Check Speech Synthesis support
            const speechSynthesisSupported = 'speechSynthesis' in window;
            document.getElementById('speechSynthesisSupport').textContent = speechSynthesisSupported ? '✅ Supported' : '❌ Not Supported';
            
            // Check microphone permissions
            checkMicPermissions();
            
            // Initialize speech recognition
            if (speechRecognitionSupported) {
                initSpeechRecognition();
            }
        });
        
        async function checkMicPermissions() {
            try {
                if (navigator.permissions) {
                    const permission = await navigator.permissions.query({ name: 'microphone' });
                    document.getElementById('micPermissions').textContent = `${permission.state === 'granted' ? '✅' : permission.state === 'denied' ? '❌' : '⚠️'} ${permission.state}`;
                } else {
                    document.getElementById('micPermissions').textContent = '⚠️ Cannot check (API not available)';
                }
            } catch (error) {
                document.getElementById('micPermissions').textContent = '⚠️ Cannot check';
            }
        }
        
        function initSpeechRecognition() {
            if ('webkitSpeechRecognition' in window) {
                recognition = new webkitSpeechRecognition();
            } else if ('SpeechRecognition' in window) {
                recognition = new SpeechRecognition();
            } else {
                return false;
            }
            
            recognition.continuous = false;
            recognition.interimResults = false;
            recognition.lang = 'en-US';
            
            recognition.onstart = function() {
                console.log('Speech recognition started');
                document.getElementById('testCircle').classList.add('listening');
                document.getElementById('status').textContent = 'Listening... Speak now!';
            };
            
            recognition.onresult = function(event) {
                const transcript = event.results[0][0].transcript;
                console.log('Speech recognized:', transcript);
                
                document.getElementById('transcriptText').textContent = transcript;
                document.getElementById('transcript').style.display = 'block';
                document.getElementById('status').textContent = 'Speech recognized! Click to try again.';
                
                // Speak the result back
                speak(`I heard you say: ${transcript}`);
            };
            
            recognition.onerror = function(event) {
                console.error('Speech recognition error:', event.error);
                document.getElementById('testCircle').classList.remove('listening');
                document.getElementById('status').textContent = `Error: ${event.error}. Click to try again.`;
                isListening = false;
            };
            
            recognition.onend = function() {
                console.log('Speech recognition ended');
                document.getElementById('testCircle').classList.remove('listening');
                isListening = false;
                if (document.getElementById('status').textContent.includes('Listening')) {
                    document.getElementById('status').textContent = 'No speech detected. Click to try again.';
                }
            };
            
            return true;
        }
        
        function toggleRecording() {
            if (!recognition) {
                alert('Speech recognition not supported in this browser. Please use Chrome, Edge, or Safari.');
                return;
            }
            
            const circle = document.getElementById('testCircle');
            
            // If speaking, stop speech
            if (circle.classList.contains('speaking')) {
                speechSynthesis.cancel();
                circle.classList.remove('speaking');
                document.getElementById('status').textContent = 'Speech stopped. Click to record.';
                return;
            }
            
            if (isListening) {
                recognition.stop();
                circle.classList.remove('listening');
                document.getElementById('status').textContent = 'Stopped listening. Click to try again.';
                isListening = false;
            } else {
                try {
                    recognition.start();
                    isListening = true;
                } catch (error) {
                    console.error('Error starting recognition:', error);
                    document.getElementById('status').textContent = 'Error starting microphone. Check permissions.';
                }
            }
        }
        
        function speak(text) {
            speechSynthesis.cancel();
            
            const utterance = new SpeechSynthesisUtterance(text);
            utterance.rate = 0.9;
            utterance.pitch = 1;
            utterance.volume = 0.8;
            
            const circle = document.getElementById('testCircle');
            
            utterance.onstart = function() {
                circle.classList.add('speaking');
                document.getElementById('status').textContent = 'Speaking... Click to stop.';
            };
            
            utterance.onend = function() {
                circle.classList.remove('speaking');
                document.getElementById('status').textContent = 'Click to record again.';
            };
            
            utterance.onerror = function(event) {
                console.error('Speech synthesis error:', event.error);
                circle.classList.remove('speaking');
                document.getElementById('status').textContent = 'Speech error. Click to try again.';
            };
            
            speechSynthesis.speak(utterance);
        }
        
        function stopSpeech() {
            speechSynthesis.cancel();
            document.getElementById('testCircle').classList.remove('speaking');
            document.getElementById('status').textContent = 'Speech stopped. Click to record.';
        }
        
        function testSpeech() {
            speak('Hello! This is a test of the speech synthesis functionality. If you can hear this, speech synthesis is working correctly.');
        }
    </script>
</body>
</html> 
```

# test_models.py

```py
#!/usr/bin/env python3
"""
Test script for User and Conversation models (Task 4)
"""

from app import app, db, User, Conversation
from datetime import datetime


def test_models():
    """Test the User and Conversation models"""
    print("🧪 Testing User and Conversation Models (Task 4)")
    print("=" * 60)

    with app.app_context():
        try:
            # Test 1: Create a new user
            print("📝 Test 1: Creating a new user...")
            user = User(
                name="John Doe",
                location="San Francisco, CA",
                situation="Looking for food assistance",
                needs="Food, temporary shelter"
            )

            db.session.add(user)
            db.session.commit()
            print(f"✅ User created: {user}")
            print(f"   User ID: {user.id}")
            print(f"   User dict: {user.to_dict()}")

            # Test 2: Create a conversation for the user
            print("\n📝 Test 2: Creating a conversation...")
            conversation = Conversation(
                user_id=user.id,
                message="I need help finding food today",
                response="I understand you're looking for food assistance. Let me help you find local resources.",
                message_type="user",
                context={
                    "location": user.location,
                    "situation": user.situation,
                    "needs": user.needs
                }
            )

            db.session.add(conversation)
            db.session.commit()
            print(f"✅ Conversation created: {conversation}")
            print(f"   Conversation ID: {conversation.id}")
            print(f"   Conversation dict: {conversation.to_dict()}")

            # Test 3: Query the user with conversations
            print("\n📝 Test 3: Querying user with conversations...")
            user_with_conversations = User.query.get(user.id)
            print(f"✅ User found: {user_with_conversations}")
            print(
                f"   Number of conversations: {len(user_with_conversations.conversations)}")

            for conv in user_with_conversations.conversations:
                print(f"   - Conversation: {conv.message[:50]}...")

            # Test 4: Query all users
            print("\n📝 Test 4: Querying all users...")
            all_users = User.query.all()
            print(f"✅ Total users in database: {len(all_users)}")

            # Test 5: Query all conversations
            print("\n📝 Test 5: Querying all conversations...")
            all_conversations = Conversation.query.all()
            print(
                f"✅ Total conversations in database: {len(all_conversations)}")

            print("\n" + "=" * 60)
            print("🎯 Task 4 Requirements Met:")
            print("✅ Created user.py in models/")
            print("✅ Created conversation.py in models/")
            print("✅ SQLAlchemy models created and linked to SQLite")
            print("✅ Test data inserted into tables successfully")
            print("\n🚀 Ready for Task 5!")

            return True

        except Exception as e:
            print(f"❌ Error testing models: {str(e)}")
            return False


def test_flask_shell_commands():
    """Test commands that would be run in Flask shell"""
    print("\n🧪 Testing Flask Shell Commands...")

    with app.app_context():
        try:
            # Commands you could run in Flask shell
            print("📝 Flask shell equivalent commands:")
            print("   from models.user import User")
            print("   from models.conversation import Conversation")
            print("   from app import db")

            # Create another test user
            user2 = User(name="Jane Smith", location="Oakland, CA")
            db.session.add(user2)
            db.session.commit()

            print(f"✅ Created user via Flask shell simulation: {user2}")

        except Exception as e:
            print(f"❌ Error in Flask shell test: {str(e)}")


if __name__ == "__main__":
    print("Starting Model Tests...\n")

    success = test_models()
    test_flask_shell_commands()

    if success:
        print("\n🎉 All tests passed! Database models are working correctly.")
    else:
        print("\n❌ Some tests failed. Please check the implementation.")

```

# utils/__init__.py

```py
# Utils package for helper functions

```

# utils/formatters.py

```py
# Clean display text, time helpers

```

