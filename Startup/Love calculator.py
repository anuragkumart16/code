from tkinter import*
import random



def calculate():
    a=random.randint(85,100)
    Monitor=Label(text=a,bg="red")
    Monitor.pack(side=BOTTOM,fill="x")
    Monitor2=Label(text="Have A Great Bond",bg="red")
    Monitor2.pack(side=BOTTOM,fill="x")
    Monitor=Label(text=( person1.get(),"And",person2.get()),bg="red")
    Monitor.pack(side=BOTTOM,fill="x")

root=Tk()
root.geometry("244x244")
root.title("Love Calculator")
Label(text="Love Calculator",bg="red",font="Lucida 20").pack(side=TOP)

person1=StringVar()
person2=StringVar()
frame1=Frame(root,pady=10)
frame1.pack()
Label(frame1,text="Your Name :").pack(side=LEFT)
firstperson=Entry(frame1,textvariable=person1)
firstperson.pack(side=LEFT)
frame2=Frame(root,pady=10)
frame2.pack()
Label(frame2,text="Mate Name :").pack(side=LEFT)
secondperson=Entry(frame2,textvariable=person2)
secondperson.pack(side=LEFT)
frame3=Frame(root)
frame3.pack()
calculate=Button(frame3,text="Calculate",command=calculate)
calculate.pack()
#Monitor=Label(text=a,bg="red")
#Monitor.pack(side=BOTTOM)
root.mainloop()
