# User info schema

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class User(db.Model):
    """User model for storing user information"""
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=True)
    location = db.Column(db.String(200), nullable=True)  # City, zip code, etc.
    # Current situation description
    situation = db.Column(db.Text, nullable=True)
    needs = db.Column(db.Text, nullable=True)  # What kind of help they need
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationship to conversations
    conversations = db.relationship(
        'Conversation', backref='user', lazy=True, cascade='all, delete-orphan')

    def __repr__(self):
        return f'<User {self.id}: {self.name or "Anonymous"}>'

    def to_dict(self):
        """Convert user to dictionary for JSON responses"""
        return {
            'id': self.id,
            'name': self.name,
            'location': self.location,
            'situation': self.situation,
            'needs': self.needs,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }
