import pytest
import tkinter 
from tkinter import *
from tkinter import ttk
class UI:
	def __init__(self,root):
		self.root = root
		self.tree=ttk.Treeview(root)
		self.treeView()
	def treeView(self):
		

		# L = Label(root, text ="Right-click to display menu", 
		# 		width = 40, height = 20) 
		# tree=self.tree
		# L = ttk.Treeview(root)
		self.tree.insert("","0","lCh1",text="Grand Father")
		self.tree.insert("lCh1","1","lCh2",text="Father")
		self.tree.insert("lCh2","2","lCh3",text="Son")
		###
		# print(type(self.tree))
		# print(type(L.identify("lCh1")))
		# print(type(self.tree.item("lCh1")))
		# self.tree.bind("<Button-3>", self.do_popup)
		self.tree.bind("<Button-3>", self.selecRightClick) 
		# self.tree.bind("<Double-1>", self.OnDoubleClick)
		# self.tree.bind('<<TreeviewSelect>>',self.callback)	
		# self.tree.bind('<<TreeviewSelect>>',self.do_popup)	



		###
		self.tree.grid(row=0,column=0) 
		label = Label(self.root, text ="other", 
				width = 40, height = 20) 
		label.grid(row=1,column=1) 
	# def contextMenu(self,res):
	# 	m = Menu(res, tearoff = 0) 
	# 	m.add_command(label ="Cut") 
	# 	m.add_command(label ="Copy") 
	# 	m.add_command(label ="Paste") 
	# 	m.add_command(label ="Reload") 
	# 	m.add_separator() 
	# 	m.add_command(label ="Rename") 
	def callback(self,event):
		print(self.tree.selection())
		# m = Menu(self.tree, tearoff = 0) 
		# m.add_command(label ="Cut") 
		# m.add_command(label ="Copy") 
		# m.add_command(label ="Paste") 
		# m.add_command(label ="Reload") 
		# m.add_separator() 
		# m.add_command(label ="Rename") 

	def selecRightClick(self,event):

		iid = self.tree.identify_row(event.y)
		m = self.menuItems(iid)
		print(iid)
		if iid:
			self.tree.selection_set(iid)
			try:
				m.tk_popup(event.x_root, event.y_root) 
			finally: 
				m.grab_release() 

		# try: 
		# 	m.tk_popup(event.x_root, event.y_root) 
		# 	# self.tree.selection_set()
		# finally: 
		# 	m.grab_release() 
	def menuItems(self,iid):
		m = Menu(self.tree, tearoff = 0) 
		j=iid
		if j == "lCh1":
			m.add_command(label ="lCh1") 
			m.add_command(label ="lCh1") 
			m.add_command(label ="lCh1") 
		elif j == "lCh2":
			m.add_command(label ="lCh2") 
			m.add_command(label ="lCh2") 
			m.add_command(label ="lCh2")
		elif j == "lCh3":
			m.add_command(label ="lCh3") 
			m.add_command(label ="lCh3") 
			m.add_command(label ="lCh3")
		return m

	def do_popup(self,event): 
		i = self.tree.selection()
		# self.tree
		print(i)

		m = Menu(self.tree, tearoff = 0) 
		j=i[0]
		if j == "lCh1":
			m.add_command(label ="lCh1") 
			m.add_command(label ="lCh1") 
			m.add_command(label ="lCh1") 
		elif j == "lCh2":
			m.add_command(label ="lCh2") 
			m.add_command(label ="lCh2") 
			m.add_command(label ="lCh2")
		elif j == "lCh3":
			m.add_command(label ="lCh3") 
			m.add_command(label ="lCh3") 
			m.add_command(label ="lCh3")
		return m



		try: 
			m.tk_popup(event.x_root, event.y_root) 
		finally: 
			m.grab_release() 
	
	def OnDoubleClick(self,event):
		item = self.L.identify("item", event.x, event.y)
		self.contextMenu(item)
		print(type(item),item)
		print("you clicked on")
		self.L.item(item)["text"]

# L.bind("<Button-3>", do_popup) 

def main():
    root = Tk()
    
    feedback = UI(root)
    # feedback.entering()
    # feedback.search()
    # feedback.advanceSearch()
    # feedback.report()

    root.mainloop()

if __name__ == "__main__":main()





@pytest.fixture
def ui():
	root = Tk()
	ui=UI(root)
	return ui
# mainloop() 
class TestUI:

	def test_resource(self,ui):
		# ui.treeView()
		print(type(ui.tree))
		print(ui.tree)
		# print(type(ui.L.set("lCh1")))
