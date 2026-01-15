import FreeSimpleGUI as sg

label1=sg.Text("Select files to compress")
input1=sg.Input()
button1=sg.FilesBrowse("choose")

label2=sg.Text("Select files to compress")
input2=sg.Input()
button2=sg.FolderBrowse("choose")

button3=sg.Button("compress!")

window=sg.Window("file compressor", layout=[[label1,input1,button1],[label2,input2,button2],[button3]])
window.read()
window.close()