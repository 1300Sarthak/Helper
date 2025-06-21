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

```
.
├── app.py              # Main Flask application
├── config.py           # Configuration management
├── cag_service.py      # CAG chatbot service layer
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Environment Configuration

Create a `.env` file in the root directory with the following variables:

```env
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
```

### 3. Run the Application

#### Development Mode

```bash
python app.py
```

#### Production Mode

```bash
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

The application will be available at `http://localhost:5000`

## API Endpoints

### Health Check

- **GET** `/`
- Returns application status

### Chat Endpoints

#### Send Message

- **POST** `/api/chat`
- **Body:**
  ```json
  {
    "message": "Hello, how are you?",
    "user_id": "user123"
  }
  ```
- **Response:**
  ```json
  {
    "response": "Hello! I'm doing well, thank you for asking.",
    "user_id": "user123",
    "timestamp": "2024-01-01T12:00:00"
  }
  ```

#### Get Chat History

- **GET** `/api/chat/history?user_id=user123`
- **Response:**
  ```json
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
  ```

#### Clear Chat History

- **POST** `/api/chat/clear`
- **Body:**
  ```json
  {
    "user_id": "user123"
  }
  ```
- **Response:**
  ```json
  {
    "message": "Chat history cleared for user user123",
    "remaining_messages": 0
  }
  ```

## CAG Integration

The application includes a placeholder CAG service in `cag_service.py`. To integrate with your actual CAG system:

1. Update the `CAGService.generate_response()` method in `cag_service.py`
2. Configure your CAG API credentials in the environment variables
3. Implement the actual API calls to your CAG system

### Example CAG Integration

```python
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
```

## Development

### Adding New Endpoints

1. Add your route in `app.py`
2. Implement proper error handling
3. Add logging for debugging
4. Update this README with endpoint documentation

### Testing

You can test the API using curl or any HTTP client:

```bash
# Health check
curl http://localhost:5000/

# Send a message
curl -X POST http://localhost:5000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello", "user_id": "test_user"}'

# Get chat history
curl http://localhost:5000/api/chat/history?user_id=test_user
```

## Deployment

### Docker (Optional)

Create a `Dockerfile`:

```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
```

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
