from tkinter import*

root = Tk()
root.title("Lily's Calculator")

def add_to_input_text(next_val):
    current_text = input_text.get()
    input_text.set(current_text+next_val)

def answer():
    ans = eval(input_text.get())
    answer_value.set(ans)

def clear():
    input_text.set("")
    answer_value.set("")

input_text = StringVar()
input_text.set("")

answer_value = StringVar()
answer_value.set("")

root.mainloop()