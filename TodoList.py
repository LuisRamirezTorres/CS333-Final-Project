class TodoList:

    def __init__(self):
        self.tasks = []


    def addTask(self, task):
        self.tasks.append(task)

    def removeTask(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
        else:
            print("That task does not exist is in the Todo List!\n")

    def getAllTasks(self):
        return self.tasks