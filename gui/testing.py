import FreeSimpleGUI as sg

label=sg.Text("Type in a to-do")
inputBox=sg.InputText(tooltip="write here")
button=sg.Button("click!")
window=sg.Window('my to-do app', layout=[[label],[inputBox,button]]) #every list inside layout act for a new row

window.read()
window.close()