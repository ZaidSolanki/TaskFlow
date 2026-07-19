import json

# -----------------------------
# TaskFlow - Version 1.2
# -----------------------------

#function to print menu
def show_menu():
    print("\n=========================")
    print("        TASKFLOW         ")
    print("=========================")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Edit Task")
    print("4. Mark Task as Completed")
    print("5. Delete Task")
    print("6. Exit")

#function to add a task
def add_task(tasks):
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
        save_tasks(tasks)

        continue_choice = input(
            "Do you want to add another task? (yes/no): "
        ).lower()

#function to view tasks
def view_tasks(tasks):
    if len(tasks) == 0:
        print("No tasks available. Please add a task first.")
        return

    print("\n===== Task List =====")

    for task in tasks:
        print(f"Title       : {task['title']}")
        print(f"Description : {task['description']}")
        print(f"Priority    : {task['priority']}")
        print(f"Due Date    : {task['due_date']}")
        print(f"Completed   : {task['completed']}")
        print("-" * 30)

#function to edit a task
def edit_task(tasks):
    selected_task = select_task(tasks)

    if selected_task is not None:

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
            save_tasks(tasks)

            print("\n✅ Title updated successfully!")

        elif edit_choice == "2":
            print("\n===== Edit Description =====")
            print(f"Current Description : {selected_task['description']}")

            new_description = input("Enter New Description: ")

            selected_task["description"] = new_description
            save_tasks(tasks)
            
            print("\n✅ Description updated successfully!")

        elif edit_choice == "3":
            print("\n===== Edit Priority =====")
            print(f"Current Priority : {selected_task['priority']}")

            new_priority = input("Enter New Priority: ")

            selected_task["priority"] = new_priority
            save_tasks(tasks)

            print("\n✅ Priority updated successfully!")

        elif edit_choice == "4":
            print("\n===== Edit Due Date =====")
            print(f"Current Due Date : {selected_task['due_date']}")

            new_due_date = input("Enter New Due Date: ")

            selected_task["due_date"] = new_due_date
            save_tasks(tasks)

            print("\n✅ Due Date updated successfully!")

        elif edit_choice == "5":
            print("Edit cancelled.")

        else:
            print("Invalid choice.")

#function to mark a task as completed
def mark_task_completed(tasks):
    selected_task = select_task(tasks)

    if selected_task is not None:
        selected_task["completed"] = True
        save_tasks(tasks)
        
        print(f"\n✅ Task '{selected_task['title']}' marked as completed!")

#function to delete a task
def delete_task(tasks):
    selected_task = select_task(tasks)

    if selected_task is not None:
        tasks.remove(selected_task)
        save_tasks(tasks)
        print(f"\n✅ Task '{selected_task['title']}' deleted successfully!")

#Function to select a task
def select_task(tasks):
    # Check if any task exists
    if len(tasks) == 0:
        print("No tasks available. Please add a task first.")
        return None

    # Show all tasks
    print("\n===== Select a Task =====")

    count = 1

    for task in tasks:
        print(f"{count}. {task['title']}")
        count += 1

    # Take task number
    task_number = int(
        input("\nEnter the number of the task you want to select: ")
    )

    # Validate task number
    if task_number < 1 or task_number > len(tasks):
        print("Invalid task number. Please try again.")
        return None

    # Get the selected task
    selected_task = tasks[task_number - 1]
    return selected_task

#save tasks to a JSON file
def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

#function to load tasks from a JSON file
def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
            return tasks
    except FileNotFoundError:
        return []

# Store all tasks (Application starts with an empty task list)
tasks = load_tasks()

# Shows the application is running
running = True

while running:

    # -----------------------------
    # Menu
    # -----------------------------
    show_menu()

    # Select an option from the menu
    menu_choice = input("Enter your choice (1-6): ")

    # -----------------------------
    # Add Task
    # -----------------------------
    if menu_choice == "1":
        add_task(tasks)

    # -----------------------------
    # View Tasks
    # -----------------------------
    elif menu_choice == "2":
        view_tasks(tasks)

    # -----------------------------
    # Edit Task
    # -----------------------------
    elif menu_choice == "3":
        edit_task(tasks)   

    # -----------------------------
    # Mark Task as Completed
    # -----------------------------
    elif menu_choice == "4":
        mark_task_completed(tasks)

    # -----------------------------
    # Delete Task
    # -----------------------------
    elif menu_choice == "5":
        delete_task(tasks)

    # -----------------------------
    # Exit
    # -----------------------------
    elif menu_choice == "6":
        print("Thank you for using TaskFlow ❤️")
        running = False

    # -----------------------------
    # Invalid Choice
    # -----------------------------
    else:
        print("Invalid choice! Please enter a number between 1 and 6.")