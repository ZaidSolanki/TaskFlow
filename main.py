# TaskFlow - Version 1

# Store all tasks
tasks = []

choice = "yes"


while (choice =="yes"):
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
    choice = input("Do you want to add another task? (yes/no): ")



# Display all tasks
print("\nTask List")

for task in tasks:
    print(f"Title       : {task['title']}")
    print(f"Description : {task['description']}")
    print(f"Priority    : {task['priority']}")
    print(f"Due Date    : {task['due_date']}")
    print(f"Completed   : {task['completed']}")
    print("-" * 30)