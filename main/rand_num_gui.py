import time
import random
from tkinter import *
from tkinter import messagebox

gui = Tk()

gui.title("Keypad")

gui.geometry("500x500")

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]


# Config our column rows and cols
Grid.rowconfigure(gui, index=0, weight=1)
Grid.columnconfigure(gui, index=0, weight=1)

Grid.rowconfigure(gui, 1, weight=1)
Grid.columnconfigure(gui, 1, weight=1)

Grid.rowconfigure(gui, 2, weight=1)
Grid.columnconfigure(gui, 2, weight=1)

random.shuffle(nums)
numsint = int(''.join(map(str, nums)))

prompter = Label(gui, text=numsint)
prompter.grid(row=0, column=0, sticky="N", columnspan=3)

equation = StringVar()
expression_field = Entry(gui, textvariable=equation)

expression_field.grid(row=1, column=0, sticky="N", columnspan=3, )

button1 = Button(gui, text=' 1 ', fg='black', relief=RAISED, borderwidth=10)
button1.grid(row=2, column=0, sticky="NSEW", padx=10, pady=10)

button2 = Button(gui, text=' 2 ', fg='black', relief=RAISED, borderwidth=10)
button2.grid(row=2, column=1, sticky="NSEW", padx=10, pady=10)

button3 = Button(gui, text=' 3 ', fg='black', relief=RAISED, borderwidth=10)
button3.grid(row=2, column=2, sticky="NSEW", padx=10, pady=10)

button4 = Button(gui, text=' 4 ', fg='black', relief=RAISED, borderwidth=10)
button4.grid(row=3, column=0, sticky="NSEW", padx=10, pady=10)

button5 = Button(gui, text=' 5 ', fg='black', relief=RAISED, borderwidth=10)
button5.grid(row=3, column=1, sticky="NSEW", padx=10, pady=10)

button6 = Button(gui, text=' 6 ', fg='black', relief=RAISED, borderwidth=10)
button6.grid(row=3, column=2, sticky="NSEW", padx=10, pady=10)

button7 = Button(gui, text=' 7 ', fg='black', relief=RAISED, borderwidth=10)
button7.grid(row=4, column=0, sticky="NSEW", padx=10, pady=10)

button8 = Button(gui, text=' 8 ', fg='black', relief=RAISED, borderwidth=10)
button8.grid(row=4, column=1, sticky="NSEW", padx=10, pady=10)

button9 = Button(gui, text=' 9 ', fg='black', relief=RAISED, borderwidth=10)
button9.grid(row=4, column=2, sticky="NSEW", padx=10, pady=10)

buttonEnter = Button(gui, text=' Enter ', fg='black',
                     relief=RAISED, borderwidth=10)
buttonEnter.grid(row=5, column=1, sticky="NSEW", padx=10, pady=10)

buttonReset = Button(gui, text=' Reset ', fg='black',
                     relief=RAISED, borderwidth=10)
buttonReset.grid(row=5, column=2, sticky="NSEW", padx=10, pady=10)

gui.mainloop()
