from tkinter import *
from PIL import Image, ImageTk


def display():
    if x.get() == 1:
        print("You agree!!")
    else:
        print("You disagree!!")


window = Tk()

x = IntVar()
image = Image.open('python.png')

resize_image = image.resize((50, 50))

img = ImageTk.PhotoImage(resize_image)

check_button = Checkbutton(window,
                           text="I agree to something",
                           variable=x,
                           onvalue=1,
                           offvalue=0,
                           command=display,
                           font=('Arial', 20),
                           fg='#00ff00',
                           bg='black',
                           activeforeground='#00ff00',
                           activebackground='black',
                           padx=25,
                           pady=10,
                           image=img,
                           compound=LEFT)
check_button.pack()

window.mainloop()
