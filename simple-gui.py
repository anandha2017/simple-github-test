#q: what library would you use to generate a simple gui in python
#A: tkinter

#q: write me a simple gui in python that takes a text input and displays the text in a label

from tkinter import *

root = Tk()

def print_text():
    print(text.get())
    label.config(text=text.get())

text = Entry(root)
text.pack()

button = Button(root, text="Print", command=print_text)
button.pack()

label = Label(root, text="Hello")
label.pack()

root.mainloop()
    

