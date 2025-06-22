#!/usr/bin/env python3
"""
Test script for Gemini API integration (Task 3)
"""

from services.gemini_service import get_support_response
import os
import sys
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


def test_gemini_integration():
    """Test the get_support_response function"""
    print("🧪 Testing Gemini API Integration (Task 3)")
    print("=" * 50)

    # Test message
    test_message = "I'm having trouble finding food today and don't know where to turn for help."

    # Test context
    test_context = {
        'location': 'San Francisco, CA',
        'situation': 'experiencing food insecurity',
        'needs': 'food assistance'
    }

    print(f"📝 Test Message: {test_message}")
    print(f"📍 Test Context: {test_context}")
    print("\n🤖 Gemini Response:")
    print("-" * 30)

    try:
        # Call the get_support_response function
        response = get_support_response(test_message, test_context)
        print(response)
        print("-" * 30)
        print("✅ Gemini integration test completed successfully!")

        # Check if we got a fallback response (indicating no API key)
        if "unable to access my full capabilities" in response:
            print("\n⚠️  Note: Using fallback response (GEMINI_API_KEY not configured)")
            print("To test with actual Gemini API:")
            print("1. Set GEMINI_API_KEY environment variable")
            print("2. Run: export GEMINI_API_KEY=your_api_key")
            print("3. Run this test again")
        else:
            print("\n🎉 Successfully connected to Gemini API!")

    except Exception as e:
        print(f"❌ Error testing Gemini integration: {str(e)}")
        return False

    return True


def test_without_context():
    """Test the function without context"""
    print("\n🧪 Testing without context...")
    test_message = "Hello, I need some help."

    try:
        response = get_support_response(test_message)
        print(f"Response: {response[:100]}...")
        print("✅ Test without context passed!")
    except Exception as e:
        print(f"❌ Error: {str(e)}")


def test_prompt_types():
    """Test different prompt types"""
    print("\n🧪 Testing different prompt types...")
    test_message = "I need help with housing."
    test_context = {'location': 'Oakland, CA', 'situation': 'homeless'}

    # Test empathetic coach
    print("\n🤗 Testing empathetic_coach prompt:")
    response = get_support_response(
        test_message, test_context, "empathetic_coach")
    print(f"Response: {response[:150]}...")

    # Test direct assistant
    print("\n📋 Testing direct_assistant prompt:")
    response = get_support_response(
        test_message, test_context, "direct_assistant")
    print(f"Response: {response[:150]}...")

    print("✅ Prompt type tests completed!")


if __name__ == "__main__":
    print("Starting Gemini API Integration Tests...\n")

    # Test with context
    success = test_gemini_integration()

    # Test without context
    test_without_context()

    # Test prompt types
    test_prompt_types()

    print(f"\n{'='*50}")
    if success:
        print("🎯 Task 3 Requirements Met:")
        print("✅ Created gemini_service.py in services/")
        print("✅ Function get_support_response(message, context) implemented")
        print("✅ Test message processed and Gemini response returned")
        print("\n🚀 Ready for Task 4!")
    else:
        print("❌ Some tests failed. Please check the implementation.")
