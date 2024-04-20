from Task import Task
from TaskEditor import TaskEditor
from TodoList import TodoList
import unittest

class testTaskEditor(unittest.TestCase):

    def setUp(self):
        self.newList = TodoList()
        self.newEditor = TaskEditor(self.newList)

    def test_editName(self):
        task = Task("Task 1", "Description 1")
        self.newList.addTask(task)
          
        new_name = "Updated Task Name"
        self.newEditor.editTask(task, newName=new_name)
        self.assertEqual(task.name, new_name)

    def test_editDescription(self):
        task = Task("Task 1", "Task Description")
        self.newList.addTask(task)

        new_description = "New Description"
        self.newEditor.editTask(task, newDescription=new_description)
        self.assertEqual(task.description, new_description)

    def test_editDeadline(self):
        task = Task("Task 1", "Description", deadline = "04-30-2024")
        self.newList.addTask(task)

        new_deadline = "05-12-2024"
        self.newEditor.editTask(task, newDeadline=new_deadline)
        self.assertEqual(task.deadline, new_deadline)



if __name__ == "__main__":
    unittest.main()