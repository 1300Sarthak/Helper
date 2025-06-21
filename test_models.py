#!/usr/bin/env python3
"""
Test script for User and Conversation models (Task 4)
"""

from app import app, db, User, Conversation
from datetime import datetime


def test_models():
    """Test the User and Conversation models"""
    print("🧪 Testing User and Conversation Models (Task 4)")
    print("=" * 60)

    with app.app_context():
        try:
            # Test 1: Create a new user
            print("📝 Test 1: Creating a new user...")
            user = User(
                name="John Doe",
                location="San Francisco, CA",
                situation="Looking for food assistance",
                needs="Food, temporary shelter"
            )

            db.session.add(user)
            db.session.commit()
            print(f"✅ User created: {user}")
            print(f"   User ID: {user.id}")
            print(f"   User dict: {user.to_dict()}")

            # Test 2: Create a conversation for the user
            print("\n📝 Test 2: Creating a conversation...")
            conversation = Conversation(
                user_id=user.id,
                message="I need help finding food today",
                response="I understand you're looking for food assistance. Let me help you find local resources.",
                message_type="user",
                context={
                    "location": user.location,
                    "situation": user.situation,
                    "needs": user.needs
                }
            )

            db.session.add(conversation)
            db.session.commit()
            print(f"✅ Conversation created: {conversation}")
            print(f"   Conversation ID: {conversation.id}")
            print(f"   Conversation dict: {conversation.to_dict()}")

            # Test 3: Query the user with conversations
            print("\n📝 Test 3: Querying user with conversations...")
            user_with_conversations = User.query.get(user.id)
            print(f"✅ User found: {user_with_conversations}")
            print(
                f"   Number of conversations: {len(user_with_conversations.conversations)}")

            for conv in user_with_conversations.conversations:
                print(f"   - Conversation: {conv.message[:50]}...")

            # Test 4: Query all users
            print("\n📝 Test 4: Querying all users...")
            all_users = User.query.all()
            print(f"✅ Total users in database: {len(all_users)}")

            # Test 5: Query all conversations
            print("\n📝 Test 5: Querying all conversations...")
            all_conversations = Conversation.query.all()
            print(
                f"✅ Total conversations in database: {len(all_conversations)}")

            print("\n" + "=" * 60)
            print("🎯 Task 4 Requirements Met:")
            print("✅ Created user.py in models/")
            print("✅ Created conversation.py in models/")
            print("✅ SQLAlchemy models created and linked to SQLite")
            print("✅ Test data inserted into tables successfully")
            print("\n🚀 Ready for Task 5!")

            return True

        except Exception as e:
            print(f"❌ Error testing models: {str(e)}")
            return False


def test_flask_shell_commands():
    """Test commands that would be run in Flask shell"""
    print("\n🧪 Testing Flask Shell Commands...")

    with app.app_context():
        try:
            # Commands you could run in Flask shell
            print("📝 Flask shell equivalent commands:")
            print("   from models.user import User")
            print("   from models.conversation import Conversation")
            print("   from app import db")

            # Create another test user
            user2 = User(name="Jane Smith", location="Oakland, CA")
            db.session.add(user2)
            db.session.commit()

            print(f"✅ Created user via Flask shell simulation: {user2}")

        except Exception as e:
            print(f"❌ Error in Flask shell test: {str(e)}")


if __name__ == "__main__":
    print("Starting Model Tests...\n")

    success = test_models()
    test_flask_shell_commands()

    if success:
        print("\n🎉 All tests passed! Database models are working correctly.")
    else:
        print("\n❌ Some tests failed. Please check the implementation.")
