#dice
from tkinter import *
import random
position=0
Numbers=[0, 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
              27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
              51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74,
              75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
          
def dice():
     global position
     if position==0:
          dice_count=random.randint(1,6)
          if dice_count==6:
               dicemon.set(dice_count)
               position=1
               for widget in monitorframe.winfo_children():
                    widget.destroy()
               Label(monitorframe,text="Piece is Out",fg="green").pack()
          else:
               for widget in monitorframe.winfo_children():
                    widget.destroy()
               Label(monitorframe,text="Roll The Dice Again Untill Its 6",fg="red").pack()
     else:
          dice_count=random.randint(1,6)
          dicemon.set(dice_count)
          position+=dice_count
          position_mon_variable.set(position)
          global Numbers
          Numbers[position]="* "
          print(Numbers)
          screen()

def screen():
     for widget in frame.winfo_children():
          widget.destroy()
     #frame1
     frame1=Frame(frame,pady=5)
     frame1.pack()
     for a in range(1,11):
          Label(frame1,text=Numbers[a],bg="black",fg="white").pack(side=LEFT,padx=5)
     #frame2
     frame2=Frame(frame,pady=5)
     frame2.pack()
     for b in range(11,21):
          Label(frame2,text=Numbers[b],bg="black",fg="white").pack(side=LEFT,padx=5)
     #frame3
     frame3=Frame(frame,pady=5)
     frame3.pack()
     for c in range(21,31):
          Label(frame3,text=Numbers[c],bg="black",fg="white").pack(side=LEFT,padx=5)
     #frame4
     frame4=Frame(frame,pady=5)
     frame4.pack()
     for d in range(31,41):
          Label(frame4,text=Numbers[d],bg="black",fg="white").pack(side=LEFT,padx=5)
     #frame5
     frame5=Frame(frame,pady=5)
     frame5.pack()
     for e in range(41,51):
          Label(frame5,text=Numbers[e],bg="black",fg="white").pack(side=LEFT,padx=5)
     #frame6
     frame6=Frame(frame,pady=5)
     frame6.pack()
     for f in range(51,61):
          Label(frame6,text=Numbers[f],bg="black",fg="white").pack(side=LEFT,padx=5)
     #frame7
     frame7=Frame(frame,pady=5)
     frame7.pack()
     for g in range(61,71):
          Label(frame7,text=Numbers[g],bg="black",fg="white").pack(side=LEFT,padx=5)
     #frame8
     frame8=Frame(frame,pady=5)
     frame8.pack()
     for h in range(71,81):
          Label(frame8,text=Numbers[h],bg="black",fg="white").pack(side=LEFT,padx=5)
     #frame9
     frame9=Frame(frame,pady=5)
     frame9.pack()
     for i in range(81,91):
          Label(frame9,text=Numbers[i],bg="black",fg="white").pack(side=LEFT,padx=5)
     #frame10
     frame10=Frame(frame)
     frame10.pack()
     for j in range(91,101):
          Label(frame10,text=Numbers[j],bg="black",fg="white").pack(side=LEFT,padx=6)
     


     
root=Tk()
root.title("Snake And Ladder")
root.geometry("310x480")
#root.minsize(400,460)
root.maxsize(310,480)
#header
header=Frame(root,pady=2,bg="black")
header.pack(side=TOP)
Label(header,text="Snake And Leadder",font="20",bg="orange",width=100).pack()
#frame
frame=Frame(root,bg="pink",pady=10)
frame.pack()
screen()
#footer
footer=Frame(root,bg="black",pady=2)
footer.pack()
Label(footer,bg="orange",width=100).pack()
#monitorframe
dicemon=IntVar()
monitorframe=Frame(root)
monitorframe.pack()
position_mon_variable=StringVar()
positionmonitor=Entry(root,textvariable=position_mon_variable)
positionmonitor.pack()
dice_count_monitor=Entry(root,textvariable=dicemon)
dice_count_monitor.pack()

Button(root,text="roll",command=dice).pack()
root.mainloop()

