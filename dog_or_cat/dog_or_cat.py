"""
dog_or_cat.py

Using the guizero library to create buttons and display images.

Dan Stormont
CoderDojo Tucson
15 February 2022
"""
# Import the widgets we'll need from the guizero library.
from guizero import App, Text, PushButton, Picture

# Create the App widget (the GUI window).
app = App(title='Dog or Cat')

# Display a message in the window.
message = Text(app, text='Dog or Cat?')
message.text_size = 50

# Create buttons.
cat_button = PushButton(app, choose_picture('cat'), text='Cat')
dog_button = PushButton(app, choose_picture('dog'), text='Dog')

# Function to choose a picture.
picture = Drawing(app, width='fill', height='fill')

def choose_picture(animal):
    if animal == 'cat':
        picture.image(0, 0, 'images/cat.jpg')
    else:
        picture.image(0, 0, 'images/dog.jpg')

# Display the widget.
app.display()
