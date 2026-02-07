# Configuration settings for Hotel Management System

class Config:
    # Secret key for Flask application
    SECRET_KEY = 'your-secret-key'
    
    # Database configuration
    SQLALCHEMY_DATABASE_URI = 'sqlite:///hotel.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Flask-Login configuration
    LOGIN_DISABLED = False
    
    # Flask-WTF configuration
    WTF_CSRF_ENABLED = True
    
    # Application settings
    APP_NAME = 'Hotel Management System'
    DEBUG = True