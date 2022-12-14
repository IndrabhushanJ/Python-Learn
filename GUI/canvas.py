# canvas = widget that is used to draw graphs, plot, images in a window

from tkinter import *

window = Tk()

canvas = Canvas(window, height=500, width=500)
# canvas.create_line(0, 0, 500, 500, fill='blue', width=5)
# canvas.create_line(0, 500, 500, 0, fill='red', width=5)
# canvas.create_rectangle(125, 125, 375, 375, outline='red', width=3, fill='light green')
# canvas.create_line(0, 250, 500, 250)
# canvas.create_polygon(125, 375, 250, 125, 375, 375, fill='green')  # triangle
# canvas.create_arc(0, 0, 500, 500, fill='pink',start= 90,extent=360)
canvas.create_arc(0,0,500,500,fill='red', extent=180, width=10)
canvas.create_arc(0,0,500,500,start=180, extent=180, width=10)
canvas.create_oval(190,190,310,310,fill='white',width=10)
canvas.create_oval(220,220,280,280,fill='light grey',width=5)
canvas.pack(padx=10,pady=10)

window.mainloop()
