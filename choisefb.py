from tkinter import *

root = Tk()
root['bg']="gray22"

lb1=Listbox(root , selectmode=SINGLE , bg="gray22", fg="white")
list1= ["Клієнт","СТО"]
for i in list1:
    lb1.insert (END, i)
lb1.pack()

root.mainloop()