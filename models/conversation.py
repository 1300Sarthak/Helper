from datetime import datetime
from .user import db


class Conversation(db.Model):
    """Conversation model for storing chat messages"""
    __tablename__ = 'conversations'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    message = db.Column(db.Text, nullable=False)
    response = db.Column(db.Text, nullable=True)  # Claude's response
    # 'user' or 'assistant'
    message_type = db.Column(db.String(20), default='user')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Context information
    context = db.Column(db.JSON, nullable=True)  # Store context as JSON

    def __repr__(self):
        return f'<Conversation {self.id}: User {self.user_id} - {self.message_type}>'

    def to_dict(self):
        """Convert conversation to dictionary for JSON responses"""
        return {
            'id': self.id,
            'user_id': self.user_id,
            'message': self.message,
            'response': self.response,
            'message_type': self.message_type,
            'context': self.context,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }
