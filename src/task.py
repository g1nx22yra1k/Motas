"""
Task management module for Motas
"""

import datetime

class Task:
    def __init__(self, title, description="", priority="medium"):
        self.title = title
        self.description = description
        self.priority = priority
        self.completed = False
        self.created_at = datetime.datetime.now()
        self.completed_at = None
        
    def mark_complete(self):
        self.completed = True
        self.completed_at = datetime.datetime.now()
        
    def get_priority_symbol(self):
        priority_symbols = {
            "high": "🔴",
            "medium": "🟡", 
            "low": "🟢"
        }
        return priority_symbols.get(self.priority, "⚪")
        
    def __str__(self):
        status = "✓" if self.completed else "○"
        priority_symbol = self.get_priority_symbol()
        return f"{status} {priority_symbol} {self.title}"
    
    def to_dict(self):
        """Convert task to dictionary for serialization"""
        return {
            "title": self.title,
            "description": self.description,
            "priority": self.priority,
            "completed": self.completed,
            "created_at": self.created_at.isoformat(),
            "completed_at": self.completed_at.isoformat() if self.completed_at else None
        }
