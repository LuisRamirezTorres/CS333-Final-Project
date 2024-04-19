from Task import Task
import unittest

class testTask(unittest.TestCase):


    def test_setUp(self):
        newTask = Task("Dishes", "do the dishes", False, "March 1, 2024")
        expected = "Dishes - do the dishes (Deadline: March 1, 2024) [Completed: False]"
        self.assertEqual(str(newTask), expected)


    def test_isCompleted(self):
        newTask = Task("Dishes", "do the dishes", False, "March 5, 2024")
        newTask.isCompleted()
        expected = "Dishes - do the dishes (Deadline: March 5, 2024) [Completed: True]"
        self.assertEqual(str(newTask), expected)


if __name__ == "__main__":
    unittest.main()