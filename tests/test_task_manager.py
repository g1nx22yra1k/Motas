"""
Unit tests for TaskManager class
"""

import unittest
from src.task_manager import TaskManager

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.manager = TaskManager()
    
    def test_add_task(self):
        task = self.manager.add_task("Test task", "Description", "high")
        self.assertEqual(len(self.manager.tasks), 1)
        self.assertEqual(task.title, "Test task")
    
    def test_get_pending_tasks(self):
        task1 = self.manager.add_task("Task 1")
        task2 = self.manager.add_task("Task 2")
        task1.mark_complete()
        
        pending = self.manager.get_pending_tasks()
        self.assertEqual(len(pending), 1)
        self.assertEqual(pending[0].title, "Task 2")
    
    def test_get_completed_tasks(self):
        task1 = self.manager.add_task("Task 1")
        task2 = self.manager.add_task("Task 2")
        task1.mark_complete()
        
        completed = self.manager.get_completed_tasks()
        self.assertEqual(len(completed), 1)
        self.assertEqual(completed[0].title, "Task 1")

if __name__ == '__main__':
    unittest.main()
