from tkinter import*


def window():
    root.title("Calculator")
    root.maxsize(230,302)
    root.minsize(230,302)

def frame1():
    frame1=Frame(root,background="black")
    frame1.pack(fill="x",side=TOP,anchor="nw")
    l1=Label(frame1,text="Basic Calculator",bg="black",foreground="white",font="Yellowtail 13",pady=13)
    l1.pack()

def frame2():
    frame2=Frame(root,background="white")
    frame2.pack()
    l2=Label(frame2,text="",bg="white",padx=230)
    l2.pack()

def frame3():
    frame3=Frame(root,background="white")
    frame3.pack()
    l4=Label(frame3,text="",background="black",pady=20,padx=100)
    l4.pack(side="top")
    l5=Label(frame3,background="white",padx=230)
    l5.pack(side="top",anchor="ne")
    

def frame4():
    frame4=Frame(root,bg="white",width=220)
    frame4.pack(side="top",anchor="n")
    _del=Button(frame4,text="<Del",bg="orange",width=5)
    _del.pack(side=LEFT)
    clear=Button(frame4,text="Clear",bg="orange",width=5)
    clear.pack(side=LEFT)
    bracket_left=Button(frame4,text="(",width=5)
    bracket_left.pack(side=LEFT)
    bracket_right=Button(frame4,text=")",width=5)
    bracket_right.pack(side=LEFT)
    mod=Button(frame4,text="Mod",width=5)
    mod.pack(side=LEFT)
    

def frame5():
    frame5=Frame(root,bg="white",width=220)
    frame5.pack(side="top",anchor="n")
    _7=Button(frame5,text="7",width=5)
    _7.pack(side=LEFT)
    _8=Button(frame5,text="8",width=5)
    _8.pack(side=LEFT)
    _9=Button(frame5,text="9",width=5)
    _9.pack(side=LEFT)
    plus=Button(frame5,text="+",width=5)
    plus.pack(side=LEFT)
    x=Button(frame5,text="x",width=5)
    x.pack()
    
    
    

def frame6():
    frame6=Frame(root,bg="white",width=220)
    frame6.pack(side="top",anchor="n")
    _4=Button(frame6,text="4",width=5)
    _4.pack(side=LEFT)
    _5=Button(frame6,text="5",width=5)
    _5.pack(side=LEFT)
    _6=Button(frame6,text="6",width=5)
    _6.pack(side=LEFT)
    minus=Button(frame6,text="-",width=5)
    minus.pack(side=LEFT)
    divide=Button(frame6,text="/",width=5)
    divide.pack(side=LEFT)

def frame7():
    frame7=Frame(root)
    frame7.pack(side="top",anchor="n")
    _1=Button(frame7,text="1",width=5)
    _1.pack(side=LEFT)
    _2=Button(frame7,text="2",width=5)
    _2.pack(side=LEFT)
    _3=Button(frame7,text="3",width=5)
    _3.pack(side=LEFT)
    equals=Button(frame7,text="=",width=5,)
    equals.pack(side=LEFT)
    about=Button(frame7,text="About",width=5,)
    about.pack(side=LEFT)

def frame8():
    frame8=Frame(root)
    frame8.pack(side="top",anchor="n")
    zero=Button(frame8,text="0",width=10)
    zero.pack(side=LEFT)
    dot=Button(frame8,text=".",width=8)
    dot.pack(side=LEFT)
    hastag=Button(frame8,text="#",width=10)
    hastag.pack(side=LEFT)


def frame10():
    frame=Frame(root)
    frame.pack(side=BOTTOM)
    label=Label(frame,text="",bg="white",padx=230)
    label.pack()
    
    
    




root=Tk()
window()
frame1()
frame2()
frame3()
frame4()
frame5()
frame6()
frame7()
frame8()
frame10()

root.mainloop()
