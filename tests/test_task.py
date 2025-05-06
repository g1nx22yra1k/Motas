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
        self.assertEqual(str(self.task), "○ Test task")
        self.task.mark_complete()
        self.assertEqual(str(self.task), "✓ Test task")

if __name__ == '__main__':
    unittest.main()
