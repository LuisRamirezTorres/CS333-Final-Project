class TaskFilter:
    
    def __init__(self, todoList):
        self.todoList = todoList
    
    def filterPriority(self, priority):
        return [task for task in self.todoList.tasks if task.priority == priority]
    
    def filterCompleted(self):
        return [task for task in self.todoList.tasks if task.completed == True]