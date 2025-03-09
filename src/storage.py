"""
Storage module for persisting tasks
"""

import json
import os
from datetime import datetime
from .task import Task

class TaskStorage:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.ensure_file_exists()
    
    def ensure_file_exists(self):
        if not os.path.exists(self.filename):
            with open(self.filename, 'w') as f:
                json.dump([], f)
    
    def save_tasks(self, tasks):
        task_data = []
        for task in tasks:
            task_dict = {
                "title": task.title,
                "description": task.description,
                "priority": task.priority,
                "completed": task.completed,
                "created_at": task.created_at.isoformat(),
                "completed_at": task.completed_at.isoformat() if task.completed_at else None
            }
            task_data.append(task_dict)
        
        with open(self.filename, 'w') as f:
            json.dump(task_data, f, indent=2)
    
    def load_tasks(self):
        try:
            with open(self.filename, 'r') as f:
                task_data = json.load(f)
            
            tasks = []
            for data in task_data:
                task = Task(data["title"], data["description"], data["priority"])
                task.completed = data["completed"]
                task.created_at = datetime.fromisoformat(data["created_at"])
                if data.get("completed_at"):
                    task.completed_at = datetime.fromisoformat(data["completed_at"])
                tasks.append(task)
            
            return tasks
        except (FileNotFoundError, json.JSONDecodeError):
            return []
