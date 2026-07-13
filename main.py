# -----------------------------
# TaskFlow - Version 1.2
# -----------------------------

# Store all tasks (Application starts with an empty task list)
tasks = []

# Shows the application is running
running = True

while running:

    # -----------------------------
    # Menu
    # -----------------------------
    print("\n=========================")
    print("        TASKFLOW         ")
    print("=========================")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Edit Task")
    print("4. Mark Task as Completed")
    print("5. Exit")

    # Select an option from the menu
    menu_choice = input("Enter your choice (1-5): ")

    # -----------------------------
    # Add Task
    # -----------------------------
    if menu_choice == "1":

        continue_choice = "yes"

        while continue_choice == "yes":

            # Take input from the user
            title = input("Enter Task Title: ")
            description = input("Enter Task Description: ")
            priority = input("Enter Task Priority: ")
            due_date = input("Enter Task Due Date: ")

            # Create a task (Dictionary)
            task = {
                "title": title,
                "description": description,
                "priority": priority,
                "due_date": due_date,
                "completed": False
            }

            # Add the task to the tasks list
            tasks.append(task)

            continue_choice = input(
                "Do you want to add another task? (yes/no): "
            ).lower()

    # -----------------------------
    # View Tasks
    # -----------------------------
    elif menu_choice == "2":
        if len(tasks) == 0:
            print("No tasks available. Please add a task first.")
            continue
        else:
            # Display all tasks
            print("\n===== Task List =====")

            for task in tasks:
                print(f"Title       : {task['title']}")
                print(f"Description : {task['description']}")
                print(f"Priority    : {task['priority']}")
                print(f"Due Date    : {task['due_date']}")
                print(f"Completed   : {task['completed']}")
                print("-" * 30)

    # -----------------------------
    # Edit Task
    # -----------------------------
    elif menu_choice == "3":
        print("Feature Coming Soon...")

    # -----------------------------
    # Mark Task as Completed
    # -----------------------------
    elif menu_choice == "4":
        print("Feature Coming Soon...")

    # -----------------------------
    # Exit
    # -----------------------------
    elif menu_choice == "5":
        print("Thank you for using TaskFlow ❤️")
        running = False

    # -----------------------------
    # Invalid Choice
    # -----------------------------
    else:
        print("Invalid choice! Please enter a number between 1 and 5.")