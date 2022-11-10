
from tkinter import *
from tkinter import ttk    

root = Tk()

notebook = ttk.Notebook(root)
notebook.pack()

frame1=ttk.Frame(notebook)
# frame2=ttk.Frame(notebook)
notebook.add(frame1,text="One")
# label = ttk.Label(frame1,text = "adsfasdfasdfsadfadsf")
# label.grid(row = 0,column=1)
def btn_click():
    label.configure(text = "00")
    pass
def btn_click_before():
    label.configure(text = "before adsfasdfasdfsadfadsf")
    pass
# notebook.add(frame2,text="Two")

label = ttk.Label(frame1,text = "adsfasdfasdfsadfadsf")
label.grid(row = 0,column=1)
btn = ttk.Button(frame1,text="Click Me",command = btn_click).grid(row = 2,column=1)
btn = ttk.Button(frame1,text="to make like before",command = btn_click_before).grid(row = 2,column=2)

# lb2 = ttk.Label(frame1,text = "00", COMMAND = btn).grid(row = 0,column=1)

# frame3 = ttk.Frame(notebook)
# notebook.insert(1,frame3,text="Three")
# notebook.forget(1)
# notebook.add(frame3,text="Three")



# print(notebook.select())
# print(notebook.index(notebook.select()))
# notebook.select(1)

# notebook.tab(1, state = 'disabled')
# notebook.tab(1, state = 'hidden')
# notebook.tab(1, state = 'normal')
# notebook.tab(1, 'text')
# notebook.tab(1)

root.mainloop()