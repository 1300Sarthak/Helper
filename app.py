from flask import Flask, jsonify
import os
from datetime import datetime
import logging
from config import config
from models.user import db, User
from models.conversation import Conversation
from routes.chat import chat_bp

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Load configuration
config_name = os.environ.get('FLASK_ENV', 'default')
app_config = config[config_name]
app.config.from_object(app_config)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///social_change_app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db.init_app(app)

# Register blueprints
app.register_blueprint(chat_bp)

# Create tables
with app.app_context():
    db.create_all()


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
