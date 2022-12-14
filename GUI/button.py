# button = you click it, then it does stuff

from tkinter import *

count = 0

def click():
    global count
    count += 1
    print(count)


window = Tk()

like = PhotoImage(file='like.png')

button = Button(window,
                text="Click Me!!",
                command=click,
                font=('Comic Sans', 30),
                fg='#00ff00',
                bg='black',
                activeforeground='#00ff00',
                activebackground='black',
                state=ACTIVE,
                image=like,
                compound=TOP,
                )
button.pack()

window.mainloop()
