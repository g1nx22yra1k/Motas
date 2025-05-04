#\!/usr/bin/env python3
"""
Motas - A simple task management system
"""

from src.task_manager import TaskManager

def main():
    print("Welcome to Motas\!")
    task_manager = TaskManager()
    
    # Demo tasks
    task_manager.add_task("Set up project", "Initialize the Motas project structure", "high")
    task_manager.add_task("Write documentation", "Create comprehensive README", "medium")
    
    print("\nPending tasks:")
    for task in task_manager.get_pending_tasks():
        print(f"  {task}")
    
if __name__ == "__main__":
    main()
