from tkinter import *
from PIL import Image, ImageTk


def submit():
    print("The temperature is: ", scale.get(), "degrees C")


window = Tk()

hot = Image.open('fire.png')
hotImg = ImageTk.PhotoImage(hot.resize((70, 70)))
hotLabel = Label(image=hotImg)
hotLabel.pack()

scale = Scale(window,
              from_=100,
              to=0,
              length=600,
              orient=VERTICAL,  # orientation of scale
              font=('Consolas', 20),
              tickinterval=10,  # adds numeric indicators
              showvalue=False,  # hides value next to slider
              resolution=5,  # increment of slider
              troughcolor='#69EAFF',
              fg='#FF1C00',
              bg='black'
              )

scale.set(((scale['from'] - scale['to']) / 2) + scale['to'])  # formula to calculate middle of the scale
scale.pack()

cold = Image.open('snowflake.png')
coldImg = ImageTk.PhotoImage(cold.resize((70, 70)))
coldLabel = Label(image=coldImg)
coldLabel.pack()

button = Button(window, text='Submit', command=submit)
button.pack()

window.mainloop()
