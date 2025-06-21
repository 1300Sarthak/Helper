from flask import Blueprint, request, jsonify
from datetime import datetime
import logging
from services.claude_service import ClaudeService
from models.user import get_user
from models.conversation import get_user_conversation, save_conversation

logger = logging.getLogger(__name__)
chat_bp = Blueprint('chat', __name__)

# Initialize Claude service
claude_service = ClaudeService()


@chat_bp.route('/message', methods=['POST'])
def send_message():
    """Send a message to Claude AI and get response"""
    try:
        data = request.get_json()

        if not data or 'message' not in data:
            return jsonify({'error': 'Message is required'}), 400

        message = data['message'].strip()
        user_id = data.get('user_id')
        mode = data.get('mode', 'support')  # 'support' or 'coach'

        if not message:
            return jsonify({'error': 'Message cannot be empty'}), 400

        # Get user context
        user_context = {}
        if user_id:
            user = get_user(user_id)
            if user:
                user_context = user.get_context_for_ai()

        # Get or create conversation
        conversation = None
        if user_id:
            conversation = get_user_conversation(user_id)
            if conversation:
                # Add user message to conversation
                conversation.add_message(message, sender="user", mode=mode)

        # Get AI response
        try:
            if mode == 'coach':
                ai_response = claude_service.get_coach_response(
                    message, user_context)
            else:
                ai_response = claude_service.get_support_response(
                    message, user_context)

            # Add AI response to conversation
            if conversation:
                conversation.add_message(
                    ai_response, sender="assistant", mode=mode)
                save_conversation(conversation)

            return jsonify({
                'response': ai_response,
                'timestamp': datetime.utcnow().isoformat(),
                'mode': mode,
                'conversation_id': conversation.conversation_id if conversation else None
            })

        except Exception as e:
            logger.error(f"Error getting AI response: {str(e)}")
            return jsonify({
                'error': 'Unable to get AI response at this time. Please try again.',
                'fallback_response': "I'm here to help. Could you tell me more about what you need assistance with?"
            }), 500

    except Exception as e:
        logger.error(f"Error in send_message: {str(e)}")
        return jsonify({'error': 'Internal server error'}), 500


@chat_bp.route('/conversation/<user_id>', methods=['GET'])
def get_conversation_history(user_id):
    """Get conversation history for a user"""
    try:
        conversation = get_user_conversation(user_id)

        if not conversation:
            return jsonify({'messages': [], 'conversation_id': None})

        # Get recent messages (last 20)
        recent_messages = conversation.get_recent_messages(20)

        return jsonify({
            'conversation_id': conversation.conversation_id,
            'messages': [msg.to_dict() for msg in recent_messages],
            'total_messages': len(conversation.messages)
        })

    except Exception as e:
        logger.error(f"Error getting conversation history: {str(e)}")
        return jsonify({'error': 'Internal server error'}), 500


@chat_bp.route('/voice-to-text', methods=['POST'])
def voice_to_text():
    """Convert voice input to text (placeholder for future enhancement)"""
    # This is a placeholder endpoint for future voice-to-text integration
    return jsonify({
        'message': 'Voice-to-text feature coming soon',
        'status': 'not_implemented'
    }), 501
