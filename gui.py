import functions
import PySimpleGUI as sg

'''importing a third party module for creating Graphical User Interface
    for mainly creating tables windows etc
'''

label = sg.Text("Type in a to-do")  # adds a text in GUI window
input_box = sg.InputText(tooltip="Enter todo", key="todo")  # adds an input area in GUI window
add_button = sg.Button("Add")  # adds a button in GUI window

window = sg.Window('My To-Do App',
                   layout=[[label], [input_box, add_button]],
                   font=('Helvetica', 20))
'''contains all the instances of all the objects in a list'''

while True:
    event, values = window.read()  # reads the window
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break

window.close()  # closes the window
