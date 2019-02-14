import tkinter
root = tkinter.Tk()

root.title("Cucumbers")
root.geometry("420x666")

my_label = tkinter.Label(root)
my_label.config(text="Hello", fg="light blue", font=("Times","150","bold"))
my_label.grid()

my_label2 = tkinter.Label(root)
my_label2.config(text="How are you?", fg="light blue", font=("Times","50","bold"))
my_label2.grid()

my_label3 = tkinter.Label(root)
my_label3.config(text="I hope you're doing good", fg="light blue", font=("Times","50","bold"))
my_label3.grid()

my_label4 = tkinter.Label(root)
my_label4.config(text="Bye", fg="light green", font=("Times","50","bold"),pady="50")
my_label4.grid()


root.mainloop()