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
    print("6. Search Tasks")
    print("7. Filter Tasks")
    print("8. Exit")

# function to add a task
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

        # Ask until user enters yes or no
        while True:
            continue_choice = input(
                "Do you want to add another task? (yes/no): "
            ).lower()

            if continue_choice == "yes" or continue_choice == "no":
                break

            print("❌ Invalid input. Please enter yes or no.")

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

#function to show filter menu
def show_filter_menu():
    print("\n===== Filter Tasks =====")
    print("1. Completed Tasks")
    print("2. Pending Tasks")
    print("3. High Priority Tasks")
    print("4. Medium Priority Tasks")
    print("5. Low Priority Tasks")
    print("6. Back")

#function to filter tasks
def filter_tasks(tasks, choice):
    filtered_tasks = []

    for task in tasks:

        if choice == "1" and task["completed"] == True:
            filtered_tasks.append(task)

        elif choice == "2" and task["completed"] == False:
            filtered_tasks.append(task)

        elif choice == "3" and task["priority"].lower() == "high":
            filtered_tasks.append(task)

        elif choice == "4" and task["priority"].lower() == "medium":
            filtered_tasks.append(task)

        elif choice == "5" and task["priority"].lower() == "low":
            filtered_tasks.append(task)

    return filtered_tasks

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
    try:
        task_number = int(
            input("\nEnter the number of the task you want to select: ")
        )
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return None

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
    
#function to search tasks by title
def search_tasks(tasks):
    search_word = input("Search tasks: ").lower()
    matching_tasks = []
    for task in tasks:
        if search_word in task["title"].lower():
            matching_tasks.append(task)
    return matching_tasks

#function to view search results
def view_search_results(matching_tasks):
    if len(matching_tasks) == 0:
        print("No matching tasks found.")
        return

    print("\n===== Search Results =====")

    for task in matching_tasks:
        print(f"Title       : {task['title']}")
        print(f"Description : {task['description']}")
        print(f"Priority    : {task['priority']}")
        print(f"Due Date    : {task['due_date']}")
        print(f"Completed   : {task['completed']}")
        print("-" * 30)

# Store all tasks (Application starts with an empty task list)
tasks = load_tasks()

# Shows the application is running
running = True

while running:

    # -----------------------------
    # Menu
    # -----------------------------
    show_menu()
    
    while True:
        menu_choice = input("Enter your choice (1-8): ")

        if menu_choice in ("1", "2", "3", "4", "5", "6", "7", "8"):
            break

        print("❌ Invalid choice! Please enter 1-8.")

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
    # Search Tasks
    # -----------------------------
    elif menu_choice == "6":
        matching_tasks = search_tasks(tasks)
        view_search_results(matching_tasks)
    # -----------------------------
    # Filter Tasks  
    # -----------------------------
    elif menu_choice == "7":
        while True:
            show_filter_menu()
            filter_choice = input("Enter your choice (1-6): ")
    
            if filter_choice in ("1", "2", "3", "4", "5"):
                filtered_tasks = filter_tasks(tasks, filter_choice)
                view_tasks(filtered_tasks)
                break
    
            elif filter_choice == "6":
                break
    
            else:
                print("❌ Invalid choice! Please enter 1-6.")
    # Exit
    # -----------------------------
    elif menu_choice == "8":
        print("Thank you for using TaskFlow ❤️")
        running = False