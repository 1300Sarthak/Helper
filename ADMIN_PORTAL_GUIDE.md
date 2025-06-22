# 🔧 Admin Portal Guide

## Overview

The Helper app now includes a comprehensive admin portal for monitoring and managing the system. The admin portal provides real-time insights into user activity, conversation logs, and system statistics.

## Accessing the Admin Portal

### URL

- **Main Portal**: `http://localhost:5001/admin/`
- **Alternative**: `http://localhost:5001/admin` (redirects to main portal)

### Access Requirements

- Currently accessible from localhost (development mode)
- In production, implement proper authentication
- No login required for development environment

## Features

### 📊 Dashboard Tab

**Real-time Statistics:**

- Total Users registered
- Total Conversations/Messages
- Users active today
- Messages sent today

**Recent Activity Feed:**

- Last 20 conversation messages
- User names and message previews
- Timestamps for each interaction
- Real-time updates every 30 seconds

### 👥 Users Tab

**User Management:**

- Complete user list with details
- User ID, name, location, housing situation
- Registration date and last activity
- Message count per user
- Search and filter functionality
- CSV export capability

**User Information Displayed:**

- ID: Unique user identifier
- Name: User's provided name (or "Anonymous")
- Location: City/area information
- Situation: Housing status (shelter, unsheltered, etc.)
- Created: Registration timestamp
- Last Active: Most recent activity
- Messages: Total conversation count

### 💬 Conversations Tab

**Message Monitoring:**

- Last 100 conversations displayed
- User messages and AI responses
- Mode tracking (Coach vs Assistant)
- Timestamp information
- Search and filter by mode
- Response previews (truncated for readability)

**Conversation Details:**

- Time: When the message was sent
- User: Who sent the message
- Mode: Coach or Assistant mode
- Message: User's input message
- Response Preview: First 100 characters of AI response
- Emotion: Placeholder for future emotion analysis

### ⚙️ System Tab

**System Information:**

- API status indicators
- Database connection status
- RAG pipeline status
- Resource database statistics

**Resource Database Stats:**

- Total Resources: 64 available resources
- Oakland Resources: 32 local resources
- Berkeley Resources: 32 regional resources

**System Actions:**

- **Clear Old Data**: Remove conversations older than 30 days
- **Reset System**: Complete data wipe (DANGER - irreversible)

## Navigation

### Tab Switching

- Click any tab in the navigation bar
- Dashboard, Users, Conversations, System
- Active tab highlighted in blue
- Smooth transitions between sections

### Auto-Refresh

- Dashboard updates every 30 seconds automatically
- Manual refresh button (circular arrow) in bottom-right
- Click refresh button for immediate data update

### Search & Filtering

**Users Tab:**

- Search box filters by name, location, situation
- Real-time filtering as you type
- Case-insensitive search

**Conversations Tab:**

- Search box filters by message content
- Mode filter dropdown (All/Coach/Assistant)
- Combined filtering for precise results

## Data Export

### User Export

- Click "Export CSV" in Users tab
- Downloads complete user database
- Includes: ID, Name, Location, Situation, Dates, Contact info
- Filename: `users_export.csv`

### Data Format

```csv
ID,Name,Location,Situation,Created At,Last Active,Phone,Email
1,John Doe,Oakland,unsheltered,2025-06-21 20:15:00,2025-06-21 20:45:00,,
```

## System Management

### Data Cleanup

**Clear Old Data:**

- Removes conversations older than 30 days
- Preserves user accounts and recent activity
- Shows count of deleted records
- Requires confirmation before execution

**Reset System:**

- **WARNING**: Deletes ALL data permanently
- Removes all users and conversations
- Cannot be undone
- Requires double confirmation
- Use only for complete system reset

### Safety Features

- Confirmation dialogs for destructive actions
- Error handling with user-friendly messages
- Database rollback on failed operations
- Graceful error recovery

## API Endpoints

### Admin Routes

- `GET /admin/` - Main dashboard
- `GET /admin/export/users` - CSV export
- `POST /admin/clear-old-data` - Cleanup old conversations
- `POST /admin/reset-system` - Complete system reset
- `GET /admin/api/stats` - Real-time statistics JSON

### Example API Response

```json
{
  "total_users": 15,
  "total_conversations": 127,
  "today_users": 3,
  "today_conversations": 12
}
```

## Visual Design

### Modern Interface

