from tkinter import *

# grid() = geometry manager that organises widgets in a tabular structure in a parent

window = Tk()

titleLable = Label(window, text="Enter your details: ", font=(30)).grid(row=0, column=0, columnspan= 2)

firstNameLabel = Label(window, text='First Name').grid(row=1, column=0,padx=10,pady=10)
firstNameEntry = Entry(window).grid(row=1, column=1,padx=10,pady=10)

lastNameLabel = Label(window, text='Last Name').grid(row=2, column=0,padx=10,pady=10)
lastNameEntry = Entry(window).grid(row=2, column=1,padx=10,pady=10)

emalLabel = Label(window, text='Email').grid(row=3, column=0,padx=10,pady=10)
emailEntry = Entry(window).grid(row=3, column=1,padx=10,pady=10)

submitButton = Button(window, text='Submit').grid(row=4, column=0, columnspan=2)

window.resizable(False,False)

window.mainloop()
