from tkinter import *
import time
from ball import *

window = Tk()

HEIGHT = 500
WIDTH = 500

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

vollyBall = Ball(canvas, 0, 0, 100, 1, 2, 'white')
tennisBall = Ball(canvas, 0, 0, 50, 4, 3, 'red')
basketBall = Ball(canvas, 0, 0, 120, 10, 4, 'yellow')

while True:
    vollyBall.move()
    tennisBall.move()
    basketBall.move()
    window.update()
    time.sleep(0.01)

window.mainloop()
