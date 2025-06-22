#!/usr/bin/env python3
"""
Test script for /api/chat/message endpoint (Task 5)
"""

import requests
import json
import time

BASE_URL = "http://localhost:5001"


def test_chat_message_endpoint():
    """Test the /api/chat/message POST endpoint"""
    print("🧪 Testing /api/chat/message Endpoint (Task 5)")
    print("=" * 60)

    # Test 1: Basic message without user context
    print("📝 Test 1: Basic message without user context...")
    try:
        payload = {
            "message": "I need help finding food today"
        }

        response = requests.post(
            f"{BASE_URL}/api/chat/message",
            json=payload,
            headers={"Content-Type": "application/json"}
        )

        if response.status_code == 200:
            data = response.json()
            print(f"✅ Basic message test passed")
            print(f"   Response: {data['response'][:100]}...")
            print(f"   User ID: {data['user_id']}")
            print(f"   Conversation ID: {data['conversation_id']}")

            # Save user_id for next test
            user_id = data['user_id']
        else:
            print(f"❌ Basic message test failed: {response.status_code}")
            print(f"   Error: {response.text}")
            return False

    except Exception as e:
        print(f"❌ Basic message test error: {str(e)}")
        return False

    # Test 2: Message with user context
    print("\n📝 Test 2: Message with user context...")
    try:
        payload = {
            "message": "Can you help me find a shelter for tonight?",
            "context": {
                "name": "Test User",
                "location": "San Francisco, CA",
                "situation": "Experiencing homelessness",
                "needs": "Shelter, food assistance"
            }
        }

        response = requests.post(
            f"{BASE_URL}/api/chat/message",
            json=payload,
            headers={"Content-Type": "application/json"}
        )

        if response.status_code == 200:
            data = response.json()
            print(f"✅ Context message test passed")
            print(f"   Response: {data['response'][:100]}...")
            print(f"   Context: {data['context']}")

            # Save user_id for history test
            context_user_id = data['user_id']
        else:
            print(f"❌ Context message test failed: {response.status_code}")
            print(f"   Error: {response.text}")
            return False

    except Exception as e:
        print(f"❌ Context message test error: {str(e)}")
        return False

    # Test 3: Message with existing user_id
    print("\n📝 Test 3: Message with existing user_id...")
    try:
        payload = {
            "message": "Thank you for the help earlier. Do you have any other suggestions?",
            "user_id": user_id
        }

        response = requests.post(
            f"{BASE_URL}/api/chat/message",
            json=payload,
            headers={"Content-Type": "application/json"}
        )

        if response.status_code == 200:
            data = response.json()
            print(f"✅ Existing user test passed")
            print(f"   Response: {data['response'][:100]}...")
            print(f"   Same User ID: {data['user_id'] == user_id}")
        else:
            print(f"❌ Existing user test failed: {response.status_code}")
            return False

    except Exception as e:
        print(f"❌ Existing user test error: {str(e)}")
        return False

    # Test 4: Get chat history
    print("\n📝 Test 4: Getting chat history...")
    try:
        response = requests.get(
            f"{BASE_URL}/api/chat/history/{context_user_id}")

        if response.status_code == 200:
            data = response.json()
            print(f"✅ Chat history test passed")
            print(f"   User: {data['user']['name']}")
            print(f"   Total conversations: {data['total_conversations']}")
        else:
            print(f"❌ Chat history test failed: {response.status_code}")
            return False

    except Exception as e:
        print(f"❌ Chat history test error: {str(e)}")
        return False

    # Test 5: Get all users
    print("\n📝 Test 5: Getting all users...")
    try:
        response = requests.get(f"{BASE_URL}/api/chat/users")

        if response.status_code == 200:
            data = response.json()
            print(f"✅ Users list test passed")
            print(f"   Total users: {data['total_users']}")
        else:
            print(f"❌ Users list test failed: {response.status_code}")
            return False

    except Exception as e:
        print(f"❌ Users list test error: {str(e)}")
        return False

    return True


def test_error_cases():
    """Test error cases"""
    print("\n🧪 Testing Error Cases...")

    # Test missing message
    print("📝 Testing missing message...")
    try:
        payload = {}
        response = requests.post(
            f"{BASE_URL}/api/chat/message",
            json=payload,
            headers={"Content-Type": "application/json"}
        )

        if response.status_code == 400:
            print("✅ Missing message error handling works")
        else:
            print(f"❌ Expected 400, got {response.status_code}")

    except Exception as e:
        print(f"❌ Error test failed: {str(e)}")


def main():
    """Run all tests"""
    print("🧪 Testing Chat Message Endpoint")
    print("=" * 60)
    print("⚠️  Make sure the Flask app is running on port 5001!")
    print("   Run: python app.py")
    print("=" * 60)

    # Test basic connectivity
    try:
        response = requests.get(f"{BASE_URL}/ping")
        if response.status_code != 200:
            print("❌ Flask app is not running or not accessible")
            print("   Please start the app with: python app.py")
            return
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to Flask app")
        print("   Please start the app with: python app.py")
        return

    success = test_chat_message_endpoint()
    test_error_cases()

    print("\n" + "=" * 60)
    if success:
        print("🎯 Task 5 Requirements Met:")
        print("✅ Added chat.py in routes/ with POST /api/chat/message")
        print("✅ Accepts message and user context, returns Gemini response")
        print("✅ POST JSON body test successful, got chat reply")
        print("\n🚀 Ready for next phase!")
    else:
        print("❌ Some tests failed. Please check the implementation.")


if __name__ == "__main__":
    main()
