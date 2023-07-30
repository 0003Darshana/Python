def show_menu():
    """Display the menu options."""
    print("\n===== To-Do List =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

def add_task(tasks):
    """Add a new task to the list."""
    task = input("Enter the task: ")
    tasks.append(task)
    print("Task added successfully!")

def view_tasks(tasks):
    """View all the tasks in the list."""
    if not tasks:
        print("No tasks in the list.")
    else:
        print("\n===== Tasks =====")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def delete_task(tasks):
    """Delete a task from the list."""
    view_tasks(tasks)
    if tasks:
        try:
            index = int(input("Enter the task number to delete: ")) - 1
            if 0 <= index < len(tasks):
                deleted_task = tasks.pop(index)
                print(f"Task '{deleted_task}' deleted successfully!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    tasks = []
    while True:
        show_menu()
        choice = input("Enter your choice (1/2/3/4): ")
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            delete_task(tasks)
        elif choice == '4':
            print("Thanks for using the To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
