"""
pydle.py

Starter code for a Wordle clone using the guizero Box and PushButton widgets.

The word list is Donald Knuth's public domain list of five-letter words.

Dan Stormont
CoderDojo Tucson
15 February 2022
"""
# Import the widgets we'll need from the guizero library.
from guizero import App, Text, Box, PushButton

# Create the App widget (the GUI window).
app = App(title='Pydle')

# Display a message in the window.
message = Text(app, text='Python Wordle Clone')

# Display the widget.
app.display()

"""
Utility method to load five letter words from the SGB text file and return them 
as a list of strings. This function came from the charlesreid1/five-letter-words 
repo on Github.
"""
def get_words():
    # Load the file.
    with open('sgb-words.txt','r') as f:
        ## This includes \n at the end of each line:
        #words = f.readlines()
    
        # This drops the \n at the end of each line:
        words = f.read().splitlines()

    return words
