from tkinter import *

def doSomething(event):
    print(event)
    # print("Mouse coordinates: " + str(event.x)+","+str(event.y))

window = Tk()

# window.bind("<Button-1>", doSomething) # left mouse button click
# window.bind("<Button-2>", doSomething) # middle mouse button click
# window.bind("<Button-3>", doSomething) # right mouse button click
# window.bind("<ButtonRelease>", doSomething) # button release mouse button click
window.bind("<Enter>", doSomething) # when cursor enters a frame/window
window.bind("<Leave>", doSomething) # when cursor exit a frame/window
window.bind("<Motion>", doSomething) # gives coordinates of mouse movement

window.mainloop()