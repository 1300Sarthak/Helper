# Gemini Service - Complete AI assistant functionality

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


class GeminiService:
    """Service for interacting with Google Gemini API for complete AI assistant functionality"""

    def __init__(self):
        self.api_key = os.environ.get('GEMINI_API_KEY')
        self.api_url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent"

        if not self.api_key:
            logger.warning("GEMINI_API_KEY not set in environment variables")

    def _get_system_prompts(self, mode: str = "coach") -> Dict[str, str]:
        """Define system prompts for different modes and interaction styles"""
        if mode == "coach":
            return {
                "empathetic_coach": """
You are a compassionate life coach helping people navigate difficult situations. Your focus is on empowerment, motivation, and practical life guidance.

Key approach:

1. **Life Coaching Focus**:
    - Help people break down overwhelming situations into manageable steps
    - Provide motivational support and perspective-shifting advice
    - Share relatable examples and simple strategies they can use today
    - Focus on what they can control and improve right now

2. **Empowering Tone**:
    - Be warm, encouraging, and confidence-building
    - Use language that helps them see their situation more clearly
    - Example: "I hear that you're feeling overwhelmed by your housing situation. Many people have been where you are, and here's what often helps..."

3. **Practical Wisdom Over Resources**:
    - Minimize heavy resource lists - focus on mindset and actionable steps
    - Give specific life advice with examples they can relate to
    - Help them think differently about their challenges
    - Suggest simple daily actions that build momentum

4. **Simplification**:
    - Break complex problems into simple, achievable parts
    - Help them see what's most important to focus on first
    - Provide clear, specific examples of what to do today

5. **Motivational Examples**:
    - Share how others have handled similar situations
    - Give concrete examples: "One approach that works well is..."
    - Focus on building their problem-solving confidence

6. **Simple Greetings**: For simple greetings, respond warmly and ask how you can support them today.""",

                "direct_assistant": """
You are a supportive life coach providing clear, actionable guidance for life improvement.

Focus on:
1. Breaking down their situation into simple, manageable parts
2. Providing specific life strategies with examples
3. Building their confidence and motivation
4. Giving them one clear next step to take today
5. Keeping advice practical and achievable

Be direct but encouraging, focusing on empowerment and what they can control."""
            }
        else:  # assistant mode
            return {
                "empathetic_coach": """
You are a resource-focused social support assistant. Your goal is to quickly connect people with specific local resources and services.

Key approach:

1. **Resource-First Response**:
    - Quickly identify what specific help they need (shelter, food, healthcare, etc.)
    - Provide detailed information about available local resources
    - Include practical details: addresses, phone numbers, hours, requirements
    - Give multiple options when available

2. **Practical Connection**:
    - Be warm but efficient in connecting them with help
    - Explain exactly how to access services (what to bring, how to apply)
    - Include both immediate and longer-term resource options
    - End with clear next steps they can take right away

3. **Comprehensive Information**:
    - Always include actionable resource information with contact details
    - Mention what services each organization provides
    - Explain any requirements or documentation needed
    - Provide backup options when possible

4. **Immediate Action Focus**:
    - Validate briefly, then focus on solutions
    - Give them specific places to go and people to call today
    - Include emergency contacts when relevant
    - Prioritize urgent needs (shelter, food, safety) first

5. **Contact Information Priority**:
    - Always include phone numbers, addresses, and hours when available
    - Mention the best times to call or visit
    - Explain what to expect when they contact each resource

6. **Simple Greetings**: For simple greetings, respond briefly and ask what specific help they need.""",

                "direct_assistant": """
You are a resource assistant providing immediate, practical help connections.

Focus on:
1. Identifying their specific needs quickly
2. Providing detailed local resource information with contact details
3. Including all access instructions (what to bring, how to apply)
4. Giving multiple options when available
5. Being efficient and action-oriented with clear next steps

Provide comprehensive resource information with specific contact details and clear instructions."""
            }

    def _is_simple_greeting(self, message: str) -> bool:
        """Check if message is a simple greeting"""
        greetings = ['hi', 'hello', 'hey', 'good morning',
                     'good afternoon', 'good evening', 'sup', 'what\'s up']
        message_clean = message.lower().strip()
        return any(greeting in message_clean for greeting in greetings) and len(message_clean.split()) <= 3

    def get_support_response(self, message: str, context: Optional[Dict[str, Any]] = None, prompt_type: str = "empathetic_coach", mode: str = "coach") -> str:
        """
        Generate a supportive response using Gemini API

        Args:
            message: User's input message
            context: Optional context information (user situation, location, etc.)
            prompt_type: Either "empathetic_coach" or "direct_assistant"

        Returns:
            Gemini's response as a string
        """
        try:
            if not self.api_key:
                return self._fallback_response(message, prompt_type)

            # Handle simple greetings naturally
            if self._is_simple_greeting(message):
                if prompt_type == "direct_assistant":
                    return "Hello. What do you need help with?"
                else:
                    return "Hi there! I'm here to help you navigate resources and support. What can I assist you with today?"

            # Get local resources via RAG pipeline
            rag_context = ""
            if context and context.get('location'):
                needs = self._extract_needs_from_message(message, context)
                rag_results = rag_pipeline.retrieve_resources(
                    context.get('location'),
                    needs,
                    context.get('situation')
                )
                rag_context = rag_pipeline.format_resources_for_gemini(
                    rag_results)
                logger.info(
                    f"RAG retrieved {rag_results.get('total_resources', 0)} resources")

            # Build the enhanced system prompt
            system_prompt = self._build_enhanced_system_prompt(
                context, rag_context, prompt_type, mode)

            # Create the full prompt
            full_prompt = f"{system_prompt}\n\nUser message: {message}"

            response = self._call_gemini_api(full_prompt, max_tokens=1200)
            if response:
                logger.info("Successfully received response from Gemini API")
                return response
            else:
                return self._fallback_response(message, prompt_type)

        except Exception as e:
            logger.error(f"Unexpected error in Gemini service: {str(e)}")
            return self._fallback_response(message, prompt_type)

    def _build_enhanced_system_prompt(self, context: Optional[Dict[str, Any]] = None, rag_context: str = "", prompt_type: str = "empathetic_coach", mode: str = "coach") -> str:
        """Build enhanced system prompt with RAG context, prompt type, and mode"""
        prompts = self._get_system_prompts(mode)
        base_prompt = prompts.get(prompt_type, prompts["empathetic_coach"])

        # Add user context
        if context:
            context_info = ""
            if context.get('location'):
                context_info += f"\nUser location: {context['location']}"
            if context.get('situation'):
                context_info += f"\nUser situation: {context['situation']}"
            if context.get('needs'):
                context_info += f"\nUser needs: {context['needs']}"
            if context.get('name'):
                context_info += f"\nUser name: {context['name']}"

            if context_info:
                base_prompt += f"\n\nCURRENT USER CONTEXT:{context_info}"

        # Add RAG context if available
        if rag_context:
            base_prompt += f"\n\nAVAILABLE LOCAL RESOURCES:\n{rag_context}"

        return base_prompt

    def _fallback_response(self, message: str, prompt_type: str = "empathetic_coach") -> str:
        """Fallback response when Gemini is unavailable"""
        if prompt_type == "direct_assistant":
            return "I'm currently unable to access my full capabilities. Please try again later or contact local support services directly."
        else:
            return "I understand you're reaching out for support. While I'm having technical difficulties right now, please don't hesitate to contact local community resources or crisis lines if you need immediate assistance."

    def _extract_needs_from_message(self, message: str, context: Optional[Dict[str, Any]] = None) -> List[str]:
        """Extract needs/categories from user message"""
        message_lower = message.lower()
        needs = []

        # Basic keyword matching
        if any(word in message_lower for word in ['food', 'hungry', 'eat', 'meal', 'grocery']):
            needs.append('food')
        if any(word in message_lower for word in ['housing', 'shelter', 'homeless', 'place to stay', 'rent']):
            needs.append('housing')
        if any(word in message_lower for word in ['health', 'medical', 'doctor', 'clinic', 'sick']):
            needs.append('health')
        if any(word in message_lower for word in ['job', 'work', 'employment', 'income']):
            needs.append('employment')
        if any(word in message_lower for word in ['mental', 'therapy', 'counseling', 'depression', 'anxiety']):
            needs.append('mental_health')
        if any(word in message_lower for word in ['legal', 'lawyer', 'immigration', 'eviction']):
            needs.append('legal')

        # Default to general if no specific needs detected
        if not needs:
            needs = ['general']

        # Add context-based needs
        if context and context.get('needs'):
            context_needs = context['needs'].lower()
            if 'food' in context_needs and 'food' not in needs:
                needs.append('food')
            if 'housing' in context_needs and 'housing' not in needs:
                needs.append('housing')

        return needs

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

    def _call_gemini_api(self, prompt: str, max_tokens: int = 1024) -> Optional[str]:
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
                    "maxOutputTokens": max_tokens,
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


def get_support_response(message: str, context: Optional[Dict[str, Any]] = None, prompt_type: str = "empathetic_coach", mode: str = "coach") -> str:
    """Main function to get support responses"""
    return gemini_service.get_support_response(message, context, prompt_type, mode)


def analyze_journal_entry(journal_text: str, user_context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Main function to analyze journal entries"""
    return gemini_service.analyze_journal_entry(journal_text, user_context)


def summarize_conversation(messages: List[Dict[str, str]], user_context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Main function to summarize conversations"""
    return gemini_service.summarize_conversation(messages, user_context)


def score_emotional_state(text: str) -> Dict[str, float]:
    """Main function to score emotional state"""
    return gemini_service.score_emotional_state(text)
