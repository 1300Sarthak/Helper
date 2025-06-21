import re
import logging
from typing import Dict, Any, List, Optional
from datetime import datetime

logger = logging.getLogger(__name__)


def sanitize_input(text: str) -> str:
    """Sanitize user input to prevent injection attacks"""
    if not text:
        return ""

    # Remove potentially dangerous characters
    sanitized = re.sub(r'[<>"\']', '', text)
    return sanitized.strip()


def validate_email(email: str) -> bool:
    """Validate email format"""
    if not email:
        return False

    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))


def validate_phone(phone: str) -> bool:
    """Validate phone number format"""
    if not phone:
        return False

    # Remove all non-digit characters
    digits_only = re.sub(r'\D', '', phone)
    return len(digits_only) >= 10


def format_timestamp(timestamp: datetime) -> str:
    """Format timestamp for API responses"""
    if not timestamp:
        return None

    return timestamp.isoformat()


def parse_location(location: str) -> Dict[str, str]:
    """Parse location string into components"""
    if not location:
        return {"city": "", "state": "", "full": ""}

    parts = location.split(',')
    if len(parts) >= 2:
        city = parts[0].strip()
        state = parts[1].strip()
        return {
            "city": city,
            "state": state,
            "full": location.strip()
        }
    else:
        return {
            "city": location.strip(),
            "state": "",
            "full": location.strip()
        }


def detect_crisis_keywords(text: str) -> List[str]:
    """Detect crisis-related keywords in text"""
    crisis_keywords = [
        'suicide', 'kill myself', 'end it all', 'want to die',
        'hurt myself', 'self-harm', 'overdose', 'dangerous',
        'emergency', 'crisis', 'help me', 'desperate',
        'no hope', 'give up', 'can\'t take it anymore',
        'homeless', 'hungry', 'cold', 'sick', 'injured'
    ]

    found_keywords = []
    text_lower = text.lower()

    for keyword in crisis_keywords:
        if keyword in text_lower:
            found_keywords.append(keyword)

    return found_keywords


def calculate_distance(lat1: float, lng1: float, lat2: float, lng2: float) -> float:
    """Calculate distance between two coordinates (Haversine formula)"""
    import math

    # Convert to radians
    lat1_rad = math.radians(lat1)
    lng1_rad = math.radians(lng1)
    lat2_rad = math.radians(lat2)
    lng2_rad = math.radians(lng2)

    # Haversine formula
    dlat = lat2_rad - lat1_rad
    dlng = lng2_rad - lng1_rad
    a = math.sin(dlat/2)**2 + math.cos(lat1_rad) * \
        math.cos(lat2_rad) * math.sin(dlng/2)**2
    c = 2 * math.asin(math.sqrt(a))

    # Earth's radius in miles
    r = 3956

    return c * r


def format_phone_number(phone: str) -> str:
    """Format phone number for display"""
    if not phone:
        return ""

    # Remove all non-digit characters
    digits = re.sub(r'\D', '', phone)

    if len(digits) == 10:
        return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
    elif len(digits) == 11 and digits[0] == '1':
        return f"+1 ({digits[1:4]}) {digits[4:7]}-{digits[7:]}"
    else:
        return phone


def truncate_text(text: str, max_length: int = 100) -> str:
    """Truncate text to specified length"""
    if not text or len(text) <= max_length:
        return text

    return text[:max_length-3] + "..."


def generate_user_id() -> str:
    """Generate a unique user ID"""
    import uuid
    return str(uuid.uuid4())


def is_valid_situation(situation: str) -> bool:
    """Validate user situation"""
    valid_situations = ['housed', 'shelter',
                        'unsheltered', 'transitional', 'risk']
    return situation in valid_situations


def log_user_interaction(user_id: str, action: str, details: Dict[str, Any] = None):
    """Log user interactions for analytics (privacy-conscious)"""
    try:
        log_data = {
            "timestamp": datetime.utcnow().isoformat(),
            "user_id": user_id,
            "action": action,
            "details": details or {}
        }

        # In production, this would go to a proper logging service
        logger.info(f"User interaction: {log_data}")

    except Exception as e:
        logger.error(f"Error logging user interaction: {str(e)}")


def get_safe_user_data(user_data: Dict[str, Any]) -> Dict[str, Any]:
    """Get user data with sensitive information removed"""
    safe_fields = ['user_id', 'name', 'location',
                   'situation', 'primary_needs', 'created_at']

    safe_data = {}
    for field in safe_fields:
        if field in user_data:
            safe_data[field] = user_data[field]

    return safe_data
