from tkinter import *
import tkinter as tk
master = Tk()

scrollbar = tk.Scrollbar(master)
scrollbar.grid(row=1,column=2,sticky="nsew")

listbox = Listbox(master,yscrollcommand=scrollbar.set)
listbox.grid(row=1,column=1)
scrollbar.config(command=listbox.yview)
listbox.insert(END, "a list entry")

for item in ["one", "two", "three", "four","one", "two", "three", "four","one", "two", "three", "four"]:
    listbox.insert(END, item)


def onselect(event):
    w = event.widget
    idx = int(w.curselection()[0])
    value=w.get(idx)
    print(value)

listbox.bind("<<ListboxSelect>>",onselect)
mainloop()