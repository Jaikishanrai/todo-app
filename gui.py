import functions
import PySimpleGUI as sg

'''importing a third party module for creating Graphical User Interface
    for mainly creating tables windows etc
'''

label = sg.Text("Type in a to-do")  # adds a text in GUI window
input_box = sg.InputText(tooltip="Enter todo", key="todo")  # adds an input area in GUI window
add_button = sg.Button("Add")  # adds a button in GUI window
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
window = sg.Window('My To-Do App',
                   layout=[[label], [input_box, add_button], [list_box, edit_button]],
                   font=('Helvetica', 20))
'''contains all the instances of all the objects in a list'''

while True:
    event, values = window.read()  # reads the window
    print(1, event)
    print(2, values)
    print(3, values['todos'])
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break

window.close()  # closes the window
