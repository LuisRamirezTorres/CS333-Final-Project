class TaskEditor:
    

    def __init__(self, todoList):
        self.todoList = todoList

    def editTask(self, task, newName = None, newDescription = None, newDeadline = None):
        if newName is not None:
            task.name = newName
        if newDescription is not None:
            task.description = newDescription
        if newDeadline is not None:
            task.deadline = newDeadline

