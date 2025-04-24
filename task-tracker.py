import json
import os

tasks = []

if os.path.exists("tasks.json"):
    with open("tasks.json", 'r') as file:
        tasks = json.load(file)

print("--------------\nwelcome to task tracker io\nplease choose an action\n")
print("1- Add task")
print("2- remove task")
print("3- list all tasks")
action = int(input("\nenter number of your desired action: "))

def addTask():
    title = input("enter the title of your task: ")
    new_id = len(tasks) + 1  # Generate new ID based on current task count
    new_task = {
        "title": title,
        "id": new_id
    }
    tasks.append(new_task)
    with open("tasks.json", 'w') as file:
        json.dump(tasks, file, indent=4)
    print(f"New task added: {title} (ID: {new_id})")

def removeTask():
    task_id = int(input("Enter the ID of the task to remove: "))
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            with open("tasks.json", 'w') as file:
                json.dump(tasks, file, indent=4)
            print(f"Task {task_id} removed successfully")
            return
    print(f"Task with ID {task_id} not found")

def listTasks():
    if not tasks:
        print("No tasks found")
    else:
        print("\nCurrent Tasks:")
        for task in tasks:
            print(f"ID: {task['id']} - {task['title']}")

match action:
    case 1:
        addTask()
    case 2:
        removeTask()
    case 3:
        listTasks()
    case _:
        print("Invalid action")