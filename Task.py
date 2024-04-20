class Task:
    def __init__(self, name, description, priority, deadline = None):
        self.name = name; 
        self.description = description
        self.priority = priority
        self.completed = False
        self.deadline = deadline

    def isCompleted(self):
        self.completed = True



    def __str__(self):
        return f"{self.name} - {self.description} (Deadline: {self.deadline}) [Completed: {self.completed}] [Priority: {self.priority}]"