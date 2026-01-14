import json
import os
import sys
Task_File="tasks.json"
def load_tasks():
    if not os.path.exists(Task_File):
        return []
    with open(Task_File,"r") as file:
        return json.load(file)
def save_tasks(tasks):
    with open(Task_File,"w") as file:
        json.dump(tasks,file,indent=2)
def list_tasks():
    tasks=load_tasks()
    if not tasks:
        print("No task found")
        return 
    for task in tasks:
        status= "✅" if task["Done"] else "❌"
        print(f'{task["id"]} . [{status}] {task["Title"]}')

def add_task(title):
    task=load_tasks()
    new_id=task[-1]["id"]+ 1 if task else 1
    new_task={"id":new_id, "title": title,"done": False}
    task.append(new_task)
    save_tasks(task)
    print(f'Task added: {title}')
if __name__=='main':
    if len(sys.argv) < 2: 
        print("Usage:") 
        print(" python todo.py list") 
        print(" python todo.py add \"task title\"") 
        sys.exit(1)
    command=sys.argv[1]
    if command == "list":
        list_tasks()
    elif command == "add":
        if len(sys.argv) < 3:
            print("Error: Task title required.")
            sys.exit(1)
        add_task(sys.argv[2])
    else:
        print(f"Unknown command: {command}")

    
