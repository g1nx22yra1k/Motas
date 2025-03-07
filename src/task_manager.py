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
    
    def get_tasks_by_priority(self, priority):
        return [task for task in self.tasks if task.priority == priority]
    
    def get_tasks_sorted_by_priority(self):
        priority_order = {"high": 0, "medium": 1, "low": 2}
        return sorted(self.tasks, key=lambda task: priority_order.get(task.priority, 3))
    
    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            return True
        return False
