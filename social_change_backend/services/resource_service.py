import logging
from typing import List, Dict, Any, Optional
import json

logger = logging.getLogger(__name__)


class ResourceService:
    """Service for managing local resources and services"""

    def __init__(self):
        # Mock data for MVP - in production, this would come from a database
        self._load_mock_resources()

    def _load_mock_resources(self):
        """Load mock resource data for MVP"""
        self.resources = [
            {
                "id": "1",
                "name": "Downtown Emergency Shelter",
                "type": "shelter",
                "category": "housing",
                "location": "San Francisco, CA",
                "address": "123 Main St, San Francisco, CA 94102",
                "phone": "(555) 123-4567",
                "hours": "24/7",
                "description": "Emergency shelter with beds, meals, and basic services",
                "eligibility": "Open to all",
                "services": ["emergency shelter", "meals", "showers", "case management"],
                "coordinates": {"lat": 37.7749, "lng": -122.4194}
            },
            {
                "id": "2",
                "name": "Community Food Bank",
                "type": "food",
                "category": "basic_needs",
                "location": "San Francisco, CA",
                "address": "456 Oak Ave, San Francisco, CA 94103",
                "phone": "(555) 234-5678",
                "hours": "Mon-Fri 9AM-5PM",
                "description": "Free food distribution and meal programs",
                "eligibility": "No ID required",
                "services": ["food distribution", "hot meals", "food stamps assistance"],
                "coordinates": {"lat": 37.7749, "lng": -122.4194}
            },
            {
                "id": "3",
                "name": "Health Clinic for the Homeless",
                "type": "healthcare",
                "category": "health",
                "location": "San Francisco, CA",
                "address": "789 Pine St, San Francisco, CA 94104",
                "phone": "(555) 345-6789",
                "hours": "Mon-Fri 8AM-6PM",
                "description": "Free medical care, mental health services, and substance abuse treatment",
                "eligibility": "No insurance required",
                "services": ["medical care", "mental health", "substance abuse treatment", "prescriptions"],
                "coordinates": {"lat": 37.7749, "lng": -122.4194}
            },
            {
                "id": "4",
                "name": "Job Training Center",
                "type": "employment",
                "category": "employment",
                "location": "San Francisco, CA",
                "address": "321 Market St, San Francisco, CA 94105",
                "phone": "(555) 456-7890",
                "hours": "Mon-Fri 9AM-5PM",
                "description": "Job training, resume help, and employment placement",
                "eligibility": "Open to all",
                "services": ["job training", "resume help", "job placement", "computer skills"],
                "coordinates": {"lat": 37.7749, "lng": -122.4194}
            },
            {
                "id": "5",
                "name": "Legal Aid Society",
                "type": "legal",
                "category": "legal",
                "location": "San Francisco, CA",
                "address": "654 Mission St, San Francisco, CA 94106",
                "phone": "(555) 567-8901",
                "hours": "Mon-Fri 9AM-5PM",
                "description": "Free legal assistance for housing, benefits, and civil matters",
                "eligibility": "Income-based",
                "services": ["legal advice", "housing assistance", "benefits help", "court representation"],
                "coordinates": {"lat": 37.7749, "lng": -122.4194}
            }
        ]

        # Add more locations for demo
        self._add_more_locations()

    def _add_more_locations(self):
        """Add resources for other cities"""
        other_cities = [
            {"city": "Los Angeles, CA", "lat": 34.0522, "lng": -118.2437},
            {"city": "New York, NY", "lat": 40.7128, "lng": -74.0060},
            {"city": "Chicago, IL", "lat": 41.8781, "lng": -87.6298},
            {"city": "Seattle, WA", "lat": 47.6062, "lng": -122.3321}
        ]

        for city_data in other_cities:
            city = city_data["city"]
            lat = city_data["lat"]
            lng = city_data["lng"]

            # Add shelter
            self.resources.append({
                "id": f"shelter_{city.replace(', ', '_').replace(' ', '_')}",
                "name": f"{city.split(',')[0]} Emergency Shelter",
                "type": "shelter",
                "category": "housing",
                "location": city,
                "address": f"123 Main St, {city}",
                "phone": "(555) 000-0000",
                "hours": "24/7",
                "description": "Emergency shelter with beds and basic services",
                "eligibility": "Open to all",
                "services": ["emergency shelter", "meals", "showers"],
                "coordinates": {"lat": lat, "lng": lng}
            })

            # Add food bank
            self.resources.append({
                "id": f"food_{city.replace(', ', '_').replace(' ', '_')}",
                "name": f"{city.split(',')[0]} Food Bank",
                "type": "food",
                "category": "basic_needs",
                "location": city,
                "address": f"456 Oak Ave, {city}",
                "phone": "(555) 000-0001",
                "hours": "Mon-Fri 9AM-5PM",
                "description": "Free food distribution",
                "eligibility": "No ID required",
                "services": ["food distribution", "hot meals"],
                "coordinates": {"lat": lat, "lng": lng}
            })

    def search_resources(self, location: str, needs: List[str] = None, resource_type: str = None) -> List[Dict[str, Any]]:
        """Search for resources based on location and needs"""
        try:
            filtered_resources = []

            for resource in self.resources:
                # Filter by location (simple string matching for MVP)
                if location.lower() not in resource["location"].lower():
                    continue

                # Filter by resource type
                if resource_type and resource_type.lower() != resource["type"].lower():
                    continue

                # Filter by needs
                if needs:
                    resource_services = [service.lower()
                                         for service in resource.get("services", [])]
                    if not any(need.lower() in service for service in resource_services for need in needs):
                        continue

                filtered_resources.append(resource)

            return filtered_resources

        except Exception as e:
            logger.error(f"Error searching resources: {str(e)}")
            return []

    def get_quick_actions(self, location: str = None) -> List[Dict[str, Any]]:
        """Get quick action resources for common needs"""
        quick_actions = [
            {
                "id": "crisis_hotline",
                "title": "Crisis Support",
                "description": "24/7 crisis hotlines and emergency support",
                "icon": "🆘",
                "category": "crisis",
                "resources": [
                    {
                        "name": "National Suicide Prevention Lifeline",
                        "phone": "988",
                        "description": "24/7 crisis support"
                    },
                    {
                        "name": "Crisis Text Line",
                        "phone": "Text HOME to 741741",
                        "description": "Text-based crisis support"
                    },
                    {
                        "name": "Emergency Services",
                        "phone": "911",
                        "description": "For immediate emergencies"
                    }
                ]
            },
            {
                "id": "shelter_finder",
                "title": "Find Shelter",
                "description": "Emergency shelters and housing assistance",
                "icon": "🏠",
                "category": "housing",
                "action": "search",
                "search_params": {"type": "shelter"}
            },
            {
                "id": "food_assistance",
                "title": "Food Assistance",
                "description": "Food banks, meal programs, and SNAP benefits",
                "icon": "🍽️",
                "category": "basic_needs",
                "action": "search",
                "search_params": {"type": "food"}
            },
            {
                "id": "healthcare",
                "title": "Healthcare",
                "description": "Medical care, mental health, and substance abuse treatment",
                "icon": "🏥",
                "category": "health",
                "action": "search",
                "search_params": {"type": "healthcare"}
            },
            {
                "id": "employment",
                "title": "Jobs & Training",
                "description": "Job training, employment services, and career help",
                "icon": "💼",
                "category": "employment",
                "action": "search",
                "search_params": {"type": "employment"}
            },
            {
                "id": "legal_help",
                "title": "Legal Assistance",
                "description": "Legal aid, housing rights, and benefits help",
                "icon": "⚖️",
                "category": "legal",
                "action": "search",
                "search_params": {"type": "legal"}
            }
        ]

        return quick_actions

    def get_categories(self) -> List[Dict[str, Any]]:
        """Get available resource categories"""
        categories = [
            {"id": "housing", "name": "Housing & Shelter", "icon": "🏠",
                "description": "Emergency shelter and housing assistance"},
            {"id": "basic_needs", "name": "Basic Needs", "icon": "🍽️",
                "description": "Food, clothing, and essential items"},
            {"id": "health", "name": "Healthcare", "icon": "🏥",
                "description": "Medical care, mental health, and substance abuse treatment"},
            {"id": "employment", "name": "Employment", "icon": "💼",
                "description": "Job training and employment services"},
            {"id": "legal", "name": "Legal Help", "icon": "⚖️",
                "description": "Legal assistance and advocacy"},
            {"id": "crisis", "name": "Crisis Support", "icon": "🆘",
                "description": "Emergency crisis resources and hotlines"}
        ]

        return categories

    def get_nearby_resources(self, location: str) -> List[Dict[str, Any]]:
        """Get resources near a specific location"""
        return self.search_resources(location)

    def get_crisis_resources(self, location: str = None) -> List[Dict[str, Any]]:
        """Get crisis resources and hotlines"""
        crisis_resources = [
            {
                "name": "National Suicide Prevention Lifeline",
                "phone": "988",
                "description": "24/7 crisis support for anyone in distress",
                "hours": "24/7",
                "type": "crisis"
            },
            {
                "name": "Crisis Text Line",
                "phone": "Text HOME to 741741",
                "description": "Text-based crisis support",
                "hours": "24/7",
                "type": "crisis"
            },
            {
                "name": "Emergency Services",
                "phone": "911",
                "description": "For immediate emergencies",
                "hours": "24/7",
                "type": "emergency"
            },
            {
                "name": "National Domestic Violence Hotline",
                "phone": "1-800-799-7233",
                "description": "Support for domestic violence situations",
                "hours": "24/7",
                "type": "crisis"
            },
            {
                "name": "Substance Abuse and Mental Health Services Administration",
                "phone": "1-800-662-4357",
                "description": "Treatment referral and information",
                "hours": "24/7",
                "type": "health"
            }
        ]

        # Add local crisis resources if location is provided
        if location:
            local_resources = self.search_resources(
                location, needs=["crisis", "emergency"])
            crisis_resources.extend(local_resources)

        return crisis_resources
