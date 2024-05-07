class TaskSort:
    
    def __init__(self, todoList):
        self.todoList = todoList

    def sortByDeadline(self):
        return sorted(self.todoList.tasks, key=lambda task: task.deadline)
    
    def sortByPriority(self):
        priorityLevel = {"High": 3, "Normal": 2, "Low": 1}
        sortedTasks = sorted(self.todoList.tasks, key=lambda task: priorityLevel.get(task.priority, 0), reverse=True)
        return sortedTasks