import tkinter as tk
from tkinter import ttk
from random import choice
from Elements.Types import Types
from Elements.Descriptors import Descriptors
from Elements.Foci import Foci

win = tk.Tk()

win.title("Numenera Concept Generator")

def randomize():
    descriptor = choice(Descriptors)
    ntype = choice(Types)
    focus = choice(Foci)
    return "I am a {0} {1} who {2}".format(descriptor, ntype, focus)

def randomize_button():
    label.configure(text=randomize())

label = ttk.Label(win, text=randomize())
label.grid(column=0, row=0)

action = ttk.Button(win, text="Generate Concept", command=randomize_button)
action.grid(column=0, row=2)

win.mainloop()




