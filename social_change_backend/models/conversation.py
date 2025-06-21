from datetime import datetime
from typing import List, Optional
import uuid


class ChatMessage:
    """Individual chat message model"""

    def __init__(self,
                 message_id: str = None,
                 content: str = "",
                 sender: str = "user",  # "user" or "assistant"
                 timestamp: datetime = None,
                 mode: str = "support"):  # "support" or "coach"

        self.message_id = message_id or str(uuid.uuid4())
        self.content = content
        self.sender = sender
        self.timestamp = timestamp or datetime.utcnow()
        self.mode = mode

    def to_dict(self) -> dict:
        """Convert message to dictionary"""
        return {
            'message_id': self.message_id,
            'content': self.content,
            'sender': self.sender,
            'timestamp': self.timestamp.isoformat(),
            'mode': self.mode
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'ChatMessage':
        """Create message from dictionary"""
        timestamp = datetime.fromisoformat(
            data['timestamp']) if data.get('timestamp') else None

        return cls(
            message_id=data.get('message_id'),
            content=data.get('content', ''),
            sender=data.get('sender', 'user'),
            timestamp=timestamp,
            mode=data.get('mode', 'support')
        )


class Conversation:
    """Conversation model for storing chat sessions"""

    def __init__(self,
                 conversation_id: str = None,
                 user_id: str = None,
                 messages: List[ChatMessage] = None,
                 created_at: datetime = None,
                 updated_at: datetime = None):

        self.conversation_id = conversation_id or str(uuid.uuid4())
        self.user_id = user_id
        self.messages = messages or []
        self.created_at = created_at or datetime.utcnow()
        self.updated_at = updated_at or datetime.utcnow()

    def add_message(self, content: str, sender: str = "user", mode: str = "support") -> ChatMessage:
        """Add a new message to the conversation"""
        message = ChatMessage(content=content, sender=sender, mode=mode)
        self.messages.append(message)
        self.updated_at = datetime.utcnow()
        return message

    def get_recent_messages(self, limit: int = 10) -> List[ChatMessage]:
        """Get recent messages for context"""
        return self.messages[-limit:] if self.messages else []

    def get_messages_by_mode(self, mode: str) -> List[ChatMessage]:
        """Get messages filtered by mode"""
        return [msg for msg in self.messages if msg.mode == mode]

    def to_dict(self) -> dict:
        """Convert conversation to dictionary"""
        return {
            'conversation_id': self.conversation_id,
            'user_id': self.user_id,
            'messages': [msg.to_dict() for msg in self.messages],
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'Conversation':
        """Create conversation from dictionary"""
        created_at = datetime.fromisoformat(
            data['created_at']) if data.get('created_at') else None
        updated_at = datetime.fromisoformat(
            data['updated_at']) if data.get('updated_at') else None

        messages = [ChatMessage.from_dict(msg_data)
                    for msg_data in data.get('messages', [])]

        return cls(
            conversation_id=data.get('conversation_id'),
            user_id=data.get('user_id'),
            messages=messages,
            created_at=created_at,
            updated_at=updated_at
        )


# In-memory storage for MVP (replace with database in production)
_conversations_storage = {}


def get_conversation(conversation_id: str) -> Optional[Conversation]:
    """Get conversation by ID"""
    return _conversations_storage.get(conversation_id)


def get_user_conversation(user_id: str) -> Optional[Conversation]:
    """Get or create conversation for user"""
    # For MVP, we'll use a simple approach - one conversation per user
    for conv in _conversations_storage.values():
        if conv.user_id == user_id:
            return conv

    # Create new conversation if none exists
    conversation = Conversation(user_id=user_id)
    _conversations_storage[conversation.conversation_id] = conversation
    return conversation


def save_conversation(conversation: Conversation) -> Conversation:
    """Save conversation to storage"""
    _conversations_storage[conversation.conversation_id] = conversation
    return conversation
