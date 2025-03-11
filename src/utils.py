"""
Utility functions for Motas
"""

import re
from datetime import datetime

def validate_priority(priority):
    """Validate priority level"""
    valid_priorities = ["high", "medium", "low"]
    return priority.lower() in valid_priorities

def sanitize_title(title):
    """Sanitize task title by removing excessive whitespace"""
    return re.sub(r'\s+', ' ', title.strip())

def format_date(date_obj):
    """Format datetime object for display"""
    if date_obj is None:
        return "Never"
    return date_obj.strftime("%Y-%m-%d %H:%M")
