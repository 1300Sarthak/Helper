# Gemini summarization/emotion scoring

import os
import logging
from typing import Dict, Any, Optional, List
import requests
import json
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables from .env file
load_dotenv()

logger = logging.getLogger(__name__)


class GeminiService:
    """Service for interacting with Google Gemini API for summarization and emotion analysis"""

    def __init__(self):
        self.api_key = os.environ.get('GEMINI_API_KEY')
        self.api_url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent"

        if not self.api_key:
            logger.warning("GEMINI_API_KEY not set in environment variables")

    def analyze_journal_entry(self, journal_text: str, user_context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Analyze a journal entry for emotion scoring and insights

        Args:
            journal_text: The journal entry text
            user_context: Optional user context for personalized analysis

        Returns:
            Dictionary with emotion scores, insights, and suggestions
        """
        try:
            if not self.api_key:
                return self._fallback_analysis(journal_text)

            prompt = self._build_journal_analysis_prompt(
                journal_text, user_context)

            response = self._call_gemini_api(prompt)
            if response:
                return self._parse_journal_analysis(response, journal_text)
            else:
                return self._fallback_analysis(journal_text)

        except Exception as e:
            logger.error(f"Error analyzing journal entry: {str(e)}")
            return self._fallback_analysis(journal_text)

    def summarize_conversation(self, messages: List[Dict[str, str]], user_context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Summarize a conversation for context and insights

        Args:
            messages: List of message dictionaries with 'role' and 'content'
            user_context: Optional user context

        Returns:
            Dictionary with summary, key themes, and recommendations
        """
        try:
            if not self.api_key:
                return self._fallback_summary(messages)

            prompt = self._build_conversation_summary_prompt(
                messages, user_context)

            response = self._call_gemini_api(prompt)
            if response:
                return self._parse_conversation_summary(response, messages)
            else:
                return self._fallback_summary(messages)

        except Exception as e:
            logger.error(f"Error summarizing conversation: {str(e)}")
            return self._fallback_summary(messages)

    def score_emotional_state(self, text: str) -> Dict[str, float]:
        """
        Score emotional state from text

        Args:
            text: Text to analyze

        Returns:
            Dictionary with emotion scores (0-1 scale)
        """
        try:
            if not self.api_key:
                return self._fallback_emotion_scores()

            prompt = self._build_emotion_scoring_prompt(text)

            response = self._call_gemini_api(prompt)
            if response:
                return self._parse_emotion_scores(response)
            else:
                return self._fallback_emotion_scores()

        except Exception as e:
            logger.error(f"Error scoring emotional state: {str(e)}")
            return self._fallback_emotion_scores()

    def _call_gemini_api(self, prompt: str) -> Optional[str]:
        """Make API call to Gemini"""
        try:
            headers = {
                "Content-Type": "application/json"
            }

            payload = {
                "contents": [{
                    "parts": [{
                        "text": prompt
                    }]
                }],
                "generationConfig": {
                    "temperature": 0.3,
                    "topK": 40,
                    "topP": 0.95,
                    "maxOutputTokens": 1024,
                }
            }

            url = f"{self.api_url}?key={self.api_key}"

            logger.info("Sending request to Gemini API...")

            response = requests.post(
                url, headers=headers, json=payload, timeout=30)

            if response.status_code == 200:
                response_data = response.json()
                if 'candidates' in response_data and len(response_data['candidates']) > 0:
                    content = response_data['candidates'][0]['content']['parts'][0]['text']
                    logger.info(
                        "Successfully received response from Gemini API")
                    return content
                else:
                    logger.error("No candidates in Gemini response")
                    return None
            else:
                logger.error(
                    f"Gemini API error: {response.status_code} - {response.text}")
                return None

        except requests.exceptions.RequestException as e:
            logger.error(f"Network error calling Gemini API: {str(e)}")
            return None
        except Exception as e:
            logger.error(f"Unexpected error calling Gemini API: {str(e)}")
            return None

    def _build_journal_analysis_prompt(self, journal_text: str, user_context: Optional[Dict[str, Any]] = None) -> str:
        """Build prompt for journal entry analysis"""
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

        return prompt

    def _build_conversation_summary_prompt(self, messages: List[Dict[str, str]], user_context: Optional[Dict[str, Any]] = None) -> str:
        """Build prompt for conversation summarization"""
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

        return prompt

    def _build_emotion_scoring_prompt(self, text: str) -> str:
        """Build prompt for emotion scoring"""
        return f"""Score the emotional content of this text on a 0-1 scale and respond with ONLY a valid JSON object:

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

    def _parse_journal_analysis(self, response: str, original_text: str) -> Dict[str, Any]:
        """Parse journal analysis response"""
        try:
            # Try to extract JSON from response
            response_clean = response.strip()
            if response_clean.startswith('```json'):
                response_clean = response_clean[7:-3]
            elif response_clean.startswith('```'):
                response_clean = response_clean[3:-3]

            analysis = json.loads(response_clean)

            # Add metadata
            analysis['timestamp'] = datetime.now().isoformat()
            analysis['original_text_length'] = len(original_text)

            return analysis

        except json.JSONDecodeError as e:
            logger.error(
                f"Failed to parse Gemini journal analysis response: {str(e)}")
            return self._fallback_analysis(original_text)

    def _parse_conversation_summary(self, response: str, messages: List[Dict]) -> Dict[str, Any]:
        """Parse conversation summary response"""
        try:
            response_clean = response.strip()
            if response_clean.startswith('```json'):
                response_clean = response_clean[7:-3]
            elif response_clean.startswith('```'):
                response_clean = response_clean[3:-3]

            summary = json.loads(response_clean)

            # Add metadata
            summary['timestamp'] = datetime.now().isoformat()
            summary['message_count'] = len(messages)

            return summary

        except json.JSONDecodeError as e:
            logger.error(f"Failed to parse Gemini summary response: {str(e)}")
            return self._fallback_summary(messages)

    def _parse_emotion_scores(self, response: str) -> Dict[str, float]:
        """Parse emotion scoring response"""
        try:
            response_clean = response.strip()
            if response_clean.startswith('```json'):
                response_clean = response_clean[7:-3]
            elif response_clean.startswith('```'):
                response_clean = response_clean[3:-3]

            scores = json.loads(response_clean)

            # Ensure all scores are floats between 0 and 1
            for key, value in scores.items():
                if isinstance(value, (int, float)):
                    scores[key] = max(0.0, min(1.0, float(value)))

            return scores

        except json.JSONDecodeError as e:
            logger.error(f"Failed to parse Gemini emotion scores: {str(e)}")
            return self._fallback_emotion_scores()

    def _fallback_analysis(self, journal_text: str) -> Dict[str, Any]:
        """Fallback analysis when Gemini is unavailable"""
        # Simple keyword-based analysis
        text_lower = journal_text.lower()

        distress_words = ['sad', 'depressed', 'anxious', 'worried',
                          'scared', 'hopeless', 'difficult', 'hard', 'struggle']
        hope_words = ['better', 'hope', 'improve', 'positive',
                      'good', 'happy', 'grateful', 'thankful']

        distress_score = sum(
            1 for word in distress_words if word in text_lower) / len(distress_words)
        hope_score = sum(
            1 for word in hope_words if word in text_lower) / len(hope_words)

        return {
            "emotion_scores": {
                "distress": min(distress_score, 1.0),
                "hope": min(hope_score, 1.0),
                "motivation": 0.5,
                "anxiety": min(distress_score * 0.8, 1.0),
                "positivity": min(hope_score * 1.2, 1.0)
            },
            "key_themes": ["personal reflection"],
            "insights": "Journal entry reflects personal thoughts and experiences",
            "suggestions": "Continue journaling to track your emotional journey",
            "urgency_level": "low",
            "timestamp": datetime.now().isoformat(),
            "original_text_length": len(journal_text),
            "fallback": True
        }

    def _fallback_summary(self, messages: List[Dict]) -> Dict[str, Any]:
        """Fallback summary when Gemini is unavailable"""
        return {
            "summary": f"Conversation with {len(messages)} messages about support and resources",
            "user_needs": ["support", "resources"],
            "emotional_tone": "seeking assistance",
            "progress_indicators": ["reaching out for help"],
            "recommendations": ["continue conversation", "follow up on resources"],
            "follow_up_needed": True,
            "timestamp": datetime.now().isoformat(),
            "message_count": len(messages),
            "fallback": True
        }

    def _fallback_emotion_scores(self) -> Dict[str, float]:
        """Fallback emotion scores when Gemini is unavailable"""
        return {
            "distress": 0.5,
            "hope": 0.5,
            "motivation": 0.5,
            "anxiety": 0.5,
            "positivity": 0.5,
            "overall_sentiment": "neutral",
            "fallback": True
        }


# Global instance
gemini_service = GeminiService()


def analyze_journal_entry(journal_text: str, user_context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Main function to analyze journal entries"""
    return gemini_service.analyze_journal_entry(journal_text, user_context)


def summarize_conversation(messages: List[Dict[str, str]], user_context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Main function to summarize conversations"""
    return gemini_service.summarize_conversation(messages, user_context)


def score_emotional_state(text: str) -> Dict[str, float]:
    """Main function to score emotional state"""
    return gemini_service.score_emotional_state(text)
