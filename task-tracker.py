import json
import os
import datetime

tasks = []
print("--------------\nwelcome to task tracker io\nplease choose an action\n")

if os.path.exists("tasks.json"):
    with open("tasks.json", 'r') as file:
        tasks = json.load(file)
def start():
  print("--------------")
  print("1- Add task")
  print("2- remove task")
  print("3- list all tasks")
  print("4- update task")
  print("5- to quit")
  action = int(input("\nenter number of your desired action: "))
  return action

action = start()

def addTask():
    title = input("enter the title of your task: ")
    new_id = len(tasks) + 1 
    time = datetime.datetime.now()
    creationDate = f"{time.year}/{time.month}/{time.day}"
    new_task = {
        "title": title,
        "id": new_id,
        "dateCreated" : creationDate
    }
    tasks.append(new_task)
    with open("tasks.json", 'w') as file:
        json.dump(tasks, file, indent=4)
    print(f"New task added: {title} (ID: {new_id})")
    start()

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
    start()

def listTasks():
    if not tasks:
        print("No tasks found")
    else:
        print("\nCurrent Tasks:")
        for task in tasks:
            print(f"ID: {task['id']} - {task['title']}")
    start()
            
def updateTasks():
  task_id = int(input("Enter the ID of the task to update: "))
  for task in tasks:
    if task["id"] == task_id:
      newTitle = input("Enter the new title: ")
      task["title"] = newTitle
      with open("tasks.json", 'w') as file:
                json.dump(tasks, file, indent=4)
      print(f"Task {task_id} updated successfully")
      return
  print(f"Task with ID {task_id} not found")

match action:
    case 1:
        addTask()
    case 2:
        removeTask()
    case 3:
        listTasks()
    case 4:
        updateTasks()
    case 5:
        print("Bye!")
    case _:
        print("Invalid action")