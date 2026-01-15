
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
        status= "✅" if task["done"] else "❌"
        print(f'{task["id"]} . [{status}] {task["title"]}')

def add_task(title):
    task=load_tasks()
    new_id=task[-1]["id"]+ 1 if task else 1
    new_task={"id":new_id, "title": title,"done": False}
    task.append(new_task)
    save_tasks(task)
    print(f'Task added: {title}')

def mark_done(task_id):
    tasks=load_tasks()
    for task in tasks:
        if task["id"]==task_id:
            task["done"]=True
            save_tasks(tasks)
            print(f'Task {task_id} marked as done.')
            return
    print(f'Task with id {task_id} not found.')
def delete_task(task_id):
    tasks=load_tasks()
    new_tasks=list()
    for task in tasks:
        if task["id"]!=task_id:
            new_tasks.append(task)
    if len(tasks)==len(new_tasks):
        print(f'Task with id {task_id} not found')
    save_tasks(new_tasks)
    print(f"Task {task_id} deleted.")
if __name__=='__main__':
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
    elif command == "done":
     if len(sys.argv) < 3:
        print("Error: Task ID required.")
        sys.exit(1)

     try:
        task_id = int(sys.argv[2])
     except ValueError:
        print("Error: Task ID must be a number.")
        sys.exit(1)

     mark_done(task_id)
    elif command=="delete":
        if len(sys.argv)<3:
            print("Task id required")
            sys.exit(1)
        try:
            task_id=int(sys.argv[2])
        except ValueError:
            print("Error : Task id must be integer")
            sys.exit(1)
        delete_task(task_id)

    else:
        print(f"Unknown command: {command}")
    
