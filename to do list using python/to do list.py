111
class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added successfully.")
    
    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"Task '{task}' removed successfully.")
        else:
            print(f"Task '{task}' not found.")

    def view_tasks(self):
        if self.tasks:
            print("Your To-Do List:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")
        else:
            print("Your To-Do List is empty.")

    def mark_completed(self, task):
        if task in self.tasks:
            print(f"Task '{task}' marked as completed.")
        else:
            print(f"Task '{task}' not found in the list.")

def main():
    todo_list = ToDoList()

    while True:
        print("\nChoose an option:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Mark Task as Completed")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task to add: ")
            todo_list.add_task(task)
        
        elif choice == '2':
            task = input("Enter the task to remove: ")
            todo_list.remove_task(task)
        
        elif choice == '3':
            todo_list.view_tasks()
        
        elif choice == '4':
            task = input("Enter the task to mark as completed: ")
            todo_list.mark_completed(task)
        
        elif choice == '5':
            print("Exiting the app.")
            break
        
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()


