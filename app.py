from flask import Flask, jsonify
import os
from datetime import datetime
import logging
from config import config

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Load configuration
config_name = os.environ.get('FLASK_ENV', 'default')
app_config = config[config_name]
app.config.from_object(app_config)


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
