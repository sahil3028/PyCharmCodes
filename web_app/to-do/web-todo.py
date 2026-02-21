import streamlit as st
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "todos.txt")

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

for todo in todos:
    st.checkbox(todo,key=todo+"x")

st.text_input(label="",placeholder="add a new Task....",on_change=add_task,key="new")

st.session_state
print("iss2")