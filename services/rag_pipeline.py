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
                    },
                    {
                        "name": "Covenant House California - Oakland",
                        "address": "1695 Depot Rd, Oakland, CA",
                        "phone": "510-829-8224",
                        "hours": null,
                        "services": [],
                        "requirements": null,
                        "beds_available": 25,
                        "distance": null
                    },
                    {
                        "name": "Henry Robinson Center",
                        "address": "1026 Mission Blvd, Oakland, CA",
                        "phone": "510-266-2724",
                        "hours": null,
                        "services": [],
                        "requirements": null,
                        "beds_available": 137,
                        "distance": null
                    },
                    {
                        "name": "The Holland",
                        "address": "2419 Castro St, Oakland, CA",
                        "phone": "510-785-9245",
                        "hours": null,
                        "services": [],
                        "requirements": null,
                        "beds_available": 90,
                        "distance": null
                    },
                    {
                        "name": "Oakland Elizabeth House",
                        "address": "3371 Depot Rd, Oakland, CA",
                        "phone": "510-863-8125",
                        "hours": null,
                        "services": [],
                        "requirements": null,
                        "beds_available": 26,
                        "distance": null
                    },
                    {
                        "name": "East Oakland Community Project",
                        "address": "9941 University Ave, Oakland, CA",
                        "phone": "510-990-4919",
                        "hours": null,
                        "services": [],
                        "requirements": null,
                        "beds_available": 18,
                        "distance": null
                    },
                    {
                        "name": "St. Mary's Center - Closer to Home",
                        "address": "4835 Broadway, Oakland, CA",
                        "phone": "510-478-1593",
                        "hours": null,
                        "services": [],
                        "requirements": null,
                        "beds_available": 8,
                        "distance": null
                    },
                    {
                        "name": "St. Mary's Center - Presentation House",
                        "address": "8931 Ashby Ave, Oakland, CA",
                        "phone": "510-465-5451",
                        "hours": null,
                        "services": [],
                        "requirements": null,
                        "beds_available": 8,
                        "distance": null
                    },
                    {
                        "name": "St. Mary's Center - Friendly Manor",
                        "address": "362 Shattuck Ave, Oakland, CA",
                        "phone": "510-546-1983",
                        "hours": null,
                        "services": [],
                        "requirements": null,
                        "beds_available": 8,
                        "distance": null
                    },
                    {
                        "name": "Salvation Army Oakland Garden Center",
                        "address": "5801 Depot Rd, Oakland, CA",
                        "phone": "510-842-5596",
                        "hours": null,
                        "services": [],
                        "requirements": null,
                        "beds_available": 45,
                        "distance": null
                    },
                    {
                        "name": "Operation Dignity Veterans Housing",
                        "address": "1267 Castro St, Oakland, CA",
                        "phone": "510-516-8732",
                        "hours": null,
                        "services": [],
                        "requirements": null,
                        "beds_available": 32,
                        "distance": null
                    },
                    {
                        "name": "BOSS Oakland Emergency Shelter",
                        "address": "4715 Telegraph Ave, Oakland, CA",
                        "phone": "510-910-3574",
                        "hours": null,
                        "services": [],
                        "requirements": null,
                        "beds_available": 28,
                        "distance": null
                    },
                    {
                        "name": "Matilda Cleveland Transitional Housing",
                        "address": "216 Mission Blvd, Oakland, CA",
                        "phone": "510-560-3421",
                        "hours": null,
                        "services": [],
                        "requirements": null,
                        "beds_available": 35,
                        "distance": null
                    },
                    {
                        "name": "Building Futures Women's Center",
                        "address": "7354 International Blvd, Oakland, CA",
                        "phone": "510-859-4263",
                        "hours": null,
                        "services": [],
                        "requirements": null,
                        "beds_available": 22,
                        "distance": null
                    },
                    {
                        "name": "Family Front Door",
                        "address": "6488 Ashby Ave, Oakland, CA",
                        "phone": "510-944-2006",
                        "hours": null,
                        "services": [],
                        "requirements": null,
                        "beds_available": 15,
                        "distance": null
                    },
                    {
                        "name": "Oakland Winter Relief Center",
                        "address": "3607 Shattuck Ave, Oakland, CA",
                        "phone": "510-393-1870",
                        "hours": null,
                        "services": [],
                        "requirements": null,
                        "beds_available": 50,
                        "distance": null
                    },
                    {
                        "name": "Centro Legal de la Raza Housing",
                        "address": "5956 Castro St, Oakland, CA",
                        "phone": "510-468-8245",
                        "hours": null,
                        "services": [],
                        "requirements": null,
                        "beds_available": 12,
                        "distance": null
                    },
                    {
                        "name": "Davis Street Family Resource Center",
                        "address": "8236 Mission Blvd, Oakland, CA",
                        "phone": "510-951-2562",
                        "hours": null,
                        "services": [],
                        "requirements": null,
                        "beds_available": 18,
                        "distance": null
                    },
                    {
                        "name": "Women's Daytime Drop-in Oakland",
                        "address": "9821 Thornton Ave, Oakland, CA",
                        "phone": "510-623-9396",
                        "hours": null,
                        "services": [],
                        "requirements": null,
                        "beds_available": 20,
                        "distance": null
                    },
                    {
                        "name": "Crossroads Emergency Housing",
                        "address": "7411 University Ave, Oakland, CA",
                        "phone": "510-872-9069",
                        "hours": null,
                        "services": [],
                        "requirements": null,
                        "beds_available": 125,
                        "distance": null
                    },
                    {
                        "name": "Alameda Family Services Shelter",
                        "address": "6136 Telegraph Ave, Oakland, CA",
                        "phone": "510-554-6176",
                        "hours": null,
                        "services": [],
                        "requirements": null,
                        "beds_available": 16,
                        "distance": null
                    },
                    {
                        "name": "Bay Area Rescue Mission Oakland",
                        "address": "9731 Center St, Oakland, CA",
                        "phone": "510-751-8445",
                        "hours": null,
                        "services": [],
                        "requirements": null,
                        "beds_available": 60,
                        "distance": null
                    },
                    {
                        "name": "Safe Haven Transitional Housing",
                        "address": "478 International Blvd, Oakland, CA",
                        "phone": "510-843-4933",
                        "hours": null,
                        "services": [],
                        "requirements": null,
                        "beds_available": 24,
                        "distance": null
                    },
                    {
                        "name": "Unity Council Emergency Housing",
                        "address": "6207 University Ave, Oakland, CA",
                        "phone": "510-402-7664",
                        "hours": null,
                        "services": [],
                        "requirements": null,
                        "beds_available": 14,
                        "distance": null
                    },
                    {
                        "name": "Aurora Housing Program",
                        "address": "8293 Depot Rd, Oakland, CA",
                        "phone": "510-908-9834",
                        "hours": null,
                        "services": [],
                        "requirements": null,
                        "beds_available": 30,
                        "distance": null
                    },
                    {
                        "name": "Oakland Interfaith Housing",
                        "address": "170 International Blvd, Oakland, CA",
                        "phone": "510-696-7083",
                        "hours": null,
                        "services": [],
                        "requirements": null,
                        "beds_available": 22,
                        "distance": null
                    },
                    {
                        "name": "Emergency Food & Shelter Oakland",
                        "address": "2788 Center St, Oakland, CA",
                        "phone": "510-612-3823",
                        "hours": null,
                        "services": [],
                        "requirements": null,
                        "beds_available": 40,
                        "distance": null
                    },
                    {
                        "name": "New Hope Housing Services",
                        "address": "6799 Telegraph Ave, Oakland, CA",
                        "phone": "510-959-8409",
                        "hours": null,
                        "services": [],
                        "requirements": null,
                        "beds_available": 18,
                        "distance": null
                    },
                    {
                        "name": "Community Housing Partnership",
                        "address": "485 San Pablo Ave, Oakland, CA",
                        "phone": "510-633-1274",
                        "hours": null,
                        "services": [],
                        "requirements": null,
                        "beds_available": 35,
                        "distance": null
                    },
                    {
                        "name": "Friendship Bench Emergency Shelter",
                        "address": "2088 San Pablo Ave, Oakland, CA",
                        "phone": "510-825-5347",
                        "hours": null,
                        "services": [],
                        "requirements": null,
                        "beds_available": 25,
                        "distance": null
                    },
                    {
                        "name": "PATH Oakland Emergency Housing",
                        "address": "2062 San Pablo Ave, Oakland, CA",
                        "phone": "510-816-7250",
                        "hours": null,
                        "services": [],
                        "requirements": null,
                        "beds_available": 20,
                        "distance": null
                    },
                    {
                        "name": "Transitional Age Youth Program",
                        "address": "4108 International Blvd, Oakland, CA",
                        "phone": "510-386-5898",
                        "hours": null,
                        "services": [],
                        "requirements": null,
                        "beds_available": 16,
                        "distance": null
                    },
                    {
                        "name": "OCCUR Emergency Shelter",
                        "address": "7090 Ashby Ave, Oakland, CA",
                        "phone": "510-244-8082",
                        "hours": null,
                        "services": [],
                        "requirements": null,
                        "beds_available": 28,
                        "distance": null
                    }
                ],
                "healthcare": [
                    {
                        "name": "Louisa Abada",
                        "address": "1727 Martin Luther King Jr Way, Oakland, CA 94612-1327",
                        "phone": "510-893-9230",
                        "services": [
                            "Mental health assessment",
                            "Social services coordination"
                        ],
                        "requirements": "17 years experience",
                        "distance": null
                    },
                    {
                        "name": "Zena Abdallah",
                        "address": "8601 MacArthur Blvd, Oakland, CA 94605-4037",
                        "phone": "510-844-5369",
                        "services": [
                            "Trauma therapy"
                        ],
                        "requirements": "4 years experience",
                        "distance": null
                    },
                    {
                        "name": "Rachel Adams",
                        "address": "2633 E 27th St, Oakland, CA 94601-1912",
                        "phone": "510-536-8111",
                        "services": [
                            "Substance abuse counseling",
                            "Trauma therapy"
                        ],
                        "requirements": "5 years experience",
                        "distance": null
                    },
                    {
                        "name": "Neal Adams",
                        "address": "5751 Adeline St, Oakland, CA 94608-2815",
                        "phone": "510-467-4250",
                        "services": [
                            "Grief counseling"
                        ],
                        "requirements": "12 years experience",
                        "distance": null
                    },
                    {
                        "name": "Bruce Adams",
                        "address": "1005 Atlantic Ave, Alameda, CA 94501-1148",
                        "phone": "415-474-7310",
                        "services": [
                            "Trauma therapy"
                        ],
                        "requirements": "6 years experience",
                        "distance": null
                    },
                    {
                        "name": "Katherine Adamson",
                        "address": "15200 Foothill Blvd, San Leandro, CA 94578-1013",
                        "phone": "510-352-9690",
                        "services": [
                            "LGBTQ+ affirming therapy"
                        ],
                        "requirements": "14 years experience",
                        "distance": null
                    },
                    {
                        "name": "Shaina Adelstein",
                        "address": "5555 Ascot Dr, Oakland, CA 94611-3001",
                        "phone": "510-879-2110",
                        "services": [
                            "ADHD therapy"
                        ],
                        "requirements": "2 years experience",
                        "distance": null
                    },
                    {
                        "name": "Omar Bocobo",
                        "address": "2579 San Pablo Ave, Oakland, CA 94612",
                        "phone": "510-844-7896",
                        "services": [
                            "Domestic violence counseling",
                            "Trauma therapy"
                        ],
                        "requirements": "22 years experience",
                        "distance": null
                    },
                    {
                        "name": "Catherine Ho",
                        "address": "268 Grand Ave, Oakland, CA 94610",
                        "phone": "510-555-7382",
                        "services": [
                            "Bilingual services"
                        ],
                        "requirements": "5 years experience",
                        "distance": null
                    },
                    {
                        "name": "Amina Samake",
                        "address": "270 Grand Ave, Oakland, CA 94610",
                        "phone": "510-926-4751",
                        "services": [
                            "Child and adolescent therapy",
                            "Multicultural counseling",
                            "Mental health assessment"
                        ],
                        "requirements": "14 years experience",
                        "distance": null
                    },
                    {
                        "name": "Emily Pellegrino",
                        "address": "2501 Harrison St, Oakland, CA 94612",
                        "phone": "510-892-3456",
                        "services": [
                            "Case management",
                            "Trauma therapy"
                        ],
                        "requirements": "11 years experience",
                        "distance": null
                    },
                    {
                        "name": "Pamela Lozoff",
                        "address": "2501 Harrison St, Oakland, CA 94612",
                        "phone": "510-789-2341",
                        "services": [
                            "Art therapy",
                            "Mental health assessment"
                        ],
                        "requirements": "6 years experience",
                        "distance": null
                    },
                    {
                        "name": "Elizabeth Cary",
                        "address": "298 Grand Ave Ste 100, Oakland, CA 94610",
                        "phone": "510-567-8901",
                        "services": [
                            "CBT (Cognitive Behavioral Therapy)",
                            "LGBTQ+ affirming therapy",
                            "Group therapy"
                        ],
                        "requirements": "16 years experience",
                        "distance": null
                    },
                    {
                        "name": "Tara Montgomery",
                        "address": "1011 Union St, Oakland, CA 94607",
                        "phone": "510-234-5678",
                        "services": [
                            "CBT (Cognitive Behavioral Therapy)",
                            "Family therapy",
                            "Play therapy"
                        ],
                        "requirements": "22 years experience",
                        "distance": null
                    },
                    {
                        "name": "Marisol Enos",
                        "address": "1011 Union St, Oakland, CA 94607",
                        "phone": "510-876-5432",
                        "services": [
                            "EMDR therapy",
                            "Art therapy",
                            "Trauma therapy"
                        ],
                        "requirements": "18 years experience",
                        "distance": null
                    },
                    {
                        "name": "Stacy Daniels",
                        "address": "1011 Union St, Oakland, CA 94607",
                        "phone": "510-345-6789",
                        "services": [
                            "ADHD therapy",
                            "Crisis intervention",
                            "Individual therapy"
                        ],
                        "requirements": "19 years experience",
                        "distance": null
                    },
                    {
                        "name": "Yolanda Olloway-Smith",
                        "address": "1011 Union St, Oakland, CA 94607",
                        "phone": "510-987-6543",
                        "services": [
                            "Couples therapy",
                            "ADHD therapy"
                        ],
                        "requirements": "5 years experience",
                        "distance": null
                    },
                    {
                        "name": "Astraea Bella",
                        "address": "3600 Broadway, Oakland, CA 94611",
                        "phone": "510-555-0142",
                        "services": [
                            "Individual therapy"
                        ],
                        "requirements": "4 years experience",
                        "distance": null
                    },
                    {
                        "name": "Brie Robertori",
                        "address": "1926 E 19th St, Oakland, CA 94606",
                        "phone": "510-555-0143",
                        "services": [
                            "Substance abuse counseling"
                        ],
                        "requirements": "13 years experience",
                        "distance": null
                    },
                    {
                        "name": "Cameron Murphey",
                        "address": "5750 College Ave, Oakland, CA 94618",
                        "phone": "510-555-0144",
                        "services": [
                            "Group therapy"
                        ],
                        "requirements": "8 years experience",
                        "distance": null
                    },
                    {
                        "name": "Jennifer Martinez",
                        "address": "4314 Piedmont Ave, Oakland, CA 94611",
                        "phone": "510-652-8901",
                        "services": [
                            "Group therapy",
                            "DBT (Dialectical Behavior Therapy)"
                        ],
                        "requirements": "15 years experience",
                        "distance": null
                    },
                    {
                        "name": "Robert Kim",
                        "address": "2579 San Pablo Ave, Oakland, CA 94612",
                        "phone": "510-789-2345",
                        "services": [
                            "Domestic violence counseling",
                            "EMDR therapy"
                        ],
                        "requirements": "4 years experience",
                        "distance": null
                    },
                    {
                        "name": "Maria Rodriguez",
                        "address": "1515 Fruitvale Ave, Oakland, CA 94601",
                        "phone": "510-345-6789",
                        "services": [
                            "EMDR therapy",
                            "Behavioral therapy"
                        ],
                        "requirements": "16 years experience",
                        "distance": null
                    },
                    {
                        "name": "David Thompson",
                        "address": "3001 International Blvd, Oakland, CA 94601",
                        "phone": "510-567-8901",
                        "services": [
                            "Multicultural counseling"
                        ],
                        "requirements": "8 years experience",
                        "distance": null
                    },
                    {
                        "name": "Lisa Chen",
                        "address": "747 52nd Street, Oakland, CA 94609",
                        "phone": "510-234-5678",
                        "services": [
                            "EMDR therapy"
                        ],
                        "requirements": "19 years experience",
                        "distance": null
                    },
                    {
                        "name": "James Wilson",
                        "address": "1266 14th St, Oakland, CA 94607",
                        "phone": "510-345-6789",
                        "services": [
                            "Crisis intervention"
                        ],
                        "requirements": "9 years experience",
                        "distance": null
                    },
                    {
                        "name": "Amy Johnson",
                        "address": "8521 A St, Oakland, CA 94621",
                        "phone": "510-456-7890",
                        "services": [
                            "Domestic violence counseling"
                        ],
                        "requirements": "16 years experience",
                        "distance": null
                    },
                    {
                        "name": "Carlos Morales",
                        "address": "3750 Brown Ave, Oakland, CA 94619",
                        "phone": "510-567-8901",
                        "services": [
                            "Group therapy",
                            "Mental health assessment",
                            "Art therapy"
                        ],
                        "requirements": "19 years experience",
                        "distance": null
                    },
                    {
                        "name": "Diana Lee",
                        "address": "2607 Myrtle St, Oakland, CA 94607",
                        "phone": "510-678-9012",
                        "services": [
                            "Social services coordination",
                            "Domestic violence counseling"
                        ],
                        "requirements": "2 years experience",
                        "distance": null
                    },
                    {
                        "name": "Kevin Brown",
                        "address": "8755 Fontaine St, Oakland, CA 94605",
                        "phone": "510-789-0123",
                        "services": [
                            "EMDR therapy",
                            "Multicultural counseling"
                        ],
                        "requirements": "25 years experience",
                        "distance": null
                    },
                    {
                        "name": "Angela Davis",
                        "address": "1023 MacArthur Blvd, Oakland, CA 94610",
                        "phone": "510-890-1234",
                        "services": [
                            "Depression and anxiety"
                        ],
                        "requirements": "17 years experience",
                        "distance": null
                    },
                    {
                        "name": "Michelle Garcia",
                        "address": "12250 Skyline Blvd, Oakland, CA 94619",
                        "phone": "510-901-2345",
                        "services": [
                            "Domestic violence counseling",
                            "Individual therapy"
                        ],
                        "requirements": "7 years experience",
                        "distance": null
                    }
                ]
            },
            "berkeley": {
                "healthcare": [
                    {
                        "name": "Patrick Conlin",
                        "address": "2901 Hillegass Ave # 2, Berkeley, CA 94705-2211",
                        "phone": "510-841-7321",
                        "services": [
                            "LGBTQ+ affirming therapy",
                            "Crisis intervention"
                        ],
                        "requirements": "16 years experience",
                        "distance": null
                    },
                    {
                        "name": "Katrina Rose Serrano",
                        "address": "2105 Martin Luther King Jr Way, Berkeley, CA 94704-1108",
                        "phone": "510-926-6677",
                        "services": [
                            "Family therapy"
                        ],
                        "requirements": "11 years experience",
                        "distance": null
                    },
                    {
                        "name": "Judith Ann Izzo",
                        "address": "2640 Martin Luther King Jr Way, Berkeley, CA 94704-3238",
                        "phone": "510-981-5290",
                        "services": [
                            "Child and adolescent therapy",
                            "Individual therapy",
                            "DBT (Dialectical Behavior Therapy)"
                        ],
                        "requirements": "19 years experience",
                        "distance": null
                    },
                    {
                        "name": "Julianna Dickey",
                        "address": "2107 Spaulding Ave, Berkeley, CA 94703-1420",
                        "phone": "510-845-5197",
                        "services": [
                            "Trauma therapy"
                        ],
                        "requirements": "4 years experience",
                        "distance": null
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

    def format_resources_for_gemini(self, rag_results: Dict[str, Any]) -> str:
        """Format RAG results for Gemini context (same format as Claude)"""
        return self.format_resources_for_claude(rag_results)


# Global RAG pipeline instance
rag_pipeline = RAGPipeline()


def get_local_resources(location: str, needs: List[str], situation: str = None) -> Dict[str, Any]:
    """Main function to get local resources via RAG pipeline"""
    return rag_pipeline.retrieve_resources(location, needs, situation)