- Clean, professional design
- Blue accent color (#007bff)
- Card-based layout for statistics
- Responsive grid system
- Hover effects and smooth transitions

### Status Indicators

- **Green badges**: Successful states, Coach mode
- **Blue badges**: Information, Assistant mode
- **Yellow badges**: Warnings, housing situations
- **Red badges**: Errors, dangerous actions

### Typography

- System fonts for optimal readability
- Clear hierarchy with proper font weights
- Consistent spacing and alignment
- Accessible color contrast

## Browser Compatibility

### Supported Browsers

- ✅ Chrome (recommended)
- ✅ Firefox
- ✅ Safari
- ✅ Edge
- ⚠️ Internet Explorer (limited support)

### Required Features

- Modern CSS Grid support
- JavaScript ES6+ features
- Fetch API for AJAX requests
- CSS Flexbox for layouts

## Security Considerations

### Current Implementation

- **Development Mode**: Open access from localhost
- **No Authentication**: Direct access to admin panel
- **Local Database**: SQLite for development

### Production Recommendations

- **Implement Authentication**: Admin login system
- **HTTPS Required**: Secure connections only
- **IP Restrictions**: Limit admin access by IP
- **Audit Logging**: Track admin actions
- **Regular Backups**: Automated database backups

### Data Privacy

- **User Data Protection**: Secure handling of personal information
- **Conversation Privacy**: Limited access to message content
- **Export Controls**: Secure CSV download handling
- **Data Retention**: Configurable cleanup policies

## Troubleshooting

### Common Issues

#### Admin Portal Not Loading

**Symptoms**: 404 or connection errors
**Solutions**:

- Check if Flask server is running on port 5001
- Verify admin routes are registered
- Check for import errors in server logs

#### 500 Internal Server Error

**Symptoms**: Server error page
**Solutions**:

- Check server logs for Python errors
- Verify database connection
- Ensure all model fields exist

#### Empty Data Display

**Symptoms**: No users or conversations shown
**Solutions**:

- Check if database has data
- Verify database queries are correct
- Test with sample data

#### Export Not Working

**Symptoms**: CSV download fails
**Solutions**:

- Check file permissions
- Verify CSV module import
- Test with smaller datasets

### Debug Mode

```bash
# Start server with debug output
python app.py

# Check specific admin route
curl -v http://localhost:5001/admin/

# Test API endpoints
curl http://localhost:5001/admin/api/stats
```

## Usage Examples

### Daily Monitoring

1. Open admin portal: `http://localhost:5001/admin/`
2. Check dashboard for daily statistics
3. Review recent activity for unusual patterns
4. Monitor user registration trends

### User Management

1. Go to Users tab
2. Search for specific users by name/location
3. Export user data for reporting
4. Track user engagement through message counts

### Conversation Analysis

1. Switch to Conversations tab
2. Filter by mode (Coach/Assistant) to analyze usage
3. Search for specific topics or keywords
4. Monitor response quality and user satisfaction

### System Maintenance

1. Navigate to System tab
2. Check API status indicators
3. Clear old data monthly (30+ days)
4. Monitor resource database statistics

## Future Enhancements

### Planned Features

- **Real-time Analytics**: Live charts and graphs
- **User Authentication**: Secure admin login system
- **Advanced Filtering**: Date ranges, emotion filters
- **Conversation Analytics**: Sentiment analysis, topic modeling
- **Automated Reports**: Daily/weekly summary emails
- **Resource Management**: Add/edit/remove resources
- **User Communication**: Direct messaging capabilities
- **Data Visualization**: Charts for trends and patterns

### Integration Opportunities

- **Google Analytics**: Web analytics integration
- **Slack Notifications**: Real-time alerts
- **Email Reports**: Automated admin summaries
- **Database Backups**: Automated backup system
- **Performance Monitoring**: System health dashboards

---

## Quick Start Checklist

- [ ] ✅ Flask server running on port 5001
- [ ] ✅ Admin routes registered and working
- [ ] ✅ Database connected with sample data
- [ ] ✅ Admin portal accessible at `/admin/`
- [ ] ✅ All tabs functioning (Dashboard, Users, Conversations, System)
- [ ] ✅ Search and filter features working
- [ ] ✅ CSV export operational
- [ ] ✅ System actions (clear data, reset) functional

**The admin portal is now fully operational! 🎉**

Access it at: **http://localhost:5001/admin/**
