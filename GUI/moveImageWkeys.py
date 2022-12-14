from tkinter import *

# --------------Window--------------------------------------
# def moveUp(event):
#     label.place(x=label.winfo_x(), y=label.winfo_y()-50)
#
# def moveLeft(event):
#     label.place(x=label.winfo_x()-50, y=label.winfo_y())
#
# def moveDown(event):
#     label.place(x=label.winfo_x(), y=label.winfo_y()+50)
#
# def moveRight(event):
#     label.place(x=label.winfo_x()+50, y=label.winfo_y())

# -------------Canvas----------------------------------------
def moveUp(event):
    canvas.move(canvasImage, 0,-10)

def moveLeft(event):
    canvas.move(canvasImage, -10,0)

def moveDown(event):
    canvas.move(canvasImage, 0,10)

def moveRight(event):
    canvas.move(canvasImage, 10,0)


window = Tk()
# window.geometry('500x500')
#
# window.bind('<w>', moveUp)
# window.bind('<a>', moveLeft)
# window.bind('<s>', moveDown)
# window.bind('<d>', moveRight)
# window.bind('<Up>', moveUp)
# window.bind('<Left>', moveLeft)
# window.bind('<Down>', moveDown)
# window.bind('<Right>', moveRight)
#
raceCar = PhotoImage(file='racing-car.png')
# label = Label(window, image=raceCar)
# label.place(x=0, y=0)
# ----------------------------------------------------------------
# Canves

window.bind('<w>', moveUp)
window.bind('<a>', moveLeft)
window.bind('<s>', moveDown)
window.bind('<d>', moveRight)
window.bind('<Up>', moveUp)
window.bind('<Left>', moveLeft)
window.bind('<Down>', moveDown)
window.bind('<Right>', moveRight)

canvas = Canvas(window,width=500, height=500)
canvas.pack()

canvasImage = canvas.create_image(0,0, image=raceCar, anchor=NW)



window.mainloop()
