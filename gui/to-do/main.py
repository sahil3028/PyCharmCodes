import FreeSimpleGUI as sg

label=sg.Text("Enter your Tasks")
inputTask=sg.Input()
button=sg.Button("add")

window=sg.Window("To-Do App",layout=[[label],[inputTask,button]])

while(True):
    out=window.read()
    print(out)
    inputTask=""

window.close()