from flask import Blueprint, request, jsonify
from datetime import datetime
import logging
from models.user import User, get_user, save_user, update_user

logger = logging.getLogger(__name__)
users_bp = Blueprint('users', __name__)


@users_bp.route('/profile', methods=['POST'])
def create_or_update_profile():
    """Create or update user profile"""
    try:
        data = request.get_json()

        if not data:
            return jsonify({'error': 'Profile data is required'}), 400

        user_id = data.get('user_id')
        name = data.get('name')
        location = data.get('location')
        situation = data.get('situation', 'unsheltered')
        primary_needs = data.get('primary_needs', [])
        previous_services = data.get('previous_services')

        # Validate situation
        valid_situations = ['housed', 'shelter',
                            'unsheltered', 'transitional', 'risk']
        if situation not in valid_situations:
            return jsonify({'error': f'Invalid situation. Must be one of: {", ".join(valid_situations)}'}), 400

        # Check if user exists
        user = None
        if user_id:
            user = get_user(user_id)

        if user:
            # Update existing user
            user.update_profile(
                name=name,
                location=location,
                situation=situation,
                primary_needs=primary_needs,
                previous_services=previous_services
            )
            save_user(user)
            action = 'updated'
        else:
            # Create new user
            user = User(
                name=name,
                location=location,
                situation=situation,
                primary_needs=primary_needs,
                previous_services=previous_services
            )
            save_user(user)
            action = 'created'

        return jsonify({
            'message': f'Profile {action} successfully',
            'user': user.to_dict(),
            'action': action
        }), 200 if action == 'updated' else 201

    except Exception as e:
        logger.error(f"Error in create_or_update_profile: {str(e)}")
        return jsonify({'error': 'Internal server error'}), 500


@users_bp.route('/profile/<user_id>', methods=['GET'])
def get_profile(user_id):
    """Get user profile by ID"""
    try:
        user = get_user(user_id)

        if not user:
            return jsonify({'error': 'User not found'}), 404

        return jsonify({
            'user': user.to_dict()
        })

    except Exception as e:
        logger.error(f"Error getting profile: {str(e)}")
        return jsonify({'error': 'Internal server error'}), 500


@users_bp.route('/profile/<user_id>', methods=['DELETE'])
def delete_profile(user_id):
    """Delete user profile (for privacy)"""
    try:
        user = get_user(user_id)

        if not user:
            return jsonify({'error': 'User not found'}), 404

        # For MVP, we'll just return success (in production, actually delete)
        # In a real implementation, you'd delete from database
        return jsonify({
            'message': 'Profile deleted successfully',
            'user_id': user_id
        })

    except Exception as e:
        logger.error(f"Error deleting profile: {str(e)}")
        return jsonify({'error': 'Internal server error'}), 500


@users_bp.route('/profile/<user_id>/context', methods=['GET'])
def get_user_context(user_id):
    """Get user context for AI interactions"""
    try:
        user = get_user(user_id)

        if not user:
            return jsonify({'error': 'User not found'}), 404

        context = user.get_context_for_ai()

        return jsonify({
            'context': context,
            'user_id': user_id
        })

    except Exception as e:
        logger.error(f"Error getting user context: {str(e)}")
        return jsonify({'error': 'Internal server error'}), 500
