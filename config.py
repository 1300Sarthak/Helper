import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Config:
    """Base configuration class"""
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your-secret-key-here')
    DEBUG = os.environ.get('DEBUG', 'True').lower() == 'true'
    PORT = int(os.environ.get('PORT', 5001))

    # CAG Chatbot Configuration
    CAG_API_KEY = os.environ.get('CAG_API_KEY', None)
    CAG_MODEL_NAME = os.environ.get('CAG_MODEL_NAME', 'default-model')
    CAG_API_URL = os.environ.get('CAG_API_URL', 'https://api.cag.example.com')

    # Database Configuration (if needed)
    DATABASE_URL = os.environ.get('DATABASE_URL', 'sqlite:///chatbot.db')
    REDIS_URL = os.environ.get('REDIS_URL', 'redis://localhost:6379')

    # Logging Configuration
    LOG_LEVEL = os.environ.get('LOG_LEVEL', 'INFO')


class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True


class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False


class TestingConfig(Config):
    """Testing configuration"""
    TESTING = True
    DEBUG = True


# Configuration dictionary
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
