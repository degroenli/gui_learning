from tkinter import *

root = Tk()


def set_label1(text):
    labeltext.set(text)


labeltext = StringVar()
labeltext.set("")

button1 = Button(root)
button1.config(text="Say hello!", bg="pink", font="Calibri, 50", command=lambda: set_label1("Bonjour"))
button1.grid()

button2 = Button(root)
button2.config(text="Say banana!", bg ="light blue", font="Calibri, 50", command=lambda: set_label1("Cucumber ಠ_ಠ"))
button2.grid()

button3 = Button(root)
button3.config(text="Clear text", command=lambda: set_label1(""))
button3.grid()

label1 = Label(root)
label1.config(textvariable=labeltext)
label1.grid()

root.mainloop()