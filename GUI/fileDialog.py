from tkinter import *
from tkinter import filedialog


def openfile():
    filepath = filedialog.askopenfilename(initialdir="F:\\Python Leaning",
                                          title='open file okay?',
                                          filetypes=(("text files", "*.txt"),
                                                     ("all files", "*.*"))
                                          )

    file = open(filepath, 'r')

    print(file.read())
    file.close()


def save():
    file = filedialog.asksaveasfile(initialdir="F:\\Python Leaning",
                                    defaultextension='*.txt',
                                    title='save file ?',
                                    filetypes=(('Text Files', '.txt'),
                                               ('HTML Files', '.html'),
                                               ('All Files', '.*')
                                               )
                                    )

    if file is None:
        return
    filetext = str(text.get(1.0, END))
    file.write(filetext)
    file.close()


def main():
    window = Tk()

    text = Text(window)
    text.pack()

    saveButton = Button(text='save', command=save)
    saveButton.pack()

    button = Button(text='open', command=openfile)
    button.pack()

    window.mainloop()


if __name__ == '__main__':
    main()
