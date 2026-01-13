from unittest import case

tasks=[]
while True:
    inpu=input("enter add or show")
    match inpu:
        case "add":
            tasks.append(input("Enter task:"))
        case "show":
            print(tasks)