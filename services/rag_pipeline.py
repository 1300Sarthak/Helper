# Custom RAG pipeline for nearby resources

import logging
from typing import Dict, List, Any, Optional
import json
from datetime import datetime

logger = logging.getLogger(__name__)


class RAGPipeline:
    """RAG Pipeline for retrieving local resources based on user context"""

    def __init__(self):
        # In a real implementation, this would connect to external APIs
        # For now, we'll use a comprehensive local database
        self.resource_database = self._initialize_resource_database()

    def _initialize_resource_database(self) -> Dict[str, List[Dict]]:
        """Initialize a comprehensive resource database"""
        return {
            "san_francisco": {
                "food": [
                    {
                        "name": "SF-Marin Food Bank",
                        "address": "900 Pennsylvania Ave, San Francisco, CA 94107",
                        "phone": "(415) 282-1900",
                        "hours": "Mon-Fri 9am-5pm",
                        "services": ["Food pantry", "Emergency food boxes"],
                        "requirements": "No documentation required",
                        "distance": 0.8
                    },
                    {
                        "name": "Glide Memorial Church",
                        "address": "330 Ellis Street, San Francisco, CA 94102",
                        "phone": "(415) 674-6000",
                        "hours": "Daily meals: 8am, 12pm, 4pm",
                        "services": ["Free meals", "Food pantry"],
                        "requirements": "None",
                        "distance": 1.2
                    },
                    {
                        "name": "St. Anthony's Dining Room",
                        "address": "150 Golden Gate Ave, San Francisco, CA 94102",
                        "phone": "(415) 592-2710",
                        "hours": "Mon-Fri 11:30am-12:30pm",
                        "services": ["Free lunch", "Groceries"],
                        "requirements": "None",
                        "distance": 1.0
                    }
                ],
                "shelter": [
                    {
                        "name": "MSC South Shelter",
                        "address": "525 5th Street, San Francisco, CA 94107",
                        "phone": "(415) 597-7960",
                        "hours": "24/7",
                        "services": ["Emergency shelter", "Case management"],
                        "requirements": "Walk-in services available",
                        "beds_available": 45,
                        "distance": 0.5
                    },
                    {
                        "name": "Next Door Shelter",
                        "address": "1001 Polk Street, San Francisco, CA 94109",
                        "phone": "(415) 487-3300",
                        "hours": "Intake: 4pm-1am",
                        "services": ["Overnight shelter", "Meals", "Showers"],
                        "requirements": "Check-in required",
                        "beds_available": 32,
                        "distance": 1.1
                    },
                    {
                        "name": "Hamilton Family Center",
                        "address": "260 Golden Gate Ave, San Francisco, CA 94102",
                        "phone": "(415) 292-0870",
                        "hours": "24/7",
                        "services": ["Family shelter", "Childcare", "Job training"],
                        "requirements": "Families with children",
                        "beds_available": 18,
                        "distance": 0.9
                    }
                ],
                "healthcare": [
                    {
                        "name": "HealthRIGHT 360",
                        "address": "1563 Mission Street, San Francisco, CA 94103",
                        "phone": "(415) 762-3700",
                        "hours": "Mon-Fri 8am-5pm",
                        "services": ["Primary care", "Mental health", "Substance abuse"],
                        "requirements": "Sliding scale fees",
                        "distance": 0.7
                    },
                    {
                        "name": "SF City Clinic",
                        "address": "356 7th Street, San Francisco, CA 94103",
                        "phone": "(415) 487-5500",
                        "hours": "Mon-Thu 8am-4pm, Fri 8am-12pm",
                        "services": ["STD testing", "HIV testing", "Vaccinations"],
                        "requirements": "Free services",
                        "distance": 0.6
                    }
                ],
                "employment": [
                    {
                        "name": "SF Works Career Center",
                        "address": "801 Turk Street, San Francisco, CA 94102",
                        "phone": "(415) 701-4848",
                        "hours": "Mon-Fri 9am-5pm",
                        "services": ["Job placement", "Resume help", "Skills training"],
                        "requirements": "None",
                        "distance": 1.3
                    }
                ]
            },
            "oakland": {
                "food": [
                    {
                        "name": "Alameda County Community Food Bank",
                        "address": "7900 Edgewater Dr, Oakland, CA 94621",
                        "phone": "(510) 635-3663",
                        "hours": "Mon-Fri 9am-4pm",
                        "services": ["Food pantry", "Mobile food pantry"],
                        "requirements": "No documentation required",
                        "distance": 2.1
                    }
                ],
                "shelter": [
                    {
                        "name": "Henry Robinson Multi Service Center",
                        "address": "3801 Martin Luther King Jr Way, Oakland, CA 94609",
                        "phone": "(510) 597-5085",
                        "hours": "24/7",
                        "services": ["Emergency shelter", "Transitional housing"],
                        "requirements": "Intake assessment required",
                        "beds_available": 67,
                        "distance": 1.8
                    }
                ]
            }
        }

    def retrieve_resources(self, location: str, needs: List[str], situation: str = None) -> Dict[str, Any]:
        """
        Retrieve relevant resources based on user location and needs

        Args:
            location: User's location (city, zip, etc.)
            needs: List of needs (food, shelter, healthcare, etc.)
            situation: User's current situation for context

        Returns:
            Dictionary of relevant resources with confidence scores
        """
        try:
            # Normalize location
            normalized_location = self._normalize_location(location)

            # Get resources for the location
            location_resources = self.resource_database.get(
                normalized_location, {})

            if not location_resources:
                return self._get_fallback_resources(location)

            # Filter resources based on needs
            relevant_resources = {}
            confidence_scores = {}

            for need in needs:
                need_type = self._map_need_to_category(need)
                if need_type in location_resources:
                    resources = location_resources[need_type]
                    # Sort by distance and availability
                    sorted_resources = self._rank_resources(
                        resources, situation)
                    # Top 3
                    relevant_resources[need_type] = sorted_resources[:3]
                    confidence_scores[need_type] = self._calculate_confidence(
                        sorted_resources)

            return {
                "location": location,
                "normalized_location": normalized_location,
                "resources": relevant_resources,
                "confidence_scores": confidence_scores,
                "total_resources": sum(len(r) for r in relevant_resources.values()),
                "timestamp": datetime.now().isoformat()
            }

        except Exception as e:
            logger.error(f"Error in RAG pipeline: {str(e)}")
            return self._get_fallback_resources(location)

    def _normalize_location(self, location: str) -> str:
        """Normalize location string to match database keys"""
        if not location:
            return "unknown"

        location_lower = location.lower()

        if "san francisco" in location_lower or "sf" in location_lower:
            return "san_francisco"
        elif "oakland" in location_lower:
            return "oakland"
        elif "berkeley" in location_lower:
            return "oakland"  # Use Oakland resources for Berkeley
        else:
            return "unknown"

    def _map_need_to_category(self, need: str) -> str:
        """Map user needs to resource categories"""
        need_lower = need.lower()

        if any(word in need_lower for word in ["food", "hungry", "meal", "eat"]):
            return "food"
        elif any(word in need_lower for word in ["shelter", "housing", "sleep", "bed"]):
            return "shelter"
        elif any(word in need_lower for word in ["health", "medical", "doctor", "clinic"]):
            return "healthcare"
        elif any(word in need_lower for word in ["job", "work", "employment", "career"]):
            return "employment"
        else:
            return "food"  # Default to food assistance

    def _rank_resources(self, resources: List[Dict], situation: str = None) -> List[Dict]:
        """Rank resources based on relevance and availability"""
        scored_resources = []

        for resource in resources:
            score = 0

            # Distance score (closer is better)
            distance = resource.get("distance", 5.0)
            score += max(0, 5 - distance)

            # Availability score
            if "beds_available" in resource:
                beds = resource["beds_available"]
                if beds > 20:
                    score += 3
                elif beds > 10:
                    score += 2
                elif beds > 0:
                    score += 1

            # Situational relevance
            if situation:
                if "family" in situation.lower() and "family" in resource.get("services", []):
                    score += 2
                if "emergency" in situation.lower() and "24/7" in resource.get("hours", ""):
                    score += 2

            # Requirements score (fewer requirements is better)
            requirements = resource.get("requirements", "")
            if "none" in requirements.lower() or "no documentation" in requirements.lower():
                score += 2

            scored_resources.append({**resource, "relevance_score": score})

        return sorted(scored_resources, key=lambda x: x["relevance_score"], reverse=True)

    def _calculate_confidence(self, resources: List[Dict]) -> float:
        """Calculate confidence score for resource recommendations"""
        if not resources:
            return 0.0

        # Base confidence on number of resources and their scores
        avg_score = sum(r.get("relevance_score", 0)
                        for r in resources) / len(resources)
        # Max confidence with 3+ resources
        resource_count_factor = min(len(resources) / 3.0, 1.0)

        return min(avg_score * resource_count_factor / 10.0, 1.0)

    def _get_fallback_resources(self, location: str) -> Dict[str, Any]:
        """Provide fallback resources when specific location data isn't available"""
        return {
            "location": location,
            "normalized_location": "unknown",
            "resources": {
                "general": [
                    {
                        "name": "211 Bay Area",
                        "phone": "2-1-1",
                        "services": ["Resource referrals", "Crisis support"],
                        "description": "Call 211 for local resource information in your area"
                    },
                    {
                        "name": "National Suicide Prevention Lifeline",
                        "phone": "988",
                        "services": ["Crisis support", "Mental health"],
                        "description": "24/7 crisis support and mental health resources"
                    }
                ]
            },
            "confidence_scores": {"general": 0.3},
            "total_resources": 2,
            "timestamp": datetime.now().isoformat(),
            "note": f"Specific resources for {location} not available. Showing general resources."
        }

    def format_resources_for_claude(self, rag_results: Dict[str, Any]) -> str:
        """Format RAG results for Claude context"""
        if not rag_results.get("resources"):
            return "No specific local resources found. Recommend calling 211 for local assistance."

        formatted = f"Local resources near {rag_results['location']}:\n\n"

        for category, resources in rag_results["resources"].items():
            formatted += f"{category.upper()} RESOURCES:\n"
            for resource in resources:
                formatted += f"• {resource['name']}\n"
                formatted += f"  Address: {resource.get('address', 'Call for address')}\n"
                formatted += f"  Phone: {resource.get('phone', 'N/A')}\n"
                formatted += f"  Hours: {resource.get('hours', 'Call for hours')}\n"
                if resource.get('requirements'):
                    formatted += f"  Requirements: {resource['requirements']}\n"
                formatted += "\n"

        return formatted


# Global RAG pipeline instance
rag_pipeline = RAGPipeline()


def get_local_resources(location: str, needs: List[str], situation: str = None) -> Dict[str, Any]:
    """Main function to get local resources via RAG pipeline"""
    return rag_pipeline.retrieve_resources(location, needs, situation)
