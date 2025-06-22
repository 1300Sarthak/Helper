# Claude 4 calls, prompt templates

import os
import logging
from typing import Dict, Any, Optional, List
import requests
import json
from dotenv import load_dotenv
from datetime import datetime
from .rag_pipeline import rag_pipeline

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
        Generate a supportive response using Claude API with RAG enhancement

        Args:
            message: User's input message
            context: Optional context information (user situation, location, etc.)

        Returns:
            Claude's response as a string
        """
        try:
            if not self.api_key:
                return self._fallback_response(message)

            # Get local resources via RAG pipeline
            rag_context = ""
            if context and context.get('location'):
                needs = self._extract_needs_from_message(message, context)
                rag_results = rag_pipeline.retrieve_resources(
                    context.get('location'),
                    needs,
                    context.get('situation')
                )
                rag_context = rag_pipeline.format_resources_for_claude(
                    rag_results)
                logger.info(
                    f"RAG retrieved {rag_results.get('total_resources', 0)} resources")

            # Build the enhanced system prompt
            system_prompt = self._build_enhanced_system_prompt(
                context, rag_context)

            # Prepare the API request
            headers = {
                "Content-Type": "application/json",
                "x-api-key": self.api_key,
                "anthropic-version": "2023-06-01"
            }

            payload = {
                "model": self.model,
                "max_tokens": 1200,  # Increased for more detailed responses
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

    def analyze_journal_entry(self, journal_text: str, user_context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Analyze a journal entry for emotion scoring and insights using Claude

        Args:
            journal_text: The journal entry text
            user_context: Optional user context for personalized analysis

        Returns:
            Dictionary with emotion scores, insights, and suggestions
        """
        try:
            if not self.api_key:
                return self._fallback_analysis(journal_text)

            prompt = f"""Analyze this journal entry and provide insights in JSON format:

Journal Entry: "{journal_text}"

Please analyze and respond with ONLY a valid JSON object containing:
{{
    "emotion_scores": {{
        "distress": 0.0-1.0,
        "hope": 0.0-1.0,
        "motivation": 0.0-1.0,
        "anxiety": 0.0-1.0,
        "positivity": 0.0-1.0
    }},
    "key_themes": ["theme1", "theme2", "theme3"],
    "insights": "Brief insight about the person's emotional state",
    "suggestions": "Supportive suggestions for improvement",
    "urgency_level": "low|medium|high"
}}"""

            if user_context:
                prompt += f"\n\nUser Context: {user_context.get('situation', '')} in {user_context.get('location', '')}"

            response = self._call_claude_api(prompt, max_tokens=800)
            if response:
                return self._parse_json_response(response, self._fallback_analysis(journal_text))
            else:
                return self._fallback_analysis(journal_text)

        except Exception as e:
            logger.error(f"Error analyzing journal entry: {str(e)}")
            return self._fallback_analysis(journal_text)

    def summarize_conversation(self, messages: List[Dict[str, str]], user_context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Summarize a conversation for context and insights using Claude

        Args:
            messages: List of message dictionaries with 'role' and 'content'
            user_context: Optional user context

        Returns:
            Dictionary with summary, key themes, and recommendations
        """
        try:
            if not self.api_key:
                return self._fallback_summary(messages)

            conversation = "\n".join(
                [f"{msg.get('role', 'user')}: {msg.get('content', '')}" for msg in messages[-10:]])  # Last 10 messages

            prompt = f"""Summarize this conversation and provide insights in JSON format:

Conversation:
{conversation}

Please analyze and respond with ONLY a valid JSON object containing:
{{
    "summary": "Brief summary of the conversation",
    "user_needs": ["need1", "need2", "need3"],
    "emotional_tone": "overall emotional tone",
    "progress_indicators": ["positive sign1", "positive sign2"],
    "recommendations": ["recommendation1", "recommendation2"],
    "follow_up_needed": true/false
}}"""

            if user_context:
                prompt += f"\n\nUser Context: {user_context.get('situation', '')} in {user_context.get('location', '')}"

            response = self._call_claude_api(prompt, max_tokens=800)
            if response:
                return self._parse_json_response(response, self._fallback_summary(messages))
            else:
                return self._fallback_summary(messages)

        except Exception as e:
            logger.error(f"Error summarizing conversation: {str(e)}")
            return self._fallback_summary(messages)

    def score_emotional_state(self, text: str) -> Dict[str, float]:
        """
        Score emotional state from text using Claude

        Args:
            text: Text to analyze

        Returns:
            Dictionary with emotion scores (0-1 scale)
        """
        try:
            if not self.api_key:
                return self._fallback_emotion_scores()

            prompt = f"""Score the emotional content of this text on a 0-1 scale and respond with ONLY a valid JSON object:

Text: "{text}"

Respond with:
{{
    "distress": 0.0-1.0,
    "hope": 0.0-1.0,
    "motivation": 0.0-1.0,
    "anxiety": 0.0-1.0,
    "positivity": 0.0-1.0,
    "overall_sentiment": "positive|neutral|negative"
}}"""

            response = self._call_claude_api(prompt, max_tokens=400)
            if response:
                return self._parse_json_response(response, self._fallback_emotion_scores())
            else:
                return self._fallback_emotion_scores()

        except Exception as e:
            logger.error(f"Error scoring emotional state: {str(e)}")
            return self._fallback_emotion_scores()

    def _call_claude_api(self, prompt: str, max_tokens: int = 1200) -> Optional[str]:
        """Make API call to Claude for analysis tasks"""
        try:
            headers = {
                "Content-Type": "application/json",
                "x-api-key": self.api_key,
                "anthropic-version": "2023-06-01"
            }

            payload = {
                "model": self.model,
                "max_tokens": max_tokens,
                "messages": [
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            }

            response = requests.post(
                self.api_url,
                headers=headers,
                json=payload,
                timeout=30
            )

            if response.status_code == 200:
                response_data = response.json()
                return response_data['content'][0]['text']
            else:
                logger.error(
                    f"Claude API error: {response.status_code} - {response.text}")
                return None

        except Exception as e:
            logger.error(f"Error calling Claude API: {str(e)}")
            return None

    def _parse_json_response(self, response: str, fallback: Dict[str, Any]) -> Dict[str, Any]:
        """Parse JSON response from Claude"""
        try:
            # Clean up response
            response_clean = response.strip()
            if response_clean.startswith('```json'):
                response_clean = response_clean[7:-3]
            elif response_clean.startswith('```'):
                response_clean = response_clean[3:-3]

            parsed = json.loads(response_clean)

            # Add metadata
            parsed['timestamp'] = datetime.now().isoformat()
            parsed['source'] = 'claude'

            return parsed

        except json.JSONDecodeError as e:
            logger.error(f"Failed to parse Claude JSON response: {str(e)}")
            return fallback

    def _extract_needs_from_message(self, message: str, context: Optional[Dict[str, Any]] = None) -> List[str]:
        """Extract needs from user message and context"""
        needs = []
        message_lower = message.lower()

        # Extract from message
        if any(word in message_lower for word in ["food", "hungry", "eat", "meal"]):
            needs.append("food")
        if any(word in message_lower for word in ["shelter", "housing", "sleep", "bed", "place to stay"]):
            needs.append("shelter")
        if any(word in message_lower for word in ["health", "medical", "doctor", "clinic", "sick"]):
            needs.append("healthcare")
        if any(word in message_lower for word in ["job", "work", "employment", "career"]):
            needs.append("employment")

        # Extract from context
        if context and context.get('needs'):
            context_needs = context['needs'].lower()
            if any(word in context_needs for word in ["food", "hungry", "eat"]):
                needs.append("food")
            if any(word in context_needs for word in ["shelter", "housing", "sleep"]):
                needs.append("shelter")
            if any(word in context_needs for word in ["health", "medical"]):
                needs.append("healthcare")
            if any(word in context_needs for word in ["job", "work", "employment"]):
                needs.append("employment")

        # Default to food if no specific needs detected
        if not needs:
            needs = ["food"]

        return list(set(needs))  # Remove duplicates

    def _build_enhanced_system_prompt(self, context: Optional[Dict[str, Any]] = None, rag_context: str = "") -> str:
        """Build enhanced system prompt with RAG context"""
        base_prompt = """You are a compassionate AI assistant for a social change app that helps people in difficult situations. Your role is to:

1. Provide warm, empathetic support using motivational interviewing techniques
2. Help users find local resources (food banks, shelters, clinics, job assistance)
3. Offer practical guidance and emotional support
4. Maintain hope and dignity in all interactions
5. Be non-judgmental and respectful

Always respond with empathy and practical help. Use specific local resource information when available."""

        # Add user context
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

        # Add RAG context with local resources
        if rag_context:
            base_prompt += f"\n\nLocal Resources Available:\n{rag_context}"
            base_prompt += "\nUse these specific local resources in your response. Provide exact addresses, phone numbers, and hours when available."

        return base_prompt

    def _build_system_prompt(self, context: Optional[Dict[str, Any]] = None) -> str:
        """Build the system prompt for Claude based on context (legacy method)"""
        return self._build_enhanced_system_prompt(context, "")

    def _fallback_response(self, message: str) -> str:
        """Fallback response when Claude API is unavailable"""
        return f"I understand you're reaching out for support. While I'm having trouble connecting to my full capabilities right now, I want you to know that your message is important. You mentioned: '{message}'. Please know that help is available, and you're taking a positive step by seeking support. Is there something specific I can try to help you with right now?"

    def _fallback_analysis(self, journal_text: str) -> Dict[str, Any]:
        """Fallback analysis when Claude is unavailable"""
        # Simple keyword-based analysis
        text_lower = journal_text.lower()

        distress_words = ['sad', 'depressed', 'anxious', 'worried',
                          'scared', 'hopeless', 'difficult', 'hard', 'struggle']
        hope_words = ['better', 'hope', 'improve', 'positive',
                      'good', 'happy', 'grateful', 'thankful']

        distress_score = min(sum(
            1 for word in distress_words if word in text_lower) / len(distress_words), 1.0)
        hope_score = min(
            sum(1 for word in hope_words if word in text_lower) / len(hope_words), 1.0)

        return {
            "emotion_scores": {
                "distress": distress_score,
                "hope": hope_score,
                "motivation": 0.5,
                "anxiety": min(distress_score * 0.8, 1.0),
                "positivity": min(hope_score * 1.2, 1.0)
            },
            "key_themes": ["personal reflection"],
            "insights": "Journal entry reflects personal thoughts and experiences",
            "suggestions": "Continue journaling to track your emotional journey",
            "urgency_level": "low",
            "timestamp": datetime.now().isoformat(),
            "source": "fallback"
        }

    def _fallback_summary(self, messages: List[Dict]) -> Dict[str, Any]:
        """Fallback summary when Claude is unavailable"""
        return {
            "summary": f"Conversation with {len(messages)} messages about support and resources",
            "user_needs": ["support", "resources"],
            "emotional_tone": "seeking assistance",
            "progress_indicators": ["reaching out for help"],
            "recommendations": ["continue conversation", "follow up on resources"],
            "follow_up_needed": True,
            "timestamp": datetime.now().isoformat(),
            "source": "fallback"
        }

    def _fallback_emotion_scores(self) -> Dict[str, float]:
        """Fallback emotion scores when Claude is unavailable"""
        return {
            "distress": 0.5,
            "hope": 0.5,
            "motivation": 0.5,
            "anxiety": 0.5,
            "positivity": 0.5,
            "overall_sentiment": "neutral",
            "source": "fallback"
        }


# Global instance
claude_service = ClaudeService()


def get_support_response(message: str, context: Optional[Dict[str, Any]] = None) -> str:
    """
    Main function to get support response from Claude
    This is the function required by Task 3
    """
    return claude_service.get_support_response(message, context)


def analyze_journal_entry(journal_text: str, user_context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Main function to analyze journal entries using Claude"""
    return claude_service.analyze_journal_entry(journal_text, user_context)


def summarize_conversation(messages: List[Dict[str, str]], user_context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Main function to summarize conversations using Claude"""
    return claude_service.summarize_conversation(messages, user_context)


def score_emotional_state(text: str) -> Dict[str, float]:
    """Main function to score emotional state using Claude"""
    return claude_service.score_emotional_state(text)
