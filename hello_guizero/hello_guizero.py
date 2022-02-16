"""
hello_guizero.py

A "hello world" program using the guizero library to create a simple graphical 
user interface.

Dan Stormont
CoderDojo Tucson
15 February 2022
"""

# Import the widgets we'll need from the guizero library.
from guizero import App, Text

# Create the App widget (the GUI window).
app = App(title='Hello guizero')

# Display a message in the window.
message = Text(app, text='My first guizero GUI!')

# Display the widget.
app.display()
