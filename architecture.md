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
