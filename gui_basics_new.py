import Tkinter as tk

class Demo1:
	def __init__(self, master):
		self.master = master
		self.frame = tk.Frame(self.master)
		self.button1 = tk.Button(self.frame, text = 'New Window', width = 25, command = self.new_window)
		self.button1.pack()
		self.frame.pack()

	def new_window(self):
		self.newWindow = tk.Toplevel(self.master)
		self.app = Demo2(self.newWindow)

class Demo2(tk.Toplevel):     
    def __init__(self):
        tk.Toplevel.__init__(self)
        self.title("Demo 2")
        self.button = tk.Button(self, text="Button 2", # specified self as master
                                width=25, command=self.close_window)
        self.button.pack()

    def close_window(self):
        self.destroy()

def main(): 
	root = tk.Tk()
	app = Demo1(root)
	root.mainloop()

if __name__ == '__main__':
	main()