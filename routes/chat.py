# Chat routes - /api/chat endpoints

from flask import Blueprint, request, jsonify
from datetime import datetime
import logging
from models.user import db, User
from models.conversation import Conversation
from services.claude_service import get_support_response, analyze_journal_entry, summarize_conversation, score_emotional_state
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

        # Get Claude response with enhanced context
        claude_response = get_support_response(message, {
            'name': user.name,
            'location': user.location,
            'situation': user.situation,
            'needs': user.needs
        })

        # Save conversation with emotion analysis in context
        conversation_context = {
            'user_context': context,
            'emotion_analysis': emotion_scores
        }

        conversation = Conversation(
            user_id=user.id,
            message=message,
            response=claude_response,
            message_type='text',
            context=conversation_context
        )
        db.session.add(conversation)
        db.session.commit()

        logger.info(f"Saved conversation for user {user.id}")

        return jsonify({
            'response': claude_response,
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
    Analyze journal entry using Claude for emotion scoring
    """
    try:
        data = request.get_json()

        if not data or 'journal_text' not in data:
            return jsonify({'error': 'Journal text is required'}), 400

        journal_text = data['journal_text']
        user_context = data.get('context', {})

        logger.info(f"Analyzing journal entry: {journal_text[:50]}...")

        # Analyze with Claude
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
    Summarize a user's conversation history using Claude
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

        # Format messages for Claude
        messages = []
        for conv in reversed(conversations):  # Reverse to get chronological order
            messages.append({'role': 'user', 'content': conv.message})
            messages.append({'role': 'assistant', 'content': conv.response})

        # Get summary from Claude
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
