# listbox = A listing of selectable of text items within it's own container

from tkinter import *


def submit():
    # print(listbox.get(listbox.curselection()))
    food = []
    for index in listbox.curselection():
        food.insert(index, listbox.get(index))

    print("You have ordered: ")
    for index in food:
        print(index)


def add():
    listbox.insert(listbox.size(), entrybox.get())
    listbox.config(height=listbox.size())


def delete():
    # listbox.delete(listbox.curselection())
    for index in reversed(listbox.curselection()):
        listbox.delete(index)
    listbox.config(height=listbox.size())


window = Tk()

listbox = Listbox(window,
                  bg='#f7ffde',
                  font=('Constantia', 30),
                  width=12,
                  selectmode=MULTIPLE)
listbox.pack()

listbox.insert(1, "pizza")
listbox.insert(2, "hotdog")
listbox.insert(3, "hamburger")
listbox.insert(4, "fried chicken")
listbox.insert(5, "bacon")

listbox.config(height=listbox.size())

entrybox = Entry(window)
entrybox.pack()

submitButton = Button(window,
                      text="Submit",
                      command=submit)
submitButton.pack()

addButton = Button(window, text="add", command=add)
addButton.pack()

deleteButton = Button(window, text="delete", command=delete)
deleteButton.pack()

window.mainloop()
