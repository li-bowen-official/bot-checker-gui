from tkinter import *

win = Tk()
win.geometry("700x300")

# Dynamically resize the window and its widget

Grid.rowconfigure(win, index=0, weight=1)
Grid.columnconfigure(win, index=0, weight=1)

# Define the function to change the size of the button text


def resize(e):
    # Get the width of the button
    w = e.width/10
    # Dynamically Resize the Button Text
    b.config(font=("Times New Roman", int(w)))
    # Resize the height
    if e.height <= 300:
        b.config(font=("Times New Roman", 30))
    elif e.height < 100:
        b.config(font=("Time New Roman", 10))
# Let us Create buttons,


b = Button(win, text="Python")
b.grid(row=0, column=0, sticky="nsew")

win.bind('<Configure>', resize)
win.mainloop()
