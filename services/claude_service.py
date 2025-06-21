# Claude 4 calls, prompt templates

import os
import logging
from typing import Dict, Any, Optional
import requests
import json
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

logger = logging.getLogger(__name__)


class ClaudeService:
    """Service for interacting with Claude API"""

    def __init__(self):
        self.api_key = os.environ.get('CLAUDE_API_KEY')
        self.api_url = "https://api.anthropic.com/v1/messages"
        self.model = "claude-3-5-sonnet-20241022"

        if not self.api_key:
            logger.warning("CLAUDE_API_KEY not set in environment variables")

    def get_support_response(self, message: str, context: Optional[Dict[str, Any]] = None) -> str:
        """
        Generate a supportive response using Claude API

        Args:
            message: User's input message
            context: Optional context information (user situation, location, etc.)

        Returns:
            Claude's response as a string
        """
        try:
            if not self.api_key:
                return self._fallback_response(message)

            # Build the system prompt for social change assistance
            system_prompt = self._build_system_prompt(context)

            # Prepare the API request
            headers = {
                "Content-Type": "application/json",
                "x-api-key": self.api_key,
                "anthropic-version": "2023-06-01"
            }

            payload = {
                "model": self.model,
                "max_tokens": 1000,
                "system": system_prompt,
                "messages": [
                    {
                        "role": "user",
                        "content": message
                    }
                ]
            }

            logger.info(
                f"Sending request to Claude API for message: {message[:50]}...")

            response = requests.post(
                self.api_url,
                headers=headers,
                json=payload,
                timeout=30
            )

            if response.status_code == 200:
                response_data = response.json()
                claude_response = response_data['content'][0]['text']
                logger.info("Successfully received response from Claude API")
                return claude_response
            else:
                logger.error(
                    f"Claude API error: {response.status_code} - {response.text}")
                return self._fallback_response(message)

        except requests.exceptions.RequestException as e:
            logger.error(f"Network error calling Claude API: {str(e)}")
            return self._fallback_response(message)
        except Exception as e:
            logger.error(f"Unexpected error in Claude service: {str(e)}")
            return self._fallback_response(message)

    def _build_system_prompt(self, context: Optional[Dict[str, Any]] = None) -> str:
        """Build the system prompt for Claude based on context"""
        base_prompt = """You are a compassionate AI assistant for a social change app that helps people in difficult situations. Your role is to:

1. Provide warm, empathetic support using motivational interviewing techniques
2. Help users find local resources (food banks, shelters, clinics, job assistance)
3. Offer practical guidance and emotional support
4. Maintain hope and dignity in all interactions
5. Be non-judgmental and respectful

Always respond with empathy and practical help. Keep responses concise but caring."""

        if context:
            context_info = ""
            if context.get('location'):
                context_info += f"\nUser location: {context['location']}"
            if context.get('situation'):
                context_info += f"\nUser situation: {context['situation']}"
            if context.get('needs'):
                context_info += f"\nUser needs: {context['needs']}"

            if context_info:
                base_prompt += f"\n\nUser Context:{context_info}"

        return base_prompt

    def _fallback_response(self, message: str) -> str:
        """Fallback response when Claude API is unavailable"""
        return f"I understand you're reaching out for support. While I'm having trouble connecting to my full capabilities right now, I want you to know that your message is important. You mentioned: '{message}'. Please know that help is available, and you're taking a positive step by seeking support. Is there something specific I can try to help you with right now?"


# Global instance
claude_service = ClaudeService()


def get_support_response(message: str, context: Optional[Dict[str, Any]] = None) -> str:
    """
    Main function to get support response from Claude
    This is the function required by Task 3
    """
    return claude_service.get_support_response(message, context)
