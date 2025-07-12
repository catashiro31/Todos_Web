import functions
import streamlit as st

def add_todo():
    new_todo = st.session_state["add"] + '\n'
    st.session_state["add"] = ""
    todos.append(new_todo)
    functions.write_todo(todos)
todos = functions.get_todos()
st.title("My Todo App")
st.subheader("List Todo:")
for index,todo in enumerate(todos):
    check = st.checkbox(todo,key=todo)
    print(st.session_state)
    if check:
        todos.pop(index)
        functions.write_todo(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="",placeholder="Add new todo ...",
              key="add",on_change=add_todo)