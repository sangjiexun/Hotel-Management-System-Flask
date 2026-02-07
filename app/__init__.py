# Application initialization for Hotel Management System

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Create Flask application instance
app = Flask(__name__)

# Load configuration
app.config.from_object('config')

# Initialize extensions
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Import models
from app.models import User, Team, Room, Meeting, CostLog, Participants_user, Participants_partner, Businesspartner

# Import routes
from app.routes import *