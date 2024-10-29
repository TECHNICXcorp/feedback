from tkinter import *
import os

root =Tk()

def create_window():
    os.system('hostmainfeedback.py')

def kill_newwin():
    os.system('hostmainfeedback.py')
    exit(0)

root = Tk()
a = Button(root, text="Create new window", command=create_window)
a.pack()
b =Button(root, text='Create new window and close current', command=kill_newwin)
b.pack()


root.mainloop()