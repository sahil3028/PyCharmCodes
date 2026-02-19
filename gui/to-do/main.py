import FreeSimpleGUI as sg
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt",'w'):
        pass

# ---------- helper functions ----------
def load_todos():
    try:
        with open("todos.txt", "r") as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        return []

def save_todo(todos):
    [todos.pop(i) for i in sorted(finished_tasks, reverse=True)]
    with open("todos.txt", "w",encoding="utf-8") as f:
            f.write('\n'.join(todos))

# ---------- GUI ----------
sg.theme("DarkBlue3")

label = sg.Text("Enter your task:")

inputTask = sg.Input(key="TASK")

event_l=sg.Text(key="event")

add_b = sg.Button("Add")

edit_b=sg.Button("Edit")

complete_b=sg.Button("Complete")

delete_b=sg.Button("Delete")

listbox = sg.Listbox(
    values=load_todos(),
    enable_events=True,
    size=(40, 10),
    key="LIST"
)

layout = [
    [label],
    [inputTask, add_b],
    [listbox,edit_b,complete_b],
    [event_l, delete_b]
]

window = sg.Window("To-Do App", layout)

# ---------- event loop ----------
todos = load_todos()
finished_tasks=[]
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case sg.WIN_CLOSED:
            save_todo(todos)
            break

        case "Add":
            task = values["TASK"].strip()
            if task:
                todos.append(task)
                window["LIST"].update(todos)
                window["TASK"].update("")
                window["event"].update(value="The task is added")

        case "Edit":
            if values["LIST"]:
                #todos[todos.index(values["LIST"][0])]=values["TASK"].strip()
                selected_index = listbox.get_indexes()[0]
                todos[selected_index] = values["TASK"].strip()

                window["LIST"].update(todos)
                window["TASK"].update("")
                window["event"].update(value="The task is edited")

        case "LIST":
            window["TASK"].update(values["LIST"][0])
        case "Complete":
             selected_index=listbox.get_indexes()[0]
             todos[selected_index] = "✔ " + todos[selected_index]
             finished_tasks.append(selected_index)
             window["LIST"].update(todos)
             window["TASK"].update("")
             window["event"].update(value="The task is completed")
        case "Delete":
            selected_index = listbox.get_indexes()[0]
            todos.pop(selected_index)
            window["LIST"].update(todos)
            window["TASK"].update("")
            window["event"].update(value="The task is Deleted")

window.close()