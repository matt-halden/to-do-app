# building webapp with streamlit library
# will be hosted on my local host
# CLI command: streamlit run /Users/matthalden/Documents/Python/App1/web.py
# lines of code should not be more than 79 characters long
# so we can have two windows open side by side

# s20 complete button: use session state for checkbox widgets
# checkboxes need a key!

import streamlit as st
import functions

todos = functions.get_todos()

# st.session_state is some sort of dictionary
# st.session_state is like calling the key of the value pair
# ...because it is a dictionary
# so when user hits enter, we call this add_todo function via
# the callback function on_change within st.text_input
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    # print(todo) print for testing
    todos.append(todo)
    functions.write_todos(todos)


st.title("Matt's Todo App")
st.subheader("This is my todo app")
st.write("This is for simple text")

# the key for checkboxes is a boolean. Becomes true when
# user marks a checkbox
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:  # when this is true...
        #print(checkbox)
        todos.pop(index)  # remove todo that is checked
        functions.write_todos(todos)
        del st.session_state[todo]  # deletes pair from session state
        st.experimental_rerun()  # needed for checkboxes, deletes box immediately

# label is header for input text box
# on_change is a callback function
# key is the value that would be entered in the text box
st.text_input(label="Label", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')

#st.session_state  # show session state on our web page for testing