"""
Command-line interface for Motas
"""

import sys
from .task_manager import TaskManager

class CLI:
    def __init__(self):
        self.task_manager = TaskManager()
    
    def run(self):
        print("Welcome to Motas\! A simple task management system.")
        
    def add_task(self, title, description="", priority="medium"):
        return self.task_manager.add_task(title, description, priority)
    
    def list_tasks(self):
        return self.task_manager.get_tasks()

if __name__ == "__main__":
    cli = CLI()
    cli.run()
