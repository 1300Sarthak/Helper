#!/usr/bin/env python3
"""
Simple test script for the CAG Chatbot Flask API
"""

import requests
import json
import time

BASE_URL = "http://localhost:5000"


def test_health_check():
    """Test the health check endpoint"""
    print("Testing health check...")
    try:
        response = requests.get(f"{BASE_URL}/")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Health check passed: {data['message']}")
            return True
        else:
            print(f"❌ Health check failed: {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print("❌ Could not connect to the API. Make sure the Flask app is running.")
        return False


def test_chat_endpoint():
    """Test the chat endpoint"""
    print("\nTesting chat endpoint...")
    try:
        payload = {
            "message": "Hello, this is a test message",
            "user_id": "test_user_123"
        }

        response = requests.post(
            f"{BASE_URL}/api/chat",
            json=payload,
            headers={"Content-Type": "application/json"}
        )

        if response.status_code == 200:
            data = response.json()
            print(f"✅ Chat endpoint passed")
            print(f"   Response: {data['response']}")
            print(f"   User ID: {data['user_id']}")
            return True
        else:
            print(f"❌ Chat endpoint failed: {response.status_code}")
            print(f"   Error: {response.text}")
            return False
    except Exception as e:
        print(f"❌ Chat endpoint error: {str(e)}")
        return False


def test_chat_history():
    """Test the chat history endpoint"""
    print("\nTesting chat history endpoint...")
    try:
        response = requests.get(
            f"{BASE_URL}/api/chat/history?user_id=test_user_123")

        if response.status_code == 200:
            data = response.json()
            print(f"✅ Chat history endpoint passed")
            print(f"   Total messages: {data['total_messages']}")
            return True
        else:
            print(f"❌ Chat history endpoint failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Chat history endpoint error: {str(e)}")
        return False


def test_status_endpoint():
    """Test the status endpoint"""
    print("\nTesting status endpoint...")
    try:
        response = requests.get(f"{BASE_URL}/api/status")

        if response.status_code == 200:
            data = response.json()
            print(f"✅ Status endpoint passed")
            print(f"   Status: {data['status']}")
            print(
                f"   CAG API configured: {data['config']['cag_api_configured']}")
            print(
                f"   Total chat entries: {data['stats']['total_chat_entries']}")
            return True
        else:
            print(f"❌ Status endpoint failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Status endpoint error: {str(e)}")
        return False


def main():
    """Run all tests"""
    print("🧪 Testing CAG Chatbot Flask API")
    print("=" * 40)

    tests = [
        test_health_check,
        test_chat_endpoint,
        test_chat_history,
        test_status_endpoint
    ]

    passed = 0
    total = len(tests)

    for test in tests:
        if test():
            passed += 1
        time.sleep(0.5)  # Small delay between tests

    print("\n" + "=" * 40)
    print(f"📊 Test Results: {passed}/{total} tests passed")

    if passed == total:
        print("🎉 All tests passed! The API is working correctly.")
    else:
        print("⚠️  Some tests failed. Check the Flask app logs for more details.")


if __name__ == "__main__":
    main()
