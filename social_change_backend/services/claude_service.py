import os
import anthropic
import logging
from typing import Dict, Any, Optional
from datetime import datetime

logger = logging.getLogger(__name__)


class ClaudeService:
    """Service for interacting with Claude AI API"""

    def __init__(self):
        api_key = os.getenv('CLAUDE_API_KEY')
        if not api_key:
            logger.warning("CLAUDE_API_KEY not found in environment variables")
            self.client = None
        else:
            self.client = anthropic.Anthropic(api_key=api_key)

        self.model = "claude-3-sonnet-20240229"
        self.max_tokens = 1000

    def get_support_response(self, message: str, user_context: Dict[str, Any]) -> str:
        """Get support response from Claude"""
        system_prompt = self._build_support_prompt(user_context)
        return self._call_claude(message, system_prompt)

    def get_coach_response(self, message: str, user_context: Dict[str, Any]) -> str:
        """Get life coach response from Claude"""
        system_prompt = self._build_coach_prompt(user_context)
        return self._call_claude(message, system_prompt)

    def _call_claude(self, message: str, system_prompt: str) -> str:
        """Make API call to Claude"""
        if not self.client:
            return self._get_fallback_response()

        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=self.max_tokens,
                system=system_prompt,
                messages=[{"role": "user", "content": message}]
            )

            return response.content[0].text

        except Exception as e:
            logger.error(f"Error calling Claude API: {str(e)}")
            return self._get_fallback_response()

    def _build_support_prompt(self, user_context: Dict[str, Any]) -> str:
        """Build system prompt for support mode"""
        base_prompt = f"""
You are a compassionate AI assistant for "For Social Change," a platform helping people experiencing homelessness or housing insecurity.

Your role:
- Provide empathetic, non-judgmental support
- Offer practical resource recommendations
- Maintain dignity and respect in all interactions
- Prioritize immediate safety and basic needs
- Connect users with local services

User Context:
- Location: {user_context.get('location', 'Not specified')}
- Current Situation: {user_context.get('situation', 'Not specified')}
- Primary Needs: {', '.join(user_context.get('primaryNeeds', []))}
- Name: {user_context.get('name', 'Anonymous')}

Guidelines:
- Keep responses conversational and supportive
- Provide specific, actionable advice when possible
- If user mentions crisis/danger, prioritize safety resources
- Ask clarifying questions to better understand needs
- Be encouraging and hopeful while remaining realistic
- Focus on immediate practical steps they can take
- Suggest local resources when appropriate

Remember: You are speaking with someone who may be in a vulnerable situation. Always prioritize their safety and dignity.
"""
        return base_prompt

    def _build_coach_prompt(self, user_context: Dict[str, Any]) -> str:
        """Build system prompt for life coach mode"""
        support_prompt = self._build_support_prompt(user_context)

        coach_addition = """

LIFE COACH MODE - Additional Guidelines:
- Focus on goal-setting and personal development
- Encourage small, achievable steps toward their goals
- Provide motivational support and positive reinforcement
- Help user identify their strengths and available resources
- Guide them in creating action plans
- Celebrate progress, no matter how small
- Help them envision a better future
- Support them in building confidence and self-efficacy
- Ask empowering questions that help them think through solutions
- Encourage them to take ownership of their journey

Remember: In life coach mode, you're helping them build a path forward while acknowledging their current challenges.
"""
        return support_prompt + coach_addition

    def _get_fallback_response(self) -> str:
        """Get fallback response when Claude API is unavailable"""
        fallback_responses = [
            "I'm here to help you. Could you tell me more about what you need assistance with?",
            "I want to support you. What's on your mind right now?",
            "I'm listening and ready to help. What would you like to talk about?",
            "You're not alone. I'm here to help you find resources and support.",
            "Let's work together to find solutions. What's your biggest concern right now?"
        ]

        import random
        return random.choice(fallback_responses)

    def detect_crisis_keywords(self, message: str) -> bool:
        """Detect crisis keywords in user message"""
        crisis_keywords = [
            'suicide', 'kill myself', 'end it all', 'want to die',
            'hurt myself', 'self-harm', 'overdose', 'dangerous',
            'emergency', 'crisis', 'help me', 'desperate',
            'no hope', 'give up', 'can\'t take it anymore'
        ]

        message_lower = message.lower()
        return any(keyword in message_lower for keyword in crisis_keywords)

    def get_crisis_response(self) -> str:
        """Get appropriate crisis response"""
        return """
I'm concerned about what you're going through. You're not alone, and there are people who want to help you.

If you're in immediate danger, please call 911 or go to the nearest emergency room.

For crisis support, you can call:
- National Suicide Prevention Lifeline: 988 (24/7)
- Crisis Text Line: Text HOME to 741741
- Emergency: 911

These services are free, confidential, and available 24/7. Please reach out to them - they're there to help you through this difficult time.

Would you like me to help you find local crisis resources in your area?
"""
