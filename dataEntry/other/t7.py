from tkinter import *
from tkinter import ttk 
import tkinter as tk
class FeedBack:
    def __init__(self,root):
        pass
        self.top = root
        self.outEntry()
    def outEntry(self):

        # top = Tk()
        L1 = Label(self.top, text="User Name")
        # L1.pack( side = LEFT)
        L1.grid(row=1,column=0, padx = 10,sticky="nw")

        name = tk.StringVar()
        E1 = Entry(self.top, bd =5,textvariable = name)
        # E1.pack(side = RIGHT)
        E1.grid(row=1,column=1, padx = 10,sticky="nw")
        # E1.focus_set()
        # name.trace("w", lambda l,idx, mode: print(E1.get()))
        # top.mainloop()


    root = Tk()


    root.mainloop()
