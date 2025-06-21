from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from datetime import datetime
import logging
from config import config
from cag_service import get_cag_service

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load configuration
config_name = os.environ.get('FLASK_ENV', 'default')
app.config.from_object(config[config_name])

# Initialize CAG service
cag_service = get_cag_service(app.config)

# Global variables for chatbot state
chat_history = []


@app.route('/')
def home():
    """Health check endpoint"""
    return jsonify({
        'status': 'success',
        'message': 'CAG Chatbot API is running',
        'timestamp': datetime.now().isoformat(),
        'version': '1.0.0'
    })


@app.route('/api/chat', methods=['POST'])
def chat():
    """Main chat endpoint for handling user messages"""
    try:
        data = request.get_json()

        if not data or 'message' not in data:
            return jsonify({
                'error': 'Message is required'
            }), 400

        user_message = data['message']
        user_id = data.get('user_id', 'anonymous')

        # Validate message
        if not cag_service.validate_message(user_message):
            return jsonify({
                'error': 'Invalid message format'
            }), 400

        # Log the incoming message
        logger.info(f"Received message from user {user_id}: {user_message}")

        # Add to chat history
        chat_entry = {
            'user_id': user_id,
            'message': user_message,
            'timestamp': datetime.now().isoformat(),
            'type': 'user'
        }
        chat_history.append(chat_entry)

        # Get chat context
        context = cag_service.get_chat_context(user_id)

        # Generate CAG chatbot response
        bot_response = cag_service.generate_response(
            user_message, user_id, context)

        # Add bot response to chat history
        bot_entry = {
            'user_id': 'bot',
            'message': bot_response,
            'timestamp': datetime.now().isoformat(),
            'type': 'bot'
        }
        chat_history.append(bot_entry)

        return jsonify({
            'response': bot_response,
            'user_id': user_id,
            'timestamp': datetime.now().isoformat(),
            'context': context
        })

    except Exception as e:
        logger.error(f"Error in chat endpoint: {str(e)}")
        return jsonify({
            'error': 'Internal server error'
        }), 500


@app.route('/api/chat/history', methods=['GET'])
def get_chat_history():
    """Get chat history for a specific user"""
    try:
        user_id = request.args.get('user_id', 'anonymous')

        # Filter chat history by user_id
        user_history = [
            entry for entry in chat_history if entry['user_id'] == user_id]

        return jsonify({
            'chat_history': user_history,
            'total_messages': len(user_history)
        })

    except Exception as e:
        logger.error(f"Error getting chat history: {str(e)}")
        return jsonify({
            'error': 'Internal server error'
        }), 500


@app.route('/api/chat/clear', methods=['POST'])
def clear_chat_history():
    """Clear chat history for a specific user"""
    try:
        data = request.get_json()
        user_id = data.get('user_id', 'anonymous')

        global chat_history
        chat_history = [
            entry for entry in chat_history if entry['user_id'] != user_id]

        return jsonify({
            'message': f'Chat history cleared for user {user_id}',
            'remaining_messages': len(chat_history)
        })

    except Exception as e:
        logger.error(f"Error clearing chat history: {str(e)}")
        return jsonify({
            'error': 'Internal server error'
        }), 500


@app.route('/api/status', methods=['GET'])
def get_status():
    """Get application status and configuration info"""
    try:
        return jsonify({
            'status': 'running',
            'timestamp': datetime.now().isoformat(),
            'config': {
                'debug': app.config['DEBUG'],
                'cag_api_configured': bool(cag_service.api_key),
                'cag_model': cag_service.model_name
            },
            'stats': {
                'total_chat_entries': len(chat_history),
                'unique_users': len(set(entry['user_id'] for entry in chat_history if entry['user_id'] != 'bot'))
            }
        })
    except Exception as e:
        logger.error(f"Error getting status: {str(e)}")
        return jsonify({
            'error': 'Internal server error'
        }), 500


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
    port = app.config['PORT']
    logger.info(f"Starting CAG Chatbot API on port {port}")
    app.run(host='0.0.0.0', port=port, debug=app.config['DEBUG'])
