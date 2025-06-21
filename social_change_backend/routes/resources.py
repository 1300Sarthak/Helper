from flask import Blueprint, request, jsonify
import logging
from services.resource_service import ResourceService

logger = logging.getLogger(__name__)
resources_bp = Blueprint('resources', __name__)

# Initialize resource service
resource_service = ResourceService()


@resources_bp.route('/search', methods=['GET'])
def search_resources():
    """Search for local resources based on location and needs"""
    try:
        location = request.args.get('location', '')
        needs = request.args.get('needs', '')
        resource_type = request.args.get('type', '')

        if not location:
            return jsonify({'error': 'Location is required'}), 400

        # Parse needs as comma-separated list
        needs_list = [need.strip() for need in needs.split(',')
                      if need.strip()] if needs else []

        # Search for resources
        resources = resource_service.search_resources(
            location=location,
            needs=needs_list,
            resource_type=resource_type
        )

        return jsonify({
            'resources': resources,
            'search_params': {
                'location': location,
                'needs': needs_list,
                'type': resource_type
            },
            'total_count': len(resources)
        })

    except Exception as e:
        logger.error(f"Error searching resources: {str(e)}")
        return jsonify({'error': 'Internal server error'}), 500


@resources_bp.route('/quick-actions', methods=['GET'])
def get_quick_actions():
    """Get quick action resources for common needs"""
    try:
        location = request.args.get('location', '')

        quick_actions = resource_service.get_quick_actions(location)

        return jsonify({
            'quick_actions': quick_actions,
            'location': location
        })

    except Exception as e:
        logger.error(f"Error getting quick actions: {str(e)}")
        return jsonify({'error': 'Internal server error'}), 500


@resources_bp.route('/categories', methods=['GET'])
def get_resource_categories():
    """Get available resource categories"""
    try:
        categories = resource_service.get_categories()

        return jsonify({
            'categories': categories
        })

    except Exception as e:
        logger.error(f"Error getting categories: {str(e)}")
        return jsonify({'error': 'Internal server error'}), 500


@resources_bp.route('/nearby/<location>', methods=['GET'])
def get_nearby_resources(location):
    """Get resources near a specific location"""
    try:
        if not location:
            return jsonify({'error': 'Location is required'}), 400

        nearby_resources = resource_service.get_nearby_resources(location)

        return jsonify({
            'location': location,
            'resources': nearby_resources,
            'total_count': len(nearby_resources)
        })

    except Exception as e:
        logger.error(f"Error getting nearby resources: {str(e)}")
        return jsonify({'error': 'Internal server error'}), 500


@resources_bp.route('/crisis', methods=['GET'])
def get_crisis_resources():
    """Get crisis resources and hotlines"""
    try:
        location = request.args.get('location', '')

        crisis_resources = resource_service.get_crisis_resources(location)

        return jsonify({
            'crisis_resources': crisis_resources,
            'location': location
        })

    except Exception as e:
        logger.error(f"Error getting crisis resources: {str(e)}")
        return jsonify({'error': 'Internal server error'}), 500
