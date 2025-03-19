"""
Unit tests for Task class
"""

import unittest
from src.task import Task

class TestTask(unittest.TestCase):
    def setUp(self):
        self.task = Task("Test task", "This is a test task", "high")
    
    def test_task_creation(self):
        self.assertEqual(self.task.title, "Test task")
        self.assertEqual(self.task.description, "This is a test task")
        self.assertEqual(self.task.priority, "high")
        self.assertFalse(self.task.completed)
    
    def test_mark_complete(self):
        self.task.mark_complete()
        self.assertTrue(self.task.completed)
    
    def test_str_representation(self):
        self.assertIn("○", str(self.task))
        self.assertIn("Test task", str(self.task))
        self.task.mark_complete()
        self.assertIn("✓", str(self.task))
    
    def test_to_dict(self):
        task_dict = self.task.to_dict()
        self.assertEqual(task_dict["title"], "Test task")
        self.assertEqual(task_dict["priority"], "high")
        self.assertFalse(task_dict["completed"])
    
    def test_priority_symbols(self):
        high_task = Task("High", priority="high")
        medium_task = Task("Medium", priority="medium")
        low_task = Task("Low", priority="low")
        
        self.assertEqual(high_task.get_priority_symbol(), "🔴")
        self.assertEqual(medium_task.get_priority_symbol(), "🟡")
        self.assertEqual(low_task.get_priority_symbol(), "🟢")

if __name__ == '__main__':
    unittest.main()
