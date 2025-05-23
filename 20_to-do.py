#To-Do App with File Persistence 
#Add, remove, mark tasks complete, and save/load from a file. 

def load_tasks():
    try:
        with open("todo.txt", "r") as file:
            return [line.strip() for line in file]
    except:
        return []

def save_tasks(tasks):
    with open("todo.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")
 
tasks = load_tasks()
 
while True:
    print("\nTo-Do List")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Mark Task Complete")
    print("4. Show Tasks")
    print("5. Exit")
 
    choice = input("Enter your choice: ")
 
    if choice == "1":
        task = input("Enter new task: ")
        tasks.append("[ ] " + task)
        save_tasks(tasks)
        print("Task added.")
 
    elif choice == "2":
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")
        num = int(input("Enter task number to remove: "))
        if 1 <= num <= len(tasks):
            tasks.pop(num - 1)
            save_tasks(tasks)
            print("Task removed.")

        else:

            print("Invalid number.")
 
    elif choice == "3":
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")
        num = int(input("Enter task number to mark complete: "))
        if 1 <= num <= len(tasks):
            if "[ ]" in tasks[num - 1]:
                tasks[num - 1] = tasks[num - 1].replace("[ ]", "[x]")
                save_tasks(tasks)
                print("Task marked complete.")
            else:
                print("Task already complete.")
        else:
            print("Invalid number.")
    elif choice == "4":
        print("\nYour Tasks:")
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")

 