# label = an area widget that holds text and/or image within a window

from tkinter import *

window = Tk()

photo = PhotoImage(file='coding.png')

label = Label(window,
              text="bro, do you even code?",
              font=('Arial', 40, 'bold'),
              fg='#00ff00',
              bg='black',
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20,
              image=photo,
              compound=BOTTOM)
label.pack()
# label.place(x=100, y=100)
window.mainloop()
