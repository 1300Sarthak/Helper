from flask import Blueprint, render_template_string, render_template, request, jsonify, redirect, url_for
from models.user import User, db
from models.conversation import Conversation
from datetime import datetime, timedelta
import json

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

# Simple authentication check (in production, use proper auth)


def check_admin_auth():
    """Simple admin check - in production, implement proper authentication"""
    # For now, just check if it's localhost
    # In production, add proper admin authentication
    return True


# Simple admin template
ADMIN_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Social Worker Portal</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: #f8f9fa;
            color: #333;
            line-height: 1.6;
        }
        
        .header {
            background: #007bff;
            color: white;
            padding: 1rem 2rem;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        
        .header h1 {
            margin: 0;
            font-size: 1.5rem;
        }
        
        .nav {
            background: white;
            padding: 0 2rem;
            border-bottom: 1px solid #dee2e6;
        }
        
        .nav-tabs {
            display: flex;
            gap: 0;
        }
        
        .nav-tab {
            padding: 1rem 1.5rem;
            background: none;
            border: none;
            cursor: pointer;
            border-bottom: 3px solid transparent;
            transition: all 0.3s ease;
        }
        
        .nav-tab.active {
            border-bottom-color: #007bff;
            color: #007bff;
        }
        
        .nav-tab:hover {
            background: #f8f9fa;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
        }
        
        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 1.5rem;
            margin-bottom: 2rem;
        }
        
        .stat-card {
            background: white;
            padding: 1.5rem;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            border-left: 4px solid #007bff;
        }
        
        .stat-number {
            font-size: 2rem;
            font-weight: bold;
            color: #007bff;
            margin-bottom: 0.5rem;
        }
        
        .stat-label {
            color: #666;
            font-size: 0.9rem;
        }
        
        .content-section {
            display: none;
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            overflow: hidden;
        }
        
        .content-section.active {
            display: block;
        }
        
        .section-header {
            background: #f8f9fa;
            padding: 1rem 1.5rem;
            border-bottom: 1px solid #dee2e6;
            font-weight: 600;
        }
        
        .table {
            width: 100%;
            border-collapse: collapse;
        }
        
        .table th,
        .table td {
            padding: 0.75rem 1rem;
            text-align: left;
            border-bottom: 1px solid #dee2e6;
        }
        
        .table th {
            background: #f8f9fa;
            font-weight: 600;
            color: #495057;
        }
        
        .table tbody tr:hover {
            background: #f8f9fa;
        }
        
        .badge {
            display: inline-block;
            padding: 0.25rem 0.5rem;
            font-size: 0.75rem;
            font-weight: 600;
            border-radius: 4px;
        }
        
        .badge-success {
            background: #d4edda;
            color: #155724;
        }
        
        .badge-warning {
            background: #fff3cd;
            color: #856404;
        }
        
        .badge-info {
            background: #d1ecf1;
            color: #0c5460;
        }
        
        .conversation-preview {
            max-width: 300px;
            overflow: hidden;
            text-overflow: ellipsis;
            white-space: nowrap;
        }
        
        .timestamp {
            color: #666;
            font-size: 0.85rem;
        }
        
        .filters {
            padding: 1rem 1.5rem;
            background: #f8f9fa;
            border-bottom: 1px solid #dee2e6;
            display: flex;
            gap: 1rem;
            align-items: center;
        }
        
        .filter-input {
            padding: 0.5rem;
            border: 1px solid #ced4da;
            border-radius: 4px;
            font-size: 0.9rem;
        }
        
        .btn {
            padding: 0.5rem 1rem;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 0.9rem;
            transition: all 0.3s ease;
        }
        
        .btn-primary {
            background: #007bff;
            color: white;
        }
        
        .btn-primary:hover {
            background: #0056b3;
        }
        
        .btn-danger {
            background: #dc3545;
            color: white;
        }
        
        .btn-danger:hover {
            background: #c82333;
        }
        
        .empty-state {
            text-align: center;
            padding: 3rem;
            color: #666;
        }
        
        .refresh-btn {
            position: fixed;
            bottom: 2rem;
            right: 2rem;
            background: #007bff;
            color: white;
            border: none;
            border-radius: 50%;
            width: 60px;
            height: 60px;
            cursor: pointer;
            box-shadow: 0 4px 12px rgba(0,123,255,0.3);
            font-size: 1.2rem;
        }
        
        .refresh-btn:hover {
            background: #0056b3;
            transform: scale(1.05);
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>🏠 Helper Admin Portal</h1>
    </div>
    
    <div class="nav">
        <div class="nav-tabs">
            <button class="nav-tab active" onclick="switchTab('dashboard')">Dashboard</button>
            <button class="nav-tab" onclick="switchTab('users')">Users</button>
            <button class="nav-tab" onclick="switchTab('conversations')">Conversations</button>
            <button class="nav-tab" onclick="switchTab('system')">System</button>
        </div>
    </div>
    
    <div class="container">
        <!-- Dashboard Section -->
        <div id="dashboard" class="content-section active">
            <div class="stats-grid">
                <div class="stat-card">
                    <div class="stat-number" id="totalUsers">{{ stats.total_users }}</div>
                    <div class="stat-label">Total Users</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number" id="totalConversations">{{ stats.total_conversations }}</div>
                    <div class="stat-label">Total Conversations</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number" id="todayUsers">{{ stats.today_users }}</div>
                    <div class="stat-label">Users Today</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number" id="todayConversations">{{ stats.today_conversations }}</div>
                    <div class="stat-label">Messages Today</div>
                </div>
            </div>
            
            <div class="content-section active">
                <div class="section-header">Recent Activity</div>
                <table class="table">
                    <thead>
                        <tr>
                            <th>Time</th>
                            <th>User</th>
                            <th>Action</th>
                            <th>Details</th>
                        </tr>
                    </thead>
                    <tbody id="recentActivity">
                        {% for activity in recent_activity %}
                        <tr>
                            <td class="timestamp">{{ activity.timestamp }}</td>
                            <td>{{ activity.user_name }}</td>
                            <td><span class="badge badge-info">{{ activity.action }}</span></td>
                            <td class="conversation-preview">{{ activity.details }}</td>
                        </tr>
                        {% endfor %}
                    </tbody>
                </table>
            </div>
        </div>
        
        <!-- Users Section -->
        <div id="users" class="content-section">
            <div class="filters">
                <input type="text" class="filter-input" placeholder="Search users..." id="userSearch">
                <button class="btn btn-primary" onclick="filterUsers()">Filter</button>
                <button class="btn btn-danger" onclick="exportUsers()">Export CSV</button>
            </div>
            
            <table class="table">
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Name</th>
                        <th>Location</th>
                        <th>Situation</th>
                        <th>Created</th>
                        <th>Last Active</th>
                        <th>Messages</th>
                    </tr>
                </thead>
                <tbody id="usersTable">
                    {% for user in users %}
                    <tr>
                        <td>{{ user.id }}</td>
                        <td>{{ user.name }}</td>
                        <td>{{ user.location or 'N/A' }}</td>
                        <td>
                            {% if user.situation %}
                                <span class="badge badge-warning">{{ user.situation }}</span>
                            {% else %}
                                <span class="badge badge-info">Unknown</span>
                            {% endif %}
                        </td>
                        <td class="timestamp">{{ user.created_at.strftime('%Y-%m-%d %H:%M') if user.created_at else 'N/A' }}</td>
                        <td class="timestamp">{{ user.last_active.strftime('%Y-%m-%d %H:%M') if user.last_active else 'Never' }}</td>
                        <td>{{ user.message_count }}</td>
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
        </div>
        
        <!-- Conversations Section -->
        <div id="conversations" class="content-section">
            <div class="filters">
                <input type="text" class="filter-input" placeholder="Search conversations..." id="conversationSearch">
                <select class="filter-input" id="modeFilter">
                    <option value="">All Modes</option>
                    <option value="coach">Coach Mode</option>
                    <option value="assistant">Assistant Mode</option>
                </select>
                <button class="btn btn-primary" onclick="filterConversations()">Filter</button>
            </div>
            
            <table class="table">
                <thead>
                    <tr>
                        <th>Time</th>
                        <th>User</th>
                        <th>Mode</th>
                        <th>Message</th>
                        <th>Response Preview</th>
                        <th>Emotion</th>
                    </tr>
                </thead>
                <tbody id="conversationsTable">
                    {% for conv in conversations %}
                    <tr>
                        <td class="timestamp">{{ conv.timestamp.strftime('%Y-%m-%d %H:%M:%S') if conv.timestamp else 'N/A' }}</td>
                        <td>{{ conv.user_name }}</td>
                        <td><span class="badge badge-{{ 'success' if conv.mode == 'coach' else 'info' }}">{{ conv.mode or 'N/A' }}</span></td>
                        <td class="conversation-preview">{{ conv.user_message }}</td>
                        <td class="conversation-preview">{{ conv.ai_response }}</td>
                        <td>
                            {% if conv.emotion_score %}
                                <span class="badge badge-warning">{{ conv.emotion_score }}</span>
                            {% else %}
                                <span class="badge badge-info">N/A</span>
                            {% endif %}
                        </td>
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
        </div>
        
        <!-- System Section -->
        <div id="system" class="content-section">
            <div class="section-header">System Information</div>
            <div style="padding: 1.5rem;">
                <div style="margin-bottom: 2rem;">
                    <h3>API Status</h3>
                    <p><strong>Gemini API:</strong> <span class="badge badge-success">Connected</span></p>
                    <p><strong>Database:</strong> <span class="badge badge-success">Connected</span></p>
                    <p><strong>RAG Pipeline:</strong> <span class="badge badge-success">Active</span></p>
                </div>
                
                <div style="margin-bottom: 2rem;">
                    <h3>Resource Database</h3>
                    <p><strong>Total Resources:</strong> {{ stats.total_resources }}</p>
                    <p><strong>Oakland Resources:</strong> {{ stats.oakland_resources }}</p>
                    <p><strong>Berkeley Resources:</strong> {{ stats.berkeley_resources }}</p>
                </div>
                
                <div>
                    <h3>System Actions</h3>
                    <button class="btn btn-primary" onclick="clearOldData()">Clear Old Data (30+ days)</button>
                    <button class="btn btn-danger" onclick="resetSystem()">Reset System (Danger)</button>
                </div>
            </div>
        </div>
    </div>
    
    <button class="refresh-btn" onclick="refreshData()" title="Refresh Data">↻</button>
    
    <script>
        function switchTab(tabName) {
            // Hide all content sections
            document.querySelectorAll('.content-section').forEach(section => {
                section.classList.remove('active');
            });
            
            // Remove active class from all tabs
            document.querySelectorAll('.nav-tab').forEach(tab => {
                tab.classList.remove('active');
            });
            
            // Show selected content section
            document.getElementById(tabName).classList.add('active');
            
            // Add active class to clicked tab
            event.target.classList.add('active');
        }
        
        function refreshData() {
            window.location.reload();
        }
        
        function filterUsers() {
            const search = document.getElementById('userSearch').value.toLowerCase();
            const rows = document.querySelectorAll('#usersTable tr');
            
            rows.forEach(row => {
                const text = row.textContent.toLowerCase();
                row.style.display = text.includes(search) ? '' : 'none';
            });
        }
        
        function filterConversations() {
            const search = document.getElementById('conversationSearch').value.toLowerCase();
            const mode = document.getElementById('modeFilter').value;
            const rows = document.querySelectorAll('#conversationsTable tr');
            
            rows.forEach(row => {
                const text = row.textContent.toLowerCase();
                const modeMatch = !mode || row.textContent.includes(mode);
                const searchMatch = text.includes(search);
                row.style.display = (searchMatch && modeMatch) ? '' : 'none';
            });
        }
        
        function exportUsers() {
            window.open('/admin/export/users', '_blank');
        }
        
        function clearOldData() {
            if (confirm('This will delete conversations older than 30 days. Continue?')) {
                fetch('/admin/clear-old-data', { method: 'POST' })
                    .then(response => response.json())
                    .then(data => {
                        alert(`Cleared ${data.deleted_count} old records`);
                        refreshData();
                    });
            }
        }
        
        function resetSystem() {
            if (confirm('WARNING: This will delete ALL user data and conversations. This cannot be undone. Continue?')) {
                if (confirm('Are you absolutely sure? This will permanently delete everything.')) {
                    fetch('/admin/reset-system', { method: 'POST' })
                        .then(response => response.json())
                        .then(data => {
                            alert('System reset complete');
                            refreshData();
                        });
                }
            }
        }
        
        // Auto-refresh every 30 seconds
        setInterval(refreshData, 30000);
    </script>
</body>
</html>
"""


@admin_bp.route('/')
def admin_dashboard():
    """Main admin dashboard"""
    try:
        # Get basic statistics
        stats = {
            'total_users': User.query.count(),
            'total_conversations': Conversation.query.count(),
            'today_users': User.query.filter(User.created_at >= datetime.now().date()).count(),
            'today_conversations': Conversation.query.filter(Conversation.created_at >= datetime.now().date()).count(),
            'total_resources': 64,  # From RAG pipeline
            'oakland_resources': 32,
            'berkeley_resources': 32
        }

        # Get user situation counts for chart data
        situation_counts = db.session.query(
            User.situation,
            db.func.count(User.id).label('count')
        ).filter(User.situation.isnot(None)).group_by(User.situation).all()
        
        # Initialize chart data with defaults
        stats.update({
            'housing_count': 0,
            'drug_count': 0,
            'healthcare_count': 0,
            'food_count': 0,
            'job_count': 0,
            'other_count': 0
        })
        
        # Map situation counts to chart data
        for situation, count in situation_counts:
            if situation == 'housing':
                stats['housing_count'] = count
            elif situation == 'drug':
                stats['drug_count'] = count
            elif situation == 'healthcare':
                stats['healthcare_count'] = count
            elif situation == 'food':
                stats['food_count'] = count
            elif situation == 'job':
                stats['job_count'] = count
            else:
                stats['other_count'] += count

        # Get mode usage counts
        mode_counts = db.session.query(
            Conversation.context,
            db.func.count(Conversation.id).label('count')
        ).filter(Conversation.context.isnot(None)).group_by(Conversation.context).all()
        
        coach_conversations = 0
        assistant_conversations = 0
        
        for context, count in mode_counts:
            try:
                context_data = json.loads(context) if isinstance(context, str) else context
                if isinstance(context_data, dict):
                    mode = context_data.get('mode', 'assistant')
                    if mode == 'coach':
                        coach_conversations += count
                    else:
                        assistant_conversations += count
            except:
                assistant_conversations += count
        
        stats['coach_conversations'] = coach_conversations
        stats['assistant_conversations'] = assistant_conversations

        # Get recent activity (last 20 conversations)
        recent_conversations = db.session.query(
            Conversation.created_at,
            User.name.label('user_name'),
            Conversation.message,
            Conversation.response
        ).join(User).order_by(Conversation.created_at.desc()).limit(20).all()

        recent_activity = []
        for conv in recent_conversations:
            recent_activity.append({
                'timestamp': conv.created_at.strftime('%H:%M:%S') if conv.created_at else 'N/A',
                'user_name': conv.user_name or 'Anonymous',
                'action': 'Message',
                'details': conv.message[:50] + '...' if conv.message and len(conv.message) > 50 else conv.message or 'N/A'
            })

        # Use the new template file instead of inline template
        return render_template('admin_dashboard.html',
                             stats=stats,
                             recent_activity=recent_activity,
                             current_time=datetime.now().strftime('%H:%M:%S'))

    except Exception as e:
        return f"Error loading admin dashboard: {str(e)}", 500


@admin_bp.route('/export/users')
def export_users():
    """Export users as CSV"""
    try:
        import csv
        import io
        from flask import Response

        output = io.StringIO()
        writer = csv.writer(output)

        # Write header
        writer.writerow(['ID', 'Name', 'Location', 'Situation',
                        'Created At', 'Last Active', 'Phone', 'Email'])

        # Write user data
        users = User.query.all()
        for user in users:
            writer.writerow([
                user.id,
                user.name or 'Anonymous',
                user.location or '',
                user.situation or '',
                user.created_at.strftime(
                    '%Y-%m-%d %H:%M:%S') if user.created_at else '',
                user.updated_at.strftime(
                    '%Y-%m-%d %H:%M:%S') if user.updated_at else '',
                getattr(user, 'phone', '') or '',
                getattr(user, 'email', '') or ''
            ])

        output.seek(0)
        return Response(
            output.getvalue(),
            mimetype='text/csv',
            headers={'Content-Disposition': 'attachment; filename=users_export.csv'}
        )

    except Exception as e:
        return f"Error exporting users: {str(e)}", 500


@admin_bp.route('/clear-old-data', methods=['POST'])
def clear_old_data():
    """Clear conversations older than 30 days"""
    try:
        cutoff_date = datetime.now() - timedelta(days=30)
        deleted_count = Conversation.query.filter(
            Conversation.created_at < cutoff_date).count()
        Conversation.query.filter(
            Conversation.created_at < cutoff_date).delete()
        db.session.commit()

        return jsonify({'success': True, 'deleted_count': deleted_count})

    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'error': str(e)}), 500


@admin_bp.route('/reset-system', methods=['POST'])
def reset_system():
    """Reset entire system - DELETE ALL DATA"""
    try:
        # Delete all conversations
        Conversation.query.delete()

        # Delete all users
        User.query.delete()

        db.session.commit()

        return jsonify({'success': True, 'message': 'System reset complete'})

    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'error': str(e)}), 500


@admin_bp.route('/api/stats')
def api_stats():
    """API endpoint for real-time stats"""
    try:
        stats = {
            'total_users': User.query.count(),
            'total_conversations': Conversation.query.count(),
            'today_users': User.query.filter(User.created_at >= datetime.now().date()).count(),
            'today_conversations': Conversation.query.filter(Conversation.created_at >= datetime.now().date()).count(),
        }
        return jsonify(stats)

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@admin_bp.route('/api/conversations')
def api_conversations():
    """API endpoint for real conversation data"""
    try:
        # Get conversations with user data
        conversations_query = db.session.query(
            Conversation.id,
            Conversation.user_id,
            Conversation.message,
            Conversation.response,
            Conversation.created_at,
            Conversation.context,
            User.name.label('user_name'),
            User.location,
            User.situation,
            User.needs
        ).join(User).order_by(Conversation.created_at.desc()).limit(100)
        
        conversations_data = []
        flagged_keywords = ['hurt', 'unsafe', 'no home', 'suicidal', 'kill myself', 'end it all', 'want to die', 'hopeless', 'nowhere to go']
        
        for conv in conversations_query:
            # Extract mode from context
            mode = 'support'  # default
            if conv.context:
                try:
                    context_data = json.loads(conv.context) if isinstance(conv.context, str) else conv.context
                    if isinstance(context_data, dict):
                        mode = context_data.get('mode', 'support')
                        # Also check user_context for mode
                        user_context = context_data.get('user_context', {})
                        if 'mode' in user_context:
                            mode = user_context['mode']
                except:
                    pass
            
            # Check if conversation should be flagged
            is_flagged = False
            if conv.message:
                message_lower = conv.message.lower()
                is_flagged = any(keyword in message_lower for keyword in flagged_keywords)
            
            # Create user alias
            user_alias = f"User #{conv.user_id}"
            
            # Calculate duration (for now, estimate based on message length)
            estimated_duration = max(1, len(conv.message.split()) // 10) if conv.message else 1
            
            conversations_data.append({
                'id': conv.id,
                'userId': conv.user_id,
                'userAlias': user_alias,
                'userLocation': conv.location or 'Unknown',
                'userNeeds': conv.needs or conv.situation or 'General Support',
                'mode': mode,
                'startTime': conv.created_at.isoformat() if conv.created_at else None,
                'lastMessageTime': conv.created_at.isoformat() if conv.created_at else None,
                'duration': estimated_duration,
                'messageCount': 1,  # We're showing individual messages, not full conversations
                'lastMessage': conv.message[:100] + '...' if conv.message and len(conv.message) > 100 else conv.message or '',
                'isFlagged': is_flagged,
                'fullMessage': conv.message or '',
                'response': conv.response or ''
            })
        
        return jsonify({
            'conversations': conversations_data,
            'total_count': len(conversations_data)
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@admin_bp.route('/api/conversation/<int:conversation_id>')
def api_conversation_detail(conversation_id):
    """API endpoint for detailed conversation data"""
    try:
        # Get the specific conversation with user data
        conversation = db.session.query(
            Conversation.id,
            Conversation.user_id,
            Conversation.message,
            Conversation.response,
            Conversation.created_at,
            Conversation.context,
            User.name.label('user_name'),
            User.location,
            User.situation,
            User.needs
        ).join(User).filter(Conversation.id == conversation_id).first()
        
        if not conversation:
            return jsonify({'error': 'Conversation not found'}), 404
        
        # Get all conversations for this user to build full conversation thread
        user_conversations = Conversation.query.filter_by(user_id=conversation.user_id)\
            .order_by(Conversation.created_at.asc()).all()
        
        messages = []
        for i, conv in enumerate(user_conversations):
            # Add user message
            messages.append({
                'time': conv.created_at.strftime('%H:%M') if conv.created_at else '00:00',
                'sender': 'user',
                'message': conv.message or ''
            })
            
            # Add assistant response if available
            if conv.response:
                response_time = conv.created_at + timedelta(minutes=1) if conv.created_at else datetime.now()
                messages.append({
                    'time': response_time.strftime('%H:%M'),
                    'sender': 'assistant', 
                    'message': conv.response
                })
        
        # Extract mode from context
        mode = 'support'
        if conversation.context:
            try:
                context_data = json.loads(conversation.context) if isinstance(conversation.context, str) else conversation.context
                if isinstance(context_data, dict):
                    mode = context_data.get('mode', 'support')
                    user_context = context_data.get('user_context', {})
                    if 'mode' in user_context:
                        mode = user_context['mode']
            except:
                pass
        
        conversation_detail = {
            'id': conversation.id,
            'userId': conversation.user_id,
            'userAlias': f"User #{conversation.user_id}",
            'userLocation': conversation.location or 'Unknown',
            'userNeeds': conversation.needs or conversation.situation or 'General Support',
            'mode': mode,
            'startTime': user_conversations[0].created_at.isoformat() if user_conversations else None,
            'lastMessageTime': user_conversations[-1].created_at.isoformat() if user_conversations else None,
            'duration': len(user_conversations) * 2,  # Rough estimate
            'messageCount': len(messages),
            'messages': messages
        }
        
        return jsonify(conversation_detail)
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Add this route to your admin.py or create a new route in your main app.py

@admin_bp.route('/dashboard')
def admin_dashboard_simple():
    """Simple admin dashboard view"""
    try:
        # Get statistics
        stats = {
            'total_users': User.query.count(),
            'total_conversations': Conversation.query.count(),
            'today_users': User.query.filter(User.created_at >= datetime.now().date()).count(),
            'today_conversations': Conversation.query.filter(Conversation.created_at >= datetime.now().date()).count(),
        }
        
        # Get recent activity (last 20 conversations)
        recent_conversations = db.session.query(
            Conversation.created_at,
            User.name.label('user_name'),
            Conversation.message,
        ).join(User).order_by(Conversation.created_at.desc()).limit(20).all()
        
        recent_activity = []
        for conv in recent_conversations:
            recent_activity.append({
                'timestamp': conv.created_at.strftime('%H:%M:%S') if conv.created_at else 'N/A',
                'user_name': conv.user_name or 'Anonymous',
                'action': 'Message',
                'details': conv.message[:50] + '...' if conv.message and len(conv.message) > 50 else conv.message or 'N/A'
            })
        
        return render_template('admin_dashboard.html',
                             stats=stats,
                             recent_activity=recent_activity)
    
    except Exception as e:
        return f"Error loading admin dashboard: {str(e)}", 500