import json
import os
import datetime

def load_tasks():
    """Load tasks from JSON file if it exists"""
    tasks = []
    if os.path.exists("tasks.json"):
        try:
            with open("tasks.json", 'r') as file:
                tasks = json.load(file)
        except (json.JSONDecodeError, IOError):
            print("Warning: Could not load tasks from file. Starting with empty task list.")
    return tasks

def save_tasks(tasks):
    """Save tasks to JSON file"""
    try:
        with open("tasks.json", 'w') as file:
            json.dump(tasks, file, indent=4)
    except IOError:
        print("Error: Could not save tasks to file.")
        
def get_next_id(tasks):
    if not tasks:
        return 1
    existing_ids = {task["id"] for task in tasks}
    next_id = 1
    while next_id in existing_ids:
        next_id += 1
    
    return next_id

def display_menu():
    """Display the menu and get user input"""
    print("\n--------------")
    print("1- Add task")
    print("2- Remove task")
    print("3- List all tasks")
    print("4- Update task")
    print("5- Quit")
    while True:
        try:
            action = int(input("\nEnter number of your desired action: "))
            if 1 <= action <= 5:
                return action
            print("Please enter a number between 1 and 5")
        except ValueError:
            print("Please enter a valid number")

def add_task(tasks):
    """Add a new task to the list with a unique ID"""
    title = input("Enter the title of your task: ").strip()
    if not title:
        print("Task title cannot be empty!")
        return
    
    new_id = get_next_id(tasks)
    creation_date = datetime.datetime.now().strftime("%Y/%m/%d")
    
    new_task = {
        "title": title,
        "id": new_id,
        "dateCreated": creation_date
    }
    
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"New task added: {title} (ID: {new_id})")


def remove_task(tasks):
    """Remove a task by ID"""
    if not tasks:
        print("No tasks available to remove")
        return
    
    list_tasks(tasks)
    try:
        task_id = int(input("Enter the ID of the task to remove: "))
    except ValueError:
        print("Invalid ID. Please enter a number.")
        return
    
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            save_tasks(tasks)
            print(f"Task {task_id} removed successfully")
            return
    
    print(f"Task with ID {task_id} not found")

def list_tasks(tasks):
  if not tasks:
    print("No tasks found")
  else:
    print("\nCurrent Tasks:")
    for task in tasks:
        print(f"ID: {task['id']} - {task['title']}")
def update_task(tasks):
    """Update a task's title"""
    if not tasks:
        print("No tasks available to update")
        return
    
    list_tasks(tasks)
    try:
        task_id = int(input("Enter the ID of the task to update: "))
    except ValueError:
        print("Invalid ID. Please enter a number.")
        return
    
    for task in tasks:
        if task["id"] == task_id:
            new_title = input("Enter the new title: ").strip()
            if not new_title:
                print("Task title cannot be empty!")
                return
                
            task["title"] = new_title
            save_tasks(tasks)
            print(f"Task {task_id} updated successfully")
            return
    
    print(f"Task with ID {task_id} not found")

def main():
    """Main program loop"""
    print("--------------\nWelcome to Task Tracker IO")
    tasks = load_tasks()
    
    while True:
        action = display_menu()
        
        if action == 1:
            add_task(tasks)
        elif action == 2:
            remove_task(tasks)
        elif action == 3:
            list_tasks(tasks)
        elif action == 4:
            update_task(tasks)
        elif action == 5:
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()