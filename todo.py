import json
import os
Task_File="tasks.json"
def read_tasks():
    if not os.path.exists(Task_File):
        return []
    with open(Task_File,"r") as file:
        return json.load(file)
def list_tasks():
    tasks=read_tasks()
    if not tasks:
        print("No task found")
        return 
    for task in tasks:
        status= "✅" if task["Done"] else "❌"
        print(f'{task["id"]} . [{status}] {task["Title"]}')
if __name__=='main':
    list_tasks()
