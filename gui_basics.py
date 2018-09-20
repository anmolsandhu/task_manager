from Tkinter import *


root = Tk()

def basic_stuff():
	global root
	window = root
	lbl = Label(window, text = "Hello", font = ("Arial Bold", 50))
	#lbl.grid(column = 10, row = 10)

	btn = Button(window, text = "click Me", bg = "white", fg = "black", command = next_window())
	btn.grid(column = 10, row = 10)

	window.title("Task Manager")
	window.geometry('800x400')

	window.mainloop()


def next_window():

	global root
	window = root

	lbl = Label(window, text = "Hello", font = ("Arial Bold", 50))
	lbl.grid(column = 10, row = 10)

	btn = Button(window, text = "click Me", bg = "white", fg = "black")
	btn.grid(column = 10, row = 10)

	window.title("Task Manager")
	window.geometry('800x400')

	window.mainloop()



basic_stuff()
