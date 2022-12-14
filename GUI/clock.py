from tkinter import *
from time import *


def update():
    time_string = strftime('%I:%M:%S %p')
    time_label.config(text=time_string)

    date_string = strftime('%A,\n %d %B %Y')
    date_label.config(text=date_string)

    time_label.after(1000, update)


window = Tk()

time_label = Label(window, font=('Arial', 50), fg='#00ff00', bg='black')
time_label.pack()
date_label = Label(window, font=('Ink Free', 25))
date_label.pack()

update()

window.resizable(False,False)

window.mainloop()
