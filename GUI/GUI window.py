from tkinter import *

# widgets = GUI elements: buttons, textboxes, labels,images
# windows = serves a container to hold or contain these widgets

window = Tk() # instantiate a instance of a window
window.geometry("420x420")
window.title("Awesome Bruh")

icon = PhotoImage(file='coding.png')
window.iconphoto(True, icon)
window.config(background='black')

window.mainloop() # place window on computer screen , listen to events
