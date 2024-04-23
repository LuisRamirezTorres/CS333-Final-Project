from Task import Task
from TodoList import TodoList
from TaskEditor import TaskEditor
from TaskFilter import TaskFilter
from TaskSort import TaskSort
import unittest

class TodoListIntegrationTests(unittest.TestCase):

    def setUp(self):
        self.todoList = TodoList()
        self.taskEditor = TaskEditor(self.todoList)
        self.taskFilter = TaskFilter(self.todoList)
        self.taskSort = TaskSort(self.todoList)


    def test_addAndEditTask(self):
        task1 = Task("my task", "new task", "Normal", "04-30-2024")
        self.todoList.addTask(task1)
        self.assertEqual(len(self.todoList.tasks), 1)

        self.taskEditor.editTask(task1, newName= "updated task name")
        self.assertEqual(task1.name, "updated task name")


    def test_addAndFilterByCompleted(self):
        task1 = Task("Dishes", "I need to do the dishes", "Normal", "04-30-2024")
        task2 = Task("Trash", "I need to take the trash out", "Normal", "05-01-2024")

        self.todoList.addTask(task1)
        self.todoList.addTask(task2)

        task1.isCompleted()

        completedTask = self.taskFilter.filterCompleted()
        self.assertEqual(len(completedTask), 1)
        self.assertIn(task1, completedTask)

    def test_addEditAndFilterByPriority(self):
        task1 = Task("name", "description", "Low", "04-30-2024")
        task2 = Task("name2", "description 2", "High", "05-01-2024")

        self.todoList.addTask(task1)
        self.todoList.addTask(task2)

        #switch priorities
        self.taskEditor.editTask(task2, None, None, "Low", None)
        self.taskEditor.editTask(task1, None, None, "High", None)

        highPriorityTask = self.taskFilter.filterPriority("High")
        self.assertEqual(len(highPriorityTask), 1)
        self.assertIn(task1, highPriorityTask)
        self.assertNotIn(task2, highPriorityTask)

    def test_addEditAndSortByDeadline(self):
        task1 = Task("name 1", "Description 1", "Low", "04-30-2024")
        task2 = Task("name 2", "Description 2", "Low", "05-22-2024")

        self.todoList.addTask(task1)
        self.todoList.addTask(task2)

        #switch deadline so the order should be [task2, task1]
        self.taskEditor.editTask(task1, None, None, None, "05-22-2024")
        self.taskEditor.editTask(task2, None, None, None, "04-30-2024")

        sortedTasks = self.taskSort.sortByDeadline()
        expected = [task2, task1]
        self.assertEqual(sortedTasks, expected)

    def test_addEditAndSortByPriority(self):
        task1 = Task("name 1", "description 1", "Low", "04-30-2024")
        task2 = Task("name 2", "description 2", "High", "05-04-2024")
        task3 = Task("name 3", "description 3", "Normal", "05-22-2024")

        self.todoList.addTask(task1)
        self.todoList.addTask(task2)
        self.todoList.addTask(task3)

        #switch priorities so the order should be [task1, task3, task2]
        self.taskEditor.editTask(task1, None, None, "High", None)
        self.taskEditor.editTask(task2, None, None, "Low", None)
        self.taskEditor.editTask(task3, None, None, "Normal", None)

        sortedTasks = self.taskSort.sortByPriority()
        expected = [task1, task3, task2]

        self.assertEqual(sortedTasks, expected)





if __name__ == "__main__":
    unittest.main()

