# For Social Change - Social Services Platform

A comprehensive platform connecting vulnerable individuals with resources, support, and AI-powered assistance. Built to serve people experiencing homelessness, housing insecurity, or those at risk.

## Features

- 🤖 AI-powered conversational support via Claude API
- 🎯 Life coaching and goal-setting assistance
- 📍 Location-based resource recommendations
- 🎨 Accessible, mobile-first design with dark/light themes
- 🗣️ Voice interface simulation
- 📱 Responsive design for all devices
- 🔒 Privacy-first approach with local storage

## Tech Stack

- **Frontend**: React 18+ with TypeScript
- **Backend**: Flask (Python 3.9+)
- **AI Integration**: Claude API (Anthropic)
- **Database**: SQLite (MVP)
- **Styling**: Tailwind CSS
- **State Management**: React Context
- **HTTP Client**: Axios

## Quick Start

### Backend Setup

```bash
cd social_change_backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

### Frontend Setup

```bash
cd social_change_frontend
npm install
npm start
```

## Project Structure

```
├── social_change_backend/     # Flask API server
├── social_change_frontend/    # React TypeScript app
└── README.md
```

## Environment Variables

Create `.env` files in both backend and frontend directories:

**Backend (.env):**

```
CLAUDE_API_KEY=your_claude_api_key_here
DATABASE_URL=sqlite:///social_change.db
FLASK_ENV=development
SECRET_KEY=your_secret_key_here
CORS_ORIGINS=http://localhost:3000
```

## API Endpoints

- `POST /api/chat/message` - Send message to Claude AI
- `POST /api/users/profile` - Create/update user profile
- `GET /api/resources/search` - Find local resources
- `GET /api/resources/quick-actions` - Get quick action resources

## Contributing

This project is designed to help vulnerable individuals access resources and support. All contributions should prioritize accessibility, empathy, and user dignity.
