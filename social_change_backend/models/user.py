from datetime import datetime
from typing import Optional, List
import json


class User:
    """User model for storing profile information"""

    def __init__(self,
                 user_id: str = None,
                 name: Optional[str] = None,
                 location: Optional[str] = None,
                 situation: str = 'unsheltered',
                 primary_needs: List[str] = None,
                 previous_services: Optional[str] = None,
                 created_at: datetime = None,
                 updated_at: datetime = None):

        self.user_id = user_id or self._generate_user_id()
        self.name = name
        self.location = location
        self.situation = situation
        self.primary_needs = primary_needs or []
        self.previous_services = previous_services
        self.created_at = created_at or datetime.utcnow()
        self.updated_at = updated_at or datetime.utcnow()

    def _generate_user_id(self) -> str:
        """Generate a unique user ID"""
        import uuid
        return str(uuid.uuid4())

    def to_dict(self) -> dict:
        """Convert user to dictionary"""
        return {
            'user_id': self.user_id,
            'name': self.name,
            'location': self.location,
            'situation': self.situation,
            'primary_needs': self.primary_needs,
            'previous_services': self.previous_services,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'User':
        """Create user from dictionary"""
        created_at = datetime.fromisoformat(
            data['created_at']) if data.get('created_at') else None
        updated_at = datetime.fromisoformat(
            data['updated_at']) if data.get('updated_at') else None

        return cls(
            user_id=data.get('user_id'),
            name=data.get('name'),
            location=data.get('location'),
            situation=data.get('situation', 'unsheltered'),
            primary_needs=data.get('primary_needs', []),
            previous_services=data.get('previous_services'),
            created_at=created_at,
            updated_at=updated_at
        )

    def update_profile(self, **kwargs) -> None:
        """Update user profile fields"""
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.updated_at = datetime.utcnow()

    def get_context_for_ai(self) -> dict:
        """Get user context formatted for AI prompts"""
        return {
            'location': self.location or 'Not specified',
            'situation': self.situation,
            'primaryNeeds': self.primary_needs,
            'name': self.name or 'Anonymous'
        }


# In-memory storage for MVP (replace with database in production)
_users_storage = {}


def get_user(user_id: str) -> Optional[User]:
    """Get user by ID"""
    return _users_storage.get(user_id)


def save_user(user: User) -> User:
    """Save user to storage"""
    _users_storage[user.user_id] = user
    return user


def update_user(user_id: str, **kwargs) -> Optional[User]:
    """Update user profile"""
    user = get_user(user_id)
    if user:
        user.update_profile(**kwargs)
        save_user(user)
    return user
