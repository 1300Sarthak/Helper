#!/bin/bash

echo "🚀 Starting For Social Change MVP..."

# Start backend server
echo "📡 Starting backend server on port 5001..."
cd social_change_backend
export CLAUDE_API_KEY="demo-key-for-testing"
export PORT=5001
python app.py &
BACKEND_PID=$!

# Wait a moment for backend to start
sleep 3

# Start frontend server
echo "🌐 Starting frontend server on port 3000..."
cd ../social_change_frontend
npm start &
FRONTEND_PID=$!

echo "✅ Both servers are starting..."
echo "📱 Frontend: http://localhost:3000"
echo "🔧 Backend: http://localhost:5001/api/health"
echo ""
echo "Press Ctrl+C to stop both servers"

# Wait for user to stop
wait 