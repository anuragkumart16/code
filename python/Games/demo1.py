#roll
from tkinter import*
import random
c=0
def roll():
     global a
     a=random.randint(1,6)
     global c
     mon1.set(a)
     if c==0:          
          if a!=6:
               b="                       You Need 6 To Start"
               msg.set(b)
          elif mon1.get()=="":
               b=""
               msg.set(b)
          elif a==6:
               b="               Now You Can Move Further"
               msg.set(b)
               c=c+1
               print(c)
     elif c!=0:
          c=c+a
          if c>100:
               c=c-a
               b="you gained extra steps"
               msg.set(b)
          elif c<95:
               b="                     Piece position",c
               msg.set(b)
     


root=Tk()
#frame
frame=Frame(root,pady=5)
frame.pack()
Label(frame,text="100").pack(side=LEFT)
Label(frame,text="99").pack(side=LEFT)
Label(frame,text="98").pack(side=LEFT)
Label(frame,text="97").pack(side=LEFT)
Label(frame,text="96").pack(side=LEFT)
Label(frame,text="95").pack(side=LEFT)
Label(frame,text="94").pack(side=LEFT)
Label(frame,text="93").pack(side=LEFT)
Label(frame,text="92").pack(side=LEFT)
Label(frame,text="91").pack(side=LEFT)
#frame1
frame1=Frame(root,pady=5)
frame1.pack()
Label(frame1,text="90").pack(side=LEFT)
Label(frame1,text="89").pack(side=LEFT)
Label(frame1,text="88").pack(side=LEFT)
Label(frame1,text="87").pack(side=LEFT)
Label(frame1,text="86").pack(side=LEFT)
Label(frame1,text="85").pack(side=LEFT)
Label(frame1,text="84").pack(side=LEFT)
Label(frame1,text="83").pack(side=LEFT)
Label(frame1,text="82").pack(side=LEFT)
Label(frame1,text="81").pack(side=LEFT)
#frame2
frame2=Frame(root,pady=5)
frame2.pack()
Label(frame2,text="80").pack(side=LEFT)
Label(frame2,text="79").pack(side=LEFT)
Label(frame2,text="78").pack(side=LEFT)
Label(frame2,text="77").pack(side=LEFT)
Label(frame2,text="76").pack(side=LEFT)
Label(frame2,text="75").pack(side=LEFT)
Label(frame2,text="74").pack(side=LEFT)
Label(frame2,text="73").pack(side=LEFT)
Label(frame2,text="72").pack(side=LEFT)
Label(frame2,text="71").pack(side=LEFT)
#frame3
frame3=Frame(root,pady=5)
frame3.pack()
Label(frame3,text="70").pack(side=LEFT)
Label(frame3,text="69").pack(side=LEFT)
Label(frame3,text="68").pack(side=LEFT)
Label(frame3,text="67").pack(side=LEFT)
Label(frame3,text="66").pack(side=LEFT)
Label(frame3,text="65").pack(side=LEFT)
Label(frame3,text="64").pack(side=LEFT)
Label(frame3,text="63").pack(side=LEFT)
Label(frame3,text="62").pack(side=LEFT)
Label(frame3,text="61").pack(side=LEFT)
#frame4
frame4=Frame(root,pady=5)
frame4.pack()
Label(frame4,text="60").pack(side=LEFT)
Label(frame4,text="59").pack(side=LEFT)
Label(frame4,text="58").pack(side=LEFT)
Label(frame4,text="57").pack(side=LEFT)
Label(frame4,text="56").pack(side=LEFT)
Label(frame4,text="55").pack(side=LEFT)
Label(frame4,text="54").pack(side=LEFT)
Label(frame4,text="53").pack(side=LEFT)
Label(frame4,text="52").pack(side=LEFT)
Label(frame4,text="51").pack(side=LEFT)
#frame5
frame5=Frame(root,pady=5)
frame5.pack()
Label(frame5,text="60").pack(side=LEFT)
Label(frame5,text="49").pack(side=LEFT)
Label(frame5,text="48").pack(side=LEFT)
Label(frame5,text="47").pack(side=LEFT)
Label(frame5,text="46").pack(side=LEFT)
Label(frame5,text="45").pack(side=LEFT)
Label(frame5,text="44").pack(side=LEFT)
Label(frame5,text="43").pack(side=LEFT)
Label(frame5,text="42").pack(side=LEFT)
Label(frame5,text="41").pack(side=LEFT)
#frame6
frame6=Frame(root,pady=5)
frame6.pack()
Label(frame6,text="40").pack(side=LEFT)
Label(frame6,text="39").pack(side=LEFT)
Label(frame6,text="38").pack(side=LEFT)
Label(frame6,text="37").pack(side=LEFT)
Label(frame6,text="36").pack(side=LEFT)
Label(frame6,text="35").pack(side=LEFT)
Label(frame6,text="34").pack(side=LEFT)
Label(frame6,text="33").pack(side=LEFT)
Label(frame6,text="32").pack(side=LEFT)
Label(frame6,text="31").pack(side=LEFT)
#frame7
frame7=Frame(root,pady=5)
frame7.pack()
Label(frame7,text="30").pack(side=LEFT)
Label(frame7,text="29").pack(side=LEFT)
Label(frame7,text="28").pack(side=LEFT)
Label(frame7,text="27").pack(side=LEFT)
Label(frame7,text="26").pack(side=LEFT)
Label(frame7,text="25").pack(side=LEFT)
Label(frame7,text="24").pack(side=LEFT)
Label(frame7,text="23").pack(side=LEFT)
Label(frame7,text="22").pack(side=LEFT)
Label(frame7,text="21").pack(side=LEFT)
#frame8
frame8=Frame(root,pady=5)
frame8.pack()
Label(frame8,text="20").pack(side=LEFT)
Label(frame8,text="19").pack(side=LEFT)
Label(frame8,text="18").pack(side=LEFT)
Label(frame8,text="17").pack(side=LEFT)
Label(frame8,text="16").pack(side=LEFT)
Label(frame8,text="15").pack(side=LEFT)
Label(frame8,text="14").pack(side=LEFT)
Label(frame8,text="13").pack(side=LEFT)
Label(frame8,text="12").pack(side=LEFT)
Label(frame8,text="11").pack(side=LEFT)
#frame9
frame9=Frame(root,pady=5)
frame9.pack()
Label(frame9,text="10").pack(side=LEFT)
Label(frame9,text=" 9 ").pack(side=LEFT)
Label(frame9,text=" 8 ").pack(side=LEFT)
Label(frame9,text=" 7 ").pack(side=LEFT)
Label(frame9,text=" 6 ").pack(side=LEFT)
Label(frame9,text=" 5 ").pack(side=LEFT)
Label(frame9,text=" 4 ").pack(side=LEFT)
Label(frame9,text=" 3 ").pack(side=LEFT)
Label(frame9,text=" 2 ").pack(side=LEFT)
Label(frame9,text=" 1 ").pack(side=LEFT)
#frame10
frame10=Frame(root,pady=10)
frame10.pack()
Button(frame10,text="Roll !",command=roll).pack()
msg=StringVar()
msgbox=Entry(frame10,textvariable=msg,width=40)
msgbox.pack(pady=5)
#frame11
#mon1
frame11=Frame(root,bg="black")
frame11.pack()

mon1=StringVar()
Monitor1=Entry(frame11,textvariable=mon1,width=1)
Monitor1.pack(pady=5)

#logic of the game





root.mainloop()
