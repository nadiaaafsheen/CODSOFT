import os
def display_menu():
    print("\n======TO DO LIST======")
    print("1. ADD TASK")
    print("2. LIST TASKS")
    print("3. MARK TASK AS DONE")
    print("4. EXIT")

def add_task():
    task = input("\n ENTER A NEW TASK: ")
    with open("todo.txt","a") as file:
        file.write(task + "\n")
    print("task successfully added!!")

def list_tasks():
    print("\n======TO DO LIST======")
    if not os.path.exists("todo.txt") or os.stat("todo.txt").st_size == 0:
        print(" NO TASKS ARE ADDED YET.")
    else:
        with open("todo.txt", "r") as file:
            tasks = file.readlines()
            for idx in range(len(tasks)):
                task = tasks[idx]
                print(f"{idx + 1}. {task}")


def mark_task_done():
    list_tasks()
    try:
        task_number = int(input("\n ENTER TASK NUMBER TO MARK AS DONE: "))
        with open("todo.txt", "r") as file:
            tasks = file.readlines()
        if 1<= task_number <= len(tasks):
            tasks.pop(task_number -1)
            with open("todo.txt", "w") as file:
                file.writelines(tasks)
            print("TASK IS DONE YAY!!!")
        else:
            print("invalid task number.")
    except ValueError:
        print("invalid input. please eneter a number.")

if __name__== "__main__":
    while True:
        display_menu()
        choice= input("ENTER YOUR CHOICE (1-4): ")

        if choice =="1":
            add_task()
        elif choice =="2":
            list_tasks()
        elif choice =="3":
            mark_task_done()
        elif choice =="4":
            print("EXITINF THE TO DO LIST")
            break
        else:
            print("INVALID CHOICE")












    










