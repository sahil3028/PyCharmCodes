import FreeSimpleGUI as sg

from zip_maker import zipCreate

label1=sg.Text("Select files to compress")
input1=sg.Input()
button1=sg.FilesBrowse("choose",key="file")

label2=sg.Text("Select destination folder")
input2=sg.Input()
button2=sg.FolderBrowse("choose",key="folder")

button3=sg.Button("compress!")

window=sg.Window("file compressor", layout=[[label1,input1,button1],[label2,input2,button2],[button3]])


while True:
    event, values= window.read()
    print(event,values)

    filePaths=values["file"].split(";")
    folder=values["folder"]

    zipCreate(filePaths,folder)


window.close()