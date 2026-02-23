import streamlit as st
from PIL import Image, ImageOps
from playsound3 import playsound
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "todos.txt")
MUSIC_PATH = os.path.join(BASE_DIR, "fah.mp3")


if not os.path.exists(FILE_PATH):
    with open(FILE_PATH,'w'):
        pass



def load_todos():
    try:
        with open(FILE_PATH, "r") as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        return ["nothing"]

todos = load_todos()


def save_todo():
    #[todos.pop(i) for i in sorted(finished_tasks, reverse=True)]
    with open(FILE_PATH, "w",encoding="utf-8") as f:
            f.write('\n'.join(todos))

def add_task():
    todos.append(st.session_state["new"])
    save_todo()


st.title("My to-do app")
st.subheader("This is my to-do app")
st.write("this will help manage your tasks")

for index,todo in enumerate(todos):
    checkbox=st.checkbox(todo,key=index)
    if checkbox:
        todos.pop(index)
        del st.session_state[index]
        save_todo()
        st.rerun()

st.session_state["new"]=""
st.text_input(label="  ",placeholder="add a new Task....",on_change=add_task,key="new")


with st.expander("click your happy picture"):
    camera=st.camera_input("Camera")


print(camera)

if camera:
    img=Image.open(camera)

    gray_img=img.convert("L")
    colorized = ImageOps.colorize(gray_img, black="blue", white="yellow")

    st.image(gray_img)
    playsound("fah.mp3")