from TodoList import TodoList
from Task import Task
from TaskEditor import TaskEditor
from TaskFilter import TaskFilter
from TaskSort import TaskSort



def main():
    todo = TodoList()
    editor = TaskEditor(todo)
    filter = TaskFilter(todo)
    sorter = TaskSort(todo)


    while True:
        print("\nWelcome to the Todo List Menu\n")
        print("Choose one of our menu options!\n\n")

        print("1. Add Task\n")
        print("2. Edit Task\n")
        print("3. Remove Task\n")
        print("4. List Tasks\n")
        print("5. Sort Tasks\n")
        print("6. Filter Tasks\n")
        print("7. Show All Tasks\n")
        print("8. Mark Task As Completed\n")
        print("9. Exit\n")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            name = input("Enter task name: ")
            description = input("Enter task description: ")
            priority = input("Enter task priority (High, Normal, Low): ")
            deadline = input("Enter a deadline (optional): ")
            task = Task(name, description, priority, deadline)
            todo.addTask(task)
            print("\nTask added successfully!\n\n")
        
        elif choice == "2":
            taskInd = int(input("Enter the index of the task you would like to edit: "))
            if taskInd < 1 or taskInd > len(todo.tasks):
                print("Invalid task index!\n")
                continue
            task = todo.tasks[taskInd - 1]
            newName = input("Enter new task name (Press ENTER to skip): ")
            newDescription = input("Enter new task description (Press ENTER to skip): ")
            newPriority = input("Enter new task priority (Press ENTER to skip): ")
            newDeadline = input("Enter new deadline (Press ENTER to skip): ")
            editor.editTask(task, newName, newDescription, newPriority, newDeadline)
            print("Task edited successfully!\n\n")

        elif choice == "3":
            taskInd = int(input("Enter the index of the task you would like to remove: "))
            if taskInd < 1 or taskInd > len(todo.tasks):
                print("Invalid task index!\n")
                continue
            task = todo.tasks.pop(taskInd - 1)
            print("Task removed successfully")

        elif choice == "4":
            print("\nTasks:")
            for i, task in enumerate(todo.tasks, start = 1):
                print(f"{i}. {task}")

        elif choice == "5":
            print("\nSort Options:\n")
            print("1. By Deadline\n")
            print("2. By Priority\n")
            sortChoice = input("Enter your sort choice: ")
            if sortChoice == "1":
                sortedTasks = sorter.sortByDeadline()
            elif sortChoice == "2":
                sortedTasks = sorter.sortByPriority()
            else:
                print("Invalid sort choice!\n")
            for i, task in enumerate(sortedTasks, start = 1):
                print(f"{i}, {task}")

        elif choice == "6":
            print("\nFilter Options:\n")
            print("1. By Completed Status\n")
            print("2. By Priority\n")

            filterChoice = input("Enter your filter option: ")
            if filterChoice == "1":
                filteredTasks = filter.filterCompleted()
            elif filterChoice == "2":
                taskPriority = input("Enter priority level (High, Normal, Low): ")
                filteredTasks = filter.filterPriority()
            else:
                print("Invalid filter choice!\n")
                continue
            print("\nFiltered Tasks:")
            for i, task in enumerate(filteredTasks, start = 1):
                print(f"{i}. {task}")

        elif choice == "7":
            print("\nAll Tasks: ")
            for i, task in enumerate(todo.tasks, start = 1):
                print(f"{i}. {task}")
        
        elif choice == "8":
            taskInd = int(input("Enter the index of the task to mark as completed: "))
            if taskInd < 1 or taskInd > len(todo.tasks):
                print("Invalid task index!\n")
                continue
            task = todo.tasks[taskInd - 1]
            task.isCompleted()
            print("Task marked as completed!\n")
        
        elif choice == "9":
            print("\nExiting...\n")
            break

        else: 
            print("Invalid choice! Try again!\n")
            



if __name__ == "__main__":
    main()

