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

        # Check if any task exists
        if len(tasks) == 0:
            print("No tasks available. Please add a task first.")

        else:

            # Show all tasks
            print("\n===== Select a Task to Edit =====")

            count = 1

            for task in tasks:
                print(f"{count}. {task['title']}")
                count += 1

            # Take task number
            task_number = int(
                input("\nEnter the number of the task you want to edit: ")
            )

            # Validate task number
            if task_number < 1 or task_number > len(tasks):
                print("Invalid task number. Please try again.")

            else:

                # Get the selected task
                selected_task = tasks[task_number - 1]

                # Edit Menu
                print("\n===== Edit Menu =====")
                print("1. Edit Title")
                print("2. Edit Description")
                print("3. Edit Priority")
                print("4. Edit Due Date")
                print("5. Cancel")

                edit_choice = input("Enter your choice: ")

                # Edit Title
                if edit_choice == "1":

                    print("\n===== Edit Title =====")
                    print(f"Current Title : {selected_task['title']}")

                    new_title = input("Enter New Title: ")

                    selected_task["title"] = new_title

                    print("\n✅ Title updated successfully!")

                elif edit_choice == "2":
                    print("Edit Description feature coming soon...")

                elif edit_choice == "3":
                    print("Edit Priority feature coming soon...")

                elif edit_choice == "4":
                    print("Edit Due Date feature coming soon...")

                elif edit_choice == "5":
                    print("Edit cancelled.")

                else:
                    print("Invalid choice.")

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