from TodoList import TodoList
from Task import Task
from TaskFilter import TaskFilter
import unittest

class testTaskFilter(unittest.TestCase):

    def setUp(self):
        self.todoList = TodoList()
        self.filter = TaskFilter(self.todoList)
        self.task1 = Task("Task 1", "Description 1", priority = "High", deadline= "04-30-2024")
        self.task2 = Task("Task 2", "Description 2", priority= "Low", deadline = "05-01-2024")
        self.task3 = Task("Task3", "Description 3", priority = "Normal", deadline = "05-22-2024")
        self.task3.isCompleted()
        self.todoList.addTask(self.task1)
        self.todoList.addTask(self.task2)
        self.todoList.addTask(self.task3)

    def test_priorityFilter(self):
        highPriority = self.filter.filterPriority("High")
        self.assertEqual(len(highPriority), 1)
        self.assertIn(self.task1, highPriority)
        self.assertNotIn(self.task2, highPriority)
        self.assertNotIn(self.task3, highPriority)

    def test_completedFilter(self):
        completed = self.filter.filterCompleted()
        self.assertEqual(len(completed), 1)
        self.assertIn(self.task3, completed)
        self.assertNotIn(self.task1, completed)
        self.assertNotIn(self.task2, completed)


if __name__ == "__main__":
    unittest.main()