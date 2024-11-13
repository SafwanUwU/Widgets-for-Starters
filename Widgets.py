from tkinter import *
from datetime import date

root = Tk()
root.title('Getting Started with Widgets')
root.geometry('400x300')

lbl = Label(root, text="Hey There!", fg="white", bg="#50b4f1", height=2, width=300)
lbl.pack(pady=10)

name_lbl = Label(root, text="Full name", bg="#50f18f")
name_lbl.pack()

name_entry = Entry(root, width=30)
name_entry.pack(pady=5)

text_box = Text(root, height=4, width=45, wrap=WORD)
text_box.pack(pady=10)

def display():

    text_box.delete(1.0, END)

    name = name_entry.get()

    greet = f"Hello, {name}!\n"
    message = f"Welcome to the application! \nToday's date is: {date.today()}"

    text_box.insert(END, greet)
    text_box.insert(END, message)

btn = Button(root, text="Begin", command=display, height=1, bg="#ac430e", fg="white")
btn.pack()

root.mainloop()