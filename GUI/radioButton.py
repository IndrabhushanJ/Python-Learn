from tkinter import *

food = ["pizza", "hamburger", "hotdog"]


def order():
    if x.get() == 0:
        print("You ordered pizza")
    elif x.get() == 1:
        print("You ordered hamburger")
    elif x.get() == 2:
        print("You ordered hotdog")
    else:
        print("huh?")


window = Tk()

x = IntVar()
pizzaImg = PhotoImage(file='pizza.png')
hamburgerImg = PhotoImage(file='hamburger.png')
hotdogImg = PhotoImage(file='hot-dog.png')
foodImg = [pizzaImg, hamburgerImg, hotdogImg]

for index in range(len(food)):
    radiobuttion = Radiobutton(window,
                               text=food[index],  # add text to radio button
                               variable=x,  # groups radiobuttons together if they share the same variable
                               value=index,  # assigns each radiobutton a different value
                               padx=25,
                               font=('Impact', 50),
                               image=foodImg[index],
                               compound=LEFT,  # add image to radiobutton
                               indicatoron=True,  # eliminate circle indicator
                               width=500,  # set width of radio buttons
                               command=order
                               )
    radiobuttion.pack(anchor=W)

window.mainloop()
