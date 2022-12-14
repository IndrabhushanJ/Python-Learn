from tkinter import *
import time

WIDTH = 500
HEIGHT = 500
xVelocity = 3
yVelocity = 2


window = Tk()

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

spaceImage = PhotoImage(file='spacemoon.png')
spaceCanvas = canvas.create_image(0, 0, image=spaceImage, anchor=NW)

ufoImage = PhotoImage(file='ufo3.png')
ufoCanvas = canvas.create_image(0, 0, image=ufoImage, anchor=NW)

image_width = ufoImage.width()
image_height = ufoImage.height()

while True:
    coordinates = canvas.coords(ufoCanvas)
    print(coordinates)
    if coordinates[0] >= WIDTH-image_width or coordinates[0]<0:
        xVelocity = -xVelocity
    if coordinates[1] >= HEIGHT-image_height or coordinates[1]<0:
        yVelocity = -yVelocity
    canvas.move(ufoCanvas, xVelocity,yVelocity)
    window.update()
    time.sleep(0.01)

window.mainloop()
