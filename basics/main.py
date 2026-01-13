# -------- Variables & List --------
#tasks = []   # list to store user tasks
running = True

# -------- Method / Function --------
def show_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("Your Tasks:")
       # for i in range(len(tasks)):   # for loop
        #    print(f"{i + 1}. {tasks[i]}")

        for index, item in enumerate(tasks):  #enumerate used in lists to get two values at once
            item=item.strip("\n")
            print(f"{index + 1}. {item}")


# reading the files into my variables

# file=open("data.txt",'r')
# tasks=file.readlines()
# file.close()

with open("data.txt",'r') as file:\
    tasks=file.readlines()



# -------- While Loop (App runs continuously) --------
while running:
    print("\n--- MENU ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Edit Task")
    print("5. Exit")

    choice = input("Enter your choice: ")   # user input

    # -------- Match-Case (Control Flow) --------
    match choice:
        case "1":
            task = input("Enter task name: ") + "\n"
            tasks.append(task)
            print("Task added successfully.")

        case "2":
            show_tasks()

        case "3":
            show_tasks()
            if tasks:
                index = int(input("Enter task number to remove: "))
                if 1 <= index <= len(tasks):
                    removed = tasks.pop(index - 1)
                    print(f"Removed task: {removed}")
                else:
                    print("Invalid task number.")

        case "4":
            show_tasks()
            index=int(input("Enter the number of task to edit"))
            tasks[index-1]=input("enter the modified task: ")
            print("done.")
        case "5":
            file = open("data.txt", 'w')
            file.writelines(tasks)
            file.close()
            print("Exiting app. Goodbye!")
            running = False

        case _:
            print("Invalid choice. Try again.")