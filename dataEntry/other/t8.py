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
        name.trace("w", lambda l,idx, mode: print(E1.get()))
        self.top.mainloop()

def main():
    root = Tk()
    # global name
    feedback = FeedBack(root)
    # feedback.outEntry()
    # name.trace("w", lambda l,idx, mode: print(E1.get()))
    # feedback.outEntry()
    # feedback.entering()
    # feedback.search()
    # feedback.advanceSearch()
    # feedback.report()

    root.mainloop()
if __name__ == "__main__":main()