from tkinter import*
from tkinter import ttk
from tkinter.messagebox import showinfo
import math



frequency =1
def drop_events(e):
     global frequency
     if dropdown.get()=="Yearly":
          frequency=1
     elif dropdown.get()=="Half Yearly":
          frequency=2
     elif dropdown.get()=="Quaterly":
          frequency=4
     elif dropdown.get()=="Monthly":
          frequency=12
     elif dropdown.get()=="Daily":
          frequency=365

    
def calculate():
    Alpha=rate.get()/frequency*100
    Alpha=Alpha+1
    Beta=frequency*time.get()
    Ammount=principal.get()*math.pow(Alpha,Beta)
    CI=Ammount-principal.get()
    monamm.set(Ammount)
    monci.set(CI) 

#Edit functions
def clear_all():
     principal.set(0)
     time.set(0)
     rate.set(0)
     dropdown.set("Yearly")
     monamm.set(" ")
     monci.set(" ")

#Help functions
def feedback():
    showinfo("Feedback","visit https://mindslingeranu1.blogspot.com")
def about():
    showinfo("Compund Interest Calculator","Calculator by Anurag")

#_________________________________________________________________
root=Tk()
root.title("Compound Interest Calculator")
root.geometry("380x466")
#main menu code start from here
Menu_=Menu(root)
#File
File=Menu(Menu_,tearoff=0)
File.add_command(label="Exit",command=quit)
#Edit
Edit=Menu(Menu_,tearoff=0)
Edit.add_command(label="Clear all",command=clear_all)


#Help
Help=Menu(Menu_,tearoff=0)
Help.add_command(label="About",command=about)
Help.add_command(label="Feedback",command=feedback)
root.config(menu=Menu_)
Menu_.add_cascade(label="File",menu=File)
Menu_.add_cascade(label="Edit",menu=Edit)
Menu_.add_cascade(label="Help",menu=Help)

#main menu code ends here

frame_top=Frame(root,bg="grey")
frame_top.pack()
Label(frame_top,text="Compound Interest Calculator",font="Lucida 17").pack()
Label(frame_top).pack()

#frame1
frame1=Frame(root,pady=40)
frame1.pack()
frame1_1=Frame(frame1,padx=3)
frame1_1.pack(side=LEFT)
frame1_2=Frame(frame1,padx=3)
frame1_2.pack(side=RIGHT)

principal=IntVar()
rate=IntVar()

Label(frame1_1,text="Principal :",padx=5).pack(side=LEFT)
prientry=Entry(frame1_1,textvariable=principal)
prientry.pack(side=LEFT)

ratentry=Entry(frame1_2,textvariable=rate)
ratentry.pack(side=RIGHT,padx=5)
Label(frame1_2,text="Rate :").pack(side=RIGHT)



#frame2
frame2=Frame(root,pady=5)
frame2.pack()
frame2_1=Frame(frame2)
frame2_1.pack(side=LEFT)
frame2_2=Frame(frame2)
frame2_2.pack(side=RIGHT)

time=IntVar()
Label(frame2_1,text="Time :").pack(side=LEFT)
timentry=Entry(frame2_2,textvariable=time)
timentry.pack(side=LEFT,padx=5)

dropdown=ttk.Combobox(frame2_2,width=15,value=["Yearly","Half Yearly","Quaterly","Monthly","Daily"])
dropdown.current(0)
dropdown.pack(side=RIGHT)
dropdown.bind("<<ComboboxSelected>>",drop_events)
Label(frame2_2,text="Frequency :").pack(side=RIGHT)

#frame3
frame3=Frame(root,pady=20)
frame3.pack()
Button(frame3,text="Calculate",command=calculate).pack()

#frame4
monamm=StringVar()
frame4=Frame(root,pady=5)
frame4.pack()
Label(frame4,text="Ammount :").pack(side=LEFT)
MonAmm=Entry(frame4,textvariable=monamm)
MonAmm.pack()


#frame5
monci=StringVar()
frame5=Frame(root,pady=5)
frame5.pack()
Label(frame5,text="Compund Interest").pack(side=LEFT)
MonCI=Entry(frame5,textvariable=monci)
MonCI.pack(side=LEFT)


root.mainloop()

