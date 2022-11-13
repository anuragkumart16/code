from tkinter import*


def screen():
    root.geometry("660x436")
    root.minsize(330,218)
    root.title("Mind Slinger")


def hr_1():
    f1 = Frame(root,bg="red")
    f1.pack(side=TOP)
    hr_4=Label(f1,text="",background="grey",padx=660)
    hr_4.pack()
    hr_1=Label(f1,text="Mind Slinger ",foreground="orange",background="black",padx=660,pady=30,font="Ariel 25")
    hr_1.pack()
    hr_3=Label(f1,text="",background="grey",padx=660)
    hr_3.pack()
    
def hr_2():
    f2 = Frame(root,bg="red")
    f2.pack(side=BOTTOM)
    hr_5=Label(f2,background="grey",padx=660,pady=1)
    hr_5.pack()
    hr_2=Label(f2,text="| copyrights to @maindslinger | ",background="black",padx=660,foreground="orange")
    hr_2.pack(side="bottom")


    
def sidebar():
    f3=Frame(root,background="black", borderwidth=5,relief=SUNKEN)
    f3.pack(side="left",fill="y",)
    profile=Button(f3,text="Profile",bg="black",foreground="white",borderwidth=5,relief=SUNKEN,padx=50)
    profile.pack()
    login=Button(f3,text="Log In",foreground="white",background="black",padx=50,borderwidth=5,relief=SUNKEN)
    login.pack()
    Notes=Button(f3,text="Notes",foreground="white",background="black",padx=50,borderwidth=5,relief=SUNKEN)
    Notes.pack()

def list_1():
    f4=Frame(root)
    f4.grid()
    Username=Label(f4,text="User Name :")
    Username.grid(column=3,row=4)
    uservalue=StringVar()
    Userentry=Entry(root,textvariable = uservalue  )
    Userentry.grid(column=4,row=4)
    


def internal():
    hr_1()
    hr_2()
    sidebar()
    #list_1()

#logic here

root=Tk()
screen()
internal()
root.mainloop()

    
