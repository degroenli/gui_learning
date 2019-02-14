import tkinter
root = tkinter.Tk()

button1 = tkinter.Button(root)
button1.config(text="food soon",
               bg="teal",
               fg="light blue",
               font=("Times", "200"),
               )
button1.grid()

root.mainloop()