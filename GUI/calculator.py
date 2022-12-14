from tkinter import *


def button_press(num):
    global equation_text
    equation_text = equation_text + str(num)
    equation_label.set(equation_text)


def equals():
    global equation_text

    try:
        result = str(eval(equation_text))
        equation_label.set(result)
        equation_text = result

    except ZeroDivisionError:
        equation_label.set('Cannot divide by zero')
        equation_text = ""

    except SyntaxError:
        equation_label.set("Syntax Error")
        equation_text = ""


def clear():
    global equation_text
    equation_text = ""
    equation_label.set("")


window = Tk()
window.title("Calculator App")
window.geometry("450x670")

equation_text = ""

equation_label = StringVar()

label = Label(window, textvariable=equation_label, font=('Consolas', 20), bg='#d8edde', width=29, height=3,
              relief=SUNKEN)
label.pack(pady=10)

frame = Frame(window, relief=RAISED)
frame.pack()

buttonClear = Button(frame, text='AC', height=4, width=29, font=90,
                     command=clear, bg='red', fg='white')
buttonClear.grid(row=0, column=0, columnspan=3)

button1 = Button(frame, text='1', height=4, width=9, font=35,
                 command=lambda: button_press(1), bg='#a4cff5')
button1.grid(row=1, column=0)

button2 = Button(frame, text='2', height=4, width=9, font=35,
                 command=lambda: button_press(2), bg='#a4cff5')
button2.grid(row=1, column=1)

button3 = Button(frame, text='3', height=4, width=9, font=35,
                 command=lambda: button_press(3), bg='#a4cff5')
button3.grid(row=1, column=2)

button4 = Button(frame, text='4', height=4, width=9, font=35,
                 command=lambda: button_press(4), bg='#a4cff5')
button4.grid(row=2, column=0)

button5 = Button(frame, text='5', height=4, width=9, font=35,
                 command=lambda: button_press(5), bg='#a4cff5')
button5.grid(row=2, column=1)

button6 = Button(frame, text='6', height=4, width=9, font=35,
                 command=lambda: button_press(6), bg='#a4cff5')
button6.grid(row=2, column=2)

button7 = Button(frame, text='7', height=4, width=9, font=35,
                 command=lambda: button_press(7), bg='#a4cff5')
button7.grid(row=3, column=0)

button8 = Button(frame, text='8', height=4, width=9, font=35,
                 command=lambda: button_press(8), bg='#a4cff5')
button8.grid(row=3, column=1)

button9 = Button(frame, text='9', height=4, width=9, font=35,
                 command=lambda: button_press(9), bg='#a4cff5')
button9.grid(row=3, column=2)

button0 = Button(frame, text='0', height=4, width=19, font=35,
                 command=lambda: button_press(0), bg='#a4cff5')
button0.grid(row=4, column=0, columnspan=2)

buttondot = Button(frame, text='.', height=4, width=9, font=35,
                   command=lambda: button_press('.'), bg='white', fg='#1b6bf5')
buttondot.grid(row=4, column=2)

buttonDivide = Button(frame, text='/', height=4, width=9, font=35,
                      command=lambda: button_press('/'), bg='white', fg='#1b6bf5')
buttonDivide.grid(row=0, column=3)

buttonMultiply = Button(frame, text='*', height=4, width=9, font=35,
                        command=lambda: button_press('*'), bg='white', fg='#1b6bf5')
buttonMultiply.grid(row=1, column=3)

buttonMinus = Button(frame, text='-', height=4, width=9, font=35,
                     command=lambda: button_press('-'), bg='white', fg='#1b6bf5')
buttonMinus.grid(row=2, column=3)

buttonPlus = Button(frame, text='+', height=4, width=9, font=35,
                    command=lambda: button_press('+'), bg='white', fg='#1b6bf5')
buttonPlus.grid(row=3, column=3)

buttonEquals = Button(frame, text='=', height=4, width=9, font=35,
                      command=equals, bg='#1b6bf5', fg='white', )
buttonEquals.grid(row=4, column=3)

window.resizable(False, False)
window.mainloop()
