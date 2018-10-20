import math
import tkinter
import compute as cp


window = tkinter.Tk()
window.title("KNN algorithm on Iris dataset")

lab1 = tkinter.Label(window,text="Sepal Length: ")
var1 = tkinter.DoubleVar()
ent1 = tkinter.Entry(window,textvariable=var1)

lab2 = tkinter.Label(window,text="Sepal Width: ")
var2 = tkinter.DoubleVar()
ent2 = tkinter.Entry(window,textvariable=var2)

lab3 = tkinter.Label(window,text="Petal Length: ")
var3 = tkinter.DoubleVar()
ent3 = tkinter.Entry(window,textvariable=var3)

lab4 = tkinter.Label(window,text="Petal Width: ")
var4 = tkinter.DoubleVar()
ent4 = tkinter.Entry(window,textvariable=var4)

def setData():
	arg1 = var1.get()
	arg2 = var2.get()
	arg3 = var3.get()
	arg4 = var4.get()
	cp.compute(arg1,arg2,arg3,arg4)


butt1 = tkinter.Button(window,text="submit",command=setData)


lab1.grid(row=1,column=1)
ent1.grid(row=1,column=3)
lab2.grid(row=2,column=1)
ent2.grid(row=2,column=3)

lab3.grid(row=3,column=1)
ent3.grid(row=3,column=3)
lab4.grid(row=4,column=1)
ent4.grid(row=4,column=3)

butt1.grid(row=5,column=2)
window.mainloop()




