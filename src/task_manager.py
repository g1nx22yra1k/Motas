"""
Task Manager for organizing and managing tasks
"""

from .task import Task

class TaskManager:
    def __init__(self):
        self.tasks = []
        
    def add_task(self, title, description="", priority="medium"):
        task = Task(title, description, priority)
        self.tasks.append(task)
        return task
        
    def get_tasks(self):
        return self.tasks
        
    def get_pending_tasks(self):
        return [task for task in self.tasks if not task.completed]
        
    def get_completed_tasks(self):
        return [task for task in self.tasks if task.completed]
