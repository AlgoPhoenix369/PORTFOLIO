# Production configuration for Flask backend
import os

class ProductionConfig:
    """Production configuration settings"""
    
    # Flask settings
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.getenv('SECRET_KEY')
    
    # Database
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_recycle': 300,
        'pool_pre_ping': True,
    }
    
    # Supabase
    SUPABASE_URL = os.getenv('SUPABASE_URL')
    SUPABASE_KEY = os.getenv('SUPABASE_KEY')
    
    # CORS
    CORS_ORIGINS = os.getenv('CORS_ORIGINS', '').split(',')
    
    # Security
    SESSION_COOKIE_SECURE = True
    REMEMBER_COOKIE_SECURE = True
    
    # Rate limiting (optional, requires Flask-Limiter)
    # RATELIMIT_DEFAULT = "100 per hour"


class DevelopmentConfig:
    """Development configuration settings"""
    
    DEBUG = True
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key')
    
    # Database
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URL', 
        'postgresql://postgres:postgres@localhost:5432/portfolio_db'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Supabase
    SUPABASE_URL = os.getenv('SUPABASE_URL')
    SUPABASE_KEY = os.getenv('SUPABASE_KEY')
    
    # CORS
    CORS_ORIGINS = ['http://localhost:3000', 'http://localhost:5173']


class TestingConfig:
    """Testing configuration settings"""
    
    TESTING = True
    DEBUG = True
    SECRET_KEY = 'test-secret-key'
    
    # Use SQLite for testing
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Disable CSRF for testing
    WTF_CSRF_ENABLED = False


config = {
    'production': ProductionConfig,
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
