from TodoList import TodoList
import unittest

class testTodoList(unittest.TestCase):

    def test_setUp(self):
        todo = TodoList()
        self.assertEqual(todo.tasks, [])


    def test_addTask(self):
        todo = TodoList()
        todo.addTask("Task 1")
        self.assertEqual(todo.tasks, ["Task 1"])

    def test_removeTask(self):
        todo = TodoList()
        todo.addTask("Task 2")
        todo.removeTask("Task 2")
        self.assertEqual(todo.tasks, [])

    def test_getAllTasks(self):
        todo = TodoList()
        todo.addTask("Task 1")
        todo.addTask("Task 2")
        allTasks = todo.getAllTasks()
        self.assertEqual(allTasks, ["Task 1", "Task 2"])



if __name__ == "__main__":
    unittest.main()