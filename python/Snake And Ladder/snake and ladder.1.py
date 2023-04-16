from tkinter import*
root=Tk()
#frame9
frame9=Frame(root)
frame9.pack()
for b in range(91,101):
     Label(frame9,text=b).pack(side=LEFT)
#frame8
frame8=Frame(root)
frame8.pack()
for b in range(81,91):
     Label(frame8,text=b).pack(side=LEFT)
#frame7
frame7=Frame(root)
frame7.pack()
for b in range(71,81):
     Label(frame7,text=b).pack(side=LEFT)
#frame6
frame6=Frame(root)
frame6.pack()
for b in range(61,71):
     Label(frame6,text=b).pack(side=LEFT)
#frame5
frame5=Frame(root)
frame5.pack()
for b in range(51,61):
     Label(frame5,text=b).pack(side=LEFT)
#frame4
frame4=Frame(root)
frame4.pack()
for b in range(41,51):
     Label(frame4,text=b).pack(side=LEFT)
#frame3
frame3=Frame(root)
frame3.pack()
for b in range(31,41):
     Label(frame3,text=b).pack(side=LEFT)
#frame2
frame2=Frame(root)
frame2.pack()
for b in range(21,31):
     Label(frame2,text=b).pack(side=LEFT)
#frame1
frame1=Frame(root)
frame1.pack()
for b in range(11,21):
     Label(frame1,text=b).pack(side=LEFT)
#frame
L=["1  ","2  ","3  ","4  ","5  ","6  ","7  ","8  ","9  ","10"]
frame=Frame(root)
frame.pack()
for b in range(0,10):
     Label(frame,text=L[b]).pack(side=LEFT)
          
root.mainloop()
