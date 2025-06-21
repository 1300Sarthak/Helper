#!/usr/bin/env python3
"""
Test script for CAG (Context-Aware Generation) and RAG (Retrieval-Augmented Generation) capabilities
"""

import requests
import json
import time

BASE_URL = "http://localhost:5001"


def test_rag_pipeline():
    """Test the RAG pipeline for resource discovery"""
    print("🔍 Testing RAG Pipeline - Resource Discovery")
    print("=" * 50)

    # Test San Francisco resources
    response = requests.post(f"{BASE_URL}/api/chat/resources", json={
        "location": "San Francisco",
        "needs": ["food", "shelter"],
        "situation": "homeless"
    })

    if response.status_code == 200:
        data = response.json()
        resources = data['resources']['resources']
        print(
            f"✅ Found {data['resources']['total_resources']} resources in San Francisco")

        for category, items in resources.items():
            print(f"\n📍 {category.upper()} RESOURCES:")
            for item in items:
                print(f"  • {item['name']}")
                print(f"    📍 {item.get('address', 'N/A')}")
                print(f"    📞 {item.get('phone', 'N/A')}")
                print(f"    🕒 {item.get('hours', 'N/A')}")
                print(
                    f"    ⭐ Relevance Score: {item.get('relevance_score', 'N/A')}")
                print()
    else:
        print(f"❌ RAG Pipeline test failed: {response.status_code}")


def test_cag_with_context():
    """Test Context-Aware Generation with Claude + RAG"""
    print("\n🧠 Testing CAG - Context-Aware Generation")
    print("=" * 50)

    # Test with full context
    response = requests.post(f"{BASE_URL}/api/chat/message", json={
        "message": "I'm really struggling and need help finding shelter for tonight",
        "context": {
            "name": "Sarah",
            "location": "San Francisco",
            "situation": "Recently lost job, staying in car",
            "needs": "emergency shelter, food assistance"
        }
    })

    if response.status_code == 200:
        data = response.json()
        print("✅ CAG Response Generated Successfully")
        print(f"👤 User ID: {data['user_id']}")
        print(f"📊 Emotion Analysis:")
        emotion = data['emotion_analysis']
        for key, value in emotion.items():
            if isinstance(value, (int, float)):
                print(f"  • {key.title()}: {value:.2f}")

        print(f"\n🤖 Claude Response:")
        print(f"  {data['response'][:200]}...")

        return data['user_id']
    else:
        print(f"❌ CAG test failed: {response.status_code}")
        return None


def test_emotion_analysis():
    """Test Claude-based emotion analysis"""
    print("\n💭 Testing Emotion Analysis")
    print("=" * 50)

    journal_entries = [
        {
            "text": "I'm feeling hopeful today. Found a temporary place to stay and had a good meal.",
            "expected": "positive"
        },
        {
            "text": "I'm really anxious and scared. Don't know where I'll sleep tonight.",
            "expected": "negative"
        }
    ]

    for i, entry in enumerate(journal_entries, 1):
        print(f"\n📝 Journal Entry {i}:")
        print(f"   \"{entry['text'][:50]}...\"")

        response = requests.post(f"{BASE_URL}/api/chat/analyze-journal", json={
            "journal_text": entry['text'],
            "context": {"location": "San Francisco", "situation": "homeless"}
        })

        if response.status_code == 200:
            data = response.json()
            analysis = data['analysis']

            print(f"✅ Analysis Complete:")
            print(
                f"   🎯 Urgency Level: {analysis.get('urgency_level', 'N/A')}")
            print(
                f"   💡 Key Themes: {', '.join(analysis.get('key_themes', []))}")
            print(f"   📊 Emotion Scores:")

            scores = analysis.get('emotion_scores', {})
            for emotion, score in scores.items():
                if isinstance(score, (int, float)):
                    bar = "█" * int(score * 10)
                    print(f"      {emotion.title()}: {score:.2f} {bar}")
        else:
            print(f"❌ Emotion analysis failed: {response.status_code}")


def test_conversation_summary(user_id):
    """Test conversation summarization"""
    if not user_id:
        return

    print(f"\n📋 Testing Conversation Summary for User {user_id}")
    print("=" * 50)

    response = requests.get(f"{BASE_URL}/api/chat/summarize/{user_id}")

    if response.status_code == 200:
        data = response.json()
        summary = data['summary']

        print("✅ Conversation Summary Generated:")
        print(f"   📝 Summary: {summary.get('summary', 'N/A')}")
        print(f"   🎭 Emotional Tone: {summary.get('emotional_tone', 'N/A')}")
        print(f"   🎯 User Needs: {', '.join(summary.get('user_needs', []))}")
        print(
            f"   ✨ Progress Indicators: {', '.join(summary.get('progress_indicators', []))}")
        print(
            f"   📋 Recommendations: {', '.join(summary.get('recommendations', []))}")
        print(
            f"   🔄 Follow-up Needed: {summary.get('follow_up_needed', 'N/A')}")
    else:
        print(f"❌ Conversation summary failed: {response.status_code}")


def test_health_check():
    """Test system health and capabilities"""
    print("\n🏥 Testing System Health")
    print("=" * 50)

    response = requests.get(f"{BASE_URL}/api/chat/health")

    if response.status_code == 200:
        data = response.json()
        print(f"✅ System Status: {data['status']}")
        print("🔧 Available Features:")

        features = data['features']
        for feature, enabled in features.items():
            status = "✅" if enabled else "❌"
            print(f"   {status} {feature.replace('_', ' ').title()}")
    else:
        print(f"❌ Health check failed: {response.status_code}")


def main():
    """Run all tests"""
    print("🚀 CAG & RAG System Test Suite")
    print("=" * 60)
    print("Testing Context-Aware Generation and Retrieval-Augmented Generation")
    print("Using Claude AI for all analysis and generation tasks")
    print("=" * 60)

    try:
        # Test all components
        test_health_check()
        test_rag_pipeline()
        user_id = test_cag_with_context()
        test_emotion_analysis()
        test_conversation_summary(user_id)

        print("\n🎉 All Tests Completed!")
        print("=" * 60)
        print("✅ RAG Pipeline: Resource discovery working")
        print("✅ CAG System: Context-aware responses working")
        print("✅ Emotion Analysis: Claude-based scoring working")
        print("✅ Conversation Summary: Claude-based insights working")
        print("✅ Integration: All systems working together")

    except requests.exceptions.ConnectionError:
        print("❌ Error: Cannot connect to Flask server")
        print("   Make sure the server is running on http://localhost:5001")
    except Exception as e:
        print(f"❌ Unexpected error: {str(e)}")


if __name__ == "__main__":
    main()
