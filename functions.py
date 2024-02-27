def get_todos(filepath="todos.txt"):
    """ Here is how we would write about what our
    function does for future reference.
    Read a text fi.le and return a list of to-do items.
    """
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos

def write_todos(todos_arg, filepath='todos.txt'):  # put default arg AFTER regular ones
    """ Write the to-do items list in the text file. """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)