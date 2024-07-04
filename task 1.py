class ToDoList:
    def __init__(self):
        self.tasks = []
    #to add items in the  to do list
    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added to the list.")
     #function for poping or removing items
    def remove_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)# -1 for the maximum length size
            print(f"Task '{removed_task}' removed from the list.")
        else:
            print("Invalid task number.")
       # function for displaying the items
    def display_tasks(self):
        if not self.tasks:
            print("No tasks found!")
        else:
            print("To-Do List:")
            for idx, task in enumerate(self.tasks, start=1):
                print(f"{idx}. {task}")

def main():
    todo_list = ToDoList()
    while True:
        print("\nTo-Do List Options:")
        print("1. Add task")
        print("2. Remove task")
        print("3. Display task")
        print("4. Exit")
        choice = input("Enter your choice: ")
    # calling the function with help to switch case
        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            task_number = int(input("Enter the task number to remove: "))
            todo_list.remove_task(task_number)
        elif choice == '3':
            todo_list.display_tasks()
        elif choice == '4':
            print("Exiting the To-Do List program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
