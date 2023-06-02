import functions
import PySimpleGUI as sg

'''importing a third party module for creating Graphical User Interface
    for mainly creating tables windows etc
'''

label = sg.Text("Type in a to-do")  # adds a text in GUI window
input_box = sg.InputText(tooltip="Enter todo")  # adds an input area in GUI window
add_button = sg.Button("Add")  # adds a button in GUI window

window = sg.Window('My To-Do App', layout=[[label], [input_box, add_button]])
'''contains all the instances of all the objects in a list'''

window.read()  # reads the window
window.close()  # closes the window
