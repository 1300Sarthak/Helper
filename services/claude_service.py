# Claude 4 calls, prompt templates - Enhanced with CAG System Prompts

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
    """Service for interacting with Claude API with CAG System Prompts"""

    def __init__(self):
        self.api_key = os.environ.get('CLAUDE_API_KEY')
        self.api_url = "https://api.anthropic.com/v1/messages"
        self.model = "claude-3-5-sonnet-20241022"

        if not self.api_key:
            logger.warning("CLAUDE_API_KEY not set in environment variables")

    def _get_cag_system_prompts(self) -> Dict[str, str]:
        """Define the two CAG system prompts"""
        return {
            "empathetic_coach": """
You are a compassionate AI social worker and life coach assistant dedicated to helping people navigate life's challenges, especially those experiencing hardship. Your goal is to provide comprehensive, thoughtful guidance for accessing resources related to housing, food, healthcare, mental health, legal help, and social support.

Core Principles:

1. **Comprehensive Support**:
    - Provide detailed, thorough responses that address the user's needs completely
    - Don't rush through answers - take time to explain options, processes, and considerations
    - Offer multiple approaches and perspectives when relevant
    - Include both immediate solutions and long-term strategies

2. **Empathetic and Understanding**:
    - Be warm, compassionate, and genuinely caring in your responses
    - Acknowledge the difficulty of the user's situation
    - Provide emotional support alongside practical guidance
    - Use encouraging language that builds confidence and hope

3. **Detailed and Educational**:
    - Explain processes step-by-step with clear reasoning
    - Provide context about why certain approaches might work better
    - Share relevant information about rights, eligibility, and what to expect
    - Include helpful tips and insights based on common experiences

4. **Personalized Guidance**:
    - Tailor responses to the user's specific situation and location when provided
    - Consider their unique circumstances, needs, and preferences
    - Adapt your approach based on their comfort level and readiness

5. **Resource-Focused**:
    - Prioritize connecting users with tangible, accessible resources
    - Provide specific information about organizations, services, and programs
    - Include contact information, addresses, and hours when available
    - Explain what to expect when accessing different services

6. **Trauma-Informed Approach**:
    - Always assume the user may be in a vulnerable state
    - Avoid judgment, blame, or dismissive language
    - Provide information in a way that feels safe and non-threatening
    - Offer multiple options so users feel they have choices

7. **Honest and Transparent**:
    - Be truthful about what you know and don't know
    - Acknowledge limitations and uncertainties
    - Suggest ways to verify information independently
    - Never invent or hallucinate information

8. **Encouraging and Hopeful**:
    - Focus on possibilities and solutions
    - Celebrate small steps and progress
    - Remind users of their strength and resilience
    - Provide encouragement for taking action

Remember: Your responses should be thorough, compassionate, and genuinely helpful. Take the time to provide comprehensive guidance that truly supports the user's journey toward better circumstances.""",

            "direct_assistant": """
You are a knowledgeable and efficient AI assistant focused on helping people access essential services and resources. Your role is to provide clear, comprehensive guidance for navigating systems related to housing, food, healthcare, mental health, legal aid, and social support.

Key Approach:

1. **Thorough Information**:
    - Provide complete, detailed responses that cover all relevant aspects
    - Don't skimp on details - users need comprehensive information to make informed decisions
    - Include step-by-step processes with clear explanations
    - Address potential challenges and how to overcome them

2. **Clear and Direct Communication**:
    - Be straightforward and honest in your responses
    - Use clear, accessible language
    - Organize information logically and systematically
    - Provide concrete, actionable steps

3. **Comprehensive Resource Guidance**:
    - Offer multiple options and alternatives when available
    - Include specific details about services, eligibility, and processes
    - Provide contact information and practical details
    - Explain what users can expect from different services

4. **Educational Approach**:
    - Help users understand how systems work
    - Explain rights, requirements, and procedures
    - Provide context about why certain approaches exist
    - Share relevant information that helps users advocate for themselves

5. **Practical and Realistic**:
    - Focus on what's actually achievable
    - Provide realistic timelines and expectations
    - Include information about common challenges and solutions
    - Offer backup plans and alternatives

6. **Location-Aware**:
    - Tailor information to the user's location when provided
    - Include local resources and services when available
    - Consider regional differences in services and requirements
    - Provide location-specific guidance when relevant

7. **Honest and Reliable**:
    - Be truthful about limitations and uncertainties
    - Acknowledge when information might be incomplete
    - Suggest ways to verify and update information
    - Never provide false or misleading information

8. **Supportive and Encouraging**:
    - Maintain a helpful and positive tone
    - Acknowledge the effort required to navigate complex systems
    - Provide encouragement for taking action
    - Focus on solutions and possibilities

Your goal is to provide thorough, accurate, and genuinely helpful information that empowers users to access the resources they need. Take the time to give complete responses that address all aspects of their questions and concerns."""
        }

    def _is_simple_greeting(self, message: str) -> bool:
        """Check if message is a simple greeting"""
        greetings = ['hi', 'hello', 'hey', 'good morning',
                     'good afternoon', 'good evening', 'sup', 'what\'s up']
        message_clean = message.lower().strip()
        return any(greeting in message_clean for greeting in greetings) and len(message_clean.split()) <= 3

    def get_support_response(self, message: str, context: Optional[Dict[str, Any]] = None, prompt_type: str = "empathetic_coach", history: Optional[List[Any]] = None) -> str:
        """
        Generate a supportive response using Claude API with CAG enhancement

        Args:
            message: User's input message
            context: Optional context information (user situation, location, etc.)
            prompt_type: Either "empathetic_coach" or "direct_assistant"
            history: Optional list of previous Conversation objects

        Returns:
            Claude's response as a string
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
                rag_context = rag_pipeline.format_resources_for_claude(
                    rag_results)
                logger.info(
                    f"RAG retrieved {rag_results.get('total_resources', 0)} resources")

            # Build the enhanced system prompt with CAG type
            system_prompt = self._build_enhanced_system_prompt(
                context, rag_context, prompt_type)

            # Prepare the API request
            headers = {
                "Content-Type": "application/json",
                "x-api-key": self.api_key,
                "anthropic-version": "2023-06-01"
            }

            # Format message history
            messages = []
            if history:
                for conv in history:
                    messages.append({"role": "user", "content": conv.message})
                    messages.append(
                        {"role": "assistant", "content": conv.response})

            # Add the current message
            messages.append({"role": "user", "content": message})

            payload = {
                "model": self.model,
                "max_tokens": 4000,
                "system": system_prompt,
                "messages": messages
            }

            logger.info(
                f"Sending request to Claude API with prompt type: {prompt_type}")

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
                return self._fallback_response(message, prompt_type)

        except requests.exceptions.RequestException as e:
            logger.error(f"Network error calling Claude API: {str(e)}")
            return self._fallback_response(message, prompt_type)
        except Exception as e:
            logger.error(f"Unexpected error in Claude service: {str(e)}")
            return self._fallback_response(message, prompt_type)

    def _build_enhanced_system_prompt(self, context: Optional[Dict[str, Any]] = None, rag_context: str = "", prompt_type: str = "empathetic_coach") -> str:
        """Build enhanced system prompt with RAG context and CAG prompt type"""
        prompts = self._get_cag_system_prompts()
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

            if context_info:
                base_prompt += f"\n\nUser Context:{context_info}"

        # Add RAG context with local resources
        if rag_context:
            base_prompt += f"\n\nLocal Resources Available:\n{rag_context}"
            base_prompt += "\nUse these specific local resources in your response. Provide exact addresses, phone numbers, and hours when available."

        return base_prompt

    def _fallback_response(self, message: str, prompt_type: str = "empathetic_coach") -> str:
        """Fallback response when Claude API is unavailable"""
        if self._is_simple_greeting(message):
            if prompt_type == "direct_assistant":
                return "Hello. What do you need help with? (Note: I'm currently offline but will try to assist.)"
            else:
                return "Hi there! I'm here to help you, though I'm having some technical difficulties right now. How can I assist you?"

        fallback_responses = {
            "empathetic_coach": f"I understand you're reaching out for support, and I want you to know that your message is important. While I'm having trouble connecting right now, I can see you mentioned: '{message}'. Please know that help is available, and you're taking a positive step by seeking support. Is there something specific I can try to help you with?",

            "direct_assistant": f"I'm currently offline but received your request: '{message}'. Try these steps: 1) Call 2-1-1 for local resources, 2) Visit your nearest community center, 3) Check with local social services. What specific help do you need?"
        }

        return fallback_responses.get(prompt_type, fallback_responses["empathetic_coach"])

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

    # Keep all the existing methods for journal analysis, conversation summary, etc.
    def analyze_journal_entry(self, journal_text: str, user_context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Analyze a journal entry for emotion scoring and insights using Claude"""
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
        """Summarize a conversation for context and insights using Claude"""
        try:
            if not self.api_key:
                return self._fallback_summary(messages)

            conversation = "\n".join(
                [f"{msg.get('role', 'user')}: {msg.get('content', '')}" for msg in messages[-10:]])

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
        """Score emotional state from text using Claude"""
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
                parsed = self._parse_json_response(
                    response, self._fallback_emotion_scores())
                parsed['timestamp'] = datetime.now().isoformat()
                parsed['source'] = 'claude'
                return parsed
            else:
                return self._fallback_emotion_scores()

        except Exception as e:
            logger.error(f"Error scoring emotional state: {str(e)}")
            return self._fallback_emotion_scores()

    def _call_claude_api(self, prompt: str, max_tokens: int = 4000) -> Optional[str]:
        """Call Claude API with the given prompt"""
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
            response_clean = response.strip()
            if response_clean.startswith('```json'):
                response_clean = response_clean[7:-3]
            elif response_clean.startswith('```'):
                response_clean = response_clean[3:-3]

            parsed = json.loads(response_clean)
            parsed['timestamp'] = datetime.now().isoformat()
            parsed['source'] = 'claude'
            return parsed

        except json.JSONDecodeError as e:
            logger.error(f"Failed to parse Claude JSON response: {str(e)}")
            return fallback

    def _fallback_analysis(self, journal_text: str) -> Dict[str, Any]:
        """Fallback analysis when Claude is unavailable"""
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


def get_support_response(message: str, context: Optional[Dict[str, Any]] = None, prompt_type: str = "empathetic_coach", history: Optional[List[Any]] = None) -> str:
    """
    Main function to get support response from Claude with CAG prompt type
    """
    return claude_service.get_support_response(message, context, prompt_type, history)


def analyze_journal_entry(journal_text: str, user_context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Main function to analyze journal entries using Claude"""
    return claude_service.analyze_journal_entry(journal_text, user_context)


def summarize_conversation(messages: List[Dict[str, str]], user_context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Main function to summarize conversations using Claude"""
    return claude_service.summarize_conversation(messages, user_context)


def score_emotional_state(text: str) -> Dict[str, float]:
    """Main function to score emotional state using Claude"""
    return claude_service.score_emotional_state(text)
