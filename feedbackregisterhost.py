from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("TECHNICX feedback")
window.geometry("500x320")
window.resizable(width=False,height=False)
window['bg'] = "gray22"

l1=Label(text="Вітаємо в додатку!", font="Vernada 17" , fg="white")
l1.pack()
l1['bg']="gray22"

l2=Label(text="Для того щоб продовжити необхідно зареєструватись.", font="Vernada 13" , fg="white")
l2.pack()
l2['bg']="gray22"

value=IntVar()
l3=Label(text="Ключ доступу" , font="Vernada 15" , fg="white")
l3.pack()
l3['bg']="gray22"

f1= Frame(window , bg="gray22", bd=8)
f1.pack()

e1=Entry(f1,width=200 , font="Vernada 13",justify=CENTER,foreground="gray22")
e1.pack()
e1.insert(0,"")
e1['bg']= "white"
 
value2=StringVar()
 
l4=Label(text="Ваш email" , font="Vernada 15" , fg="white")
l4.pack()
l4['bg']="gray22"

f2= Frame(window , bg="gray22", bd=8)
f2.pack()

e2=Entry(f2,width=100 , font="Vernada 13",justify=RIGHT,foreground="gray22")
e2.pack()
e2.insert(0,"@gmail  ")
e2['bg']= "white"

l4=Label(text="Ваше П.І.Б." , font="Vernada 15" , fg="white")
l4.pack()
l4['bg']="gray22"

f3= Frame(window , bg="gray22", bd=8)
f3.pack()

e3=Entry(f3,width=100 , font="Vernada 13",justify=CENTER,foreground="gray22")
e3.pack()
e3.insert(0,"")
e3['bg']= "white"

f4= Frame(window, bg="gray22", bd=8)
f4.pack()
   
b1 = Button(f4,text="готово", font="Vernada 15" ,foreground="white")
b1['bg']="gray22"
b1.pack()



window.mainloop()