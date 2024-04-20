from TodoList import TodoList
from Task import Task
from TaskSort import TaskSort
import unittest

class testTaskSort(unittest.TestCase):

    def setUp(self):
        self.todoList = TodoList()
        self.sort = TaskSort(self.todoList)

        self.task1 = Task("Task 1", "Description 1", priority="Normal", deadline="04-30-2024")
        self.task2 = Task("Task 2", "Description 2", priority="Low", deadline="05-22-2024")
        self.task3 = Task("Task 3", "Description 3", priority="High", deadline="05-01-2024")

        self.todoList.addTask(self.task1)
        self.todoList.addTask(self.task2)
        self.todoList.addTask(self.task3)


    def test_sortDeadline(self):
        sorted = self.sort.sortByDeadline()
        expected = [self.task1, self.task3, self.task2]
        self.assertEqual(sorted, expected)

    def test_sortPriority(self):
        sorted = self.sort.sortByPriority()
        expected = [self.task3, self.task1, self.task2]
        self.assertEqual(sorted, expected)


if __name__ == "__main__":
    unittest.main()