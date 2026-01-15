import todo
while True:
    a=input("""What You wanna do
               ->ALL
               ->ADD
               ->DELETE
               ->UPDATE
               ->EXIT\n""")
    a=a.upper()
    if a=="ALL":
        todo.list_tasks()
    elif a=="ADD":
        b=input("Enter the task you want to add\n")
        todo.add_task(b)
    elif a=="DELETE":
        b=int(input("Enter the id of task you want to delete \n"))
        todo.delete_task(b)
    elif a=="UPDATE":
        b=int(input("Enter the id of task you want to update \n"))
        todo.mark_done(b)
    elif a=="EXIT":
        break
    else:
        print("Enter a valid command")
print("Fuck you ")