from tkinter import *
from tkinter import messagebox


def click():
    # messagebox.showinfo(title='This is an info message box', message='You are Awesome :D')
    # while True:
    # messagebox.showwarning(title='WARNING!!', message='You have a VIRUS :(')
    # messagebox.showerror(title='ERROR!!', message='Something gone wrong :(')

    # if messagebox.askokcancel(title='Confirmation',message='Do you want to abort operation'):
    #     print("You did a thing!")
    # else:
    #     print("You canceled a thing")

    # if messagebox.askyesno(title='Ask yes or no', message='Do you want to delete this file?'):
    #     print("Yes")
    # else:
    #     print("no")

    # print(messagebox.askquestion(title='question',message='Are you a gamer?')) # returns yes or no

    # answer = messagebox.askyesnocancel(title='yes no cancel', message='want to exit the matrix?')
    # if answer:
    #     print("You never gonna exit this simulation!! XD")
    # elif answer == False:
    #     print("You made the right decision :)")
    # else:
    #     print("Fuck! You exited the simulation!! ")

    messagebox.askretrycancel(title='Play Again?', message='Start over your life?')



window = Tk()

button = Button(window, command=click, text='click me')
button.pack()

window.mainloop()
