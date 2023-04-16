from tkinter import *
from tkinter import ttk
import threading
import random
import time


#list
text=["cracking...","attempt failed ! /n Restarting..."]

def pro():
     threading.Thread(target=leftframedisplays).start()
     threading.Thread(target=ed).start()
def ed():
     for e in range(100):
          progress1.configure(value=random.randint(0,100))
          root.update_idletasks()
          time.sleep(0.05)
          progress2.configure(value=random.randint(0,100))
          root.update_idletasks()
          time.sleep(0.05)
          progress3.configure(value=random.randint(0,100))
          root.update_idletasks()
          time.sleep(0.05)
#leftframesdislpay()
def leftframedisplays():
     Label(leftframe,text="Selecting Target...",fg="green",bg="Black").pack(anchor="nw")
     root.update_idletasks()
     time.sleep(1)
     hack.configure(value=10)
     Label(leftframe,text=userentry.get(),fg="red",bg="black").pack(anchor="nw")
     root.update_idletasks()
     time.sleep(1)
     hack.configure(value=20)
     Label(leftframe,text="Starting Engine...",fg="green",bg="black").pack(anchor="nw")
     root.update_idletasks()
     time.sleep(1)
     hack.configure(value=30)
     Label(leftframe,text="importing Hacked...",fg="red",bg="black").pack(anchor="nw")
     root.update_idletasks()
     time.sleep(1)
     hack.configure(value=50)
     for a in range(15):
          b=random.randint(0,1)
          if b==0:
               Label(leftframe,text=text[b],fg="green",bg="black").pack(anchor="nw")
               root.update_idletasks()
               time.sleep(1)
          else:
               Label(leftframe,text=text[b],fg="red",bg="black").pack(anchor="nw")
               root.update_idletasks()
               time.sleep(1)
     Label(leftframe,text="cracking...",fg="green",bg="black").pack(anchor="nw")
     root.update_idletasks()
     time.sleep(1)
     hack.configure(value=70)
     Label(leftframe,text="Target cracked !/n loging in...",fg="yellow",bg="black").pack(anchor="nw")
     root.update_idletasks()
     time.sleep(1)
     hack.configure(value=100)
      
     
     
#window
root=Tk()
root.configure(bg="black")
root.geometry("600x500")
root.title("Active Meter")
#upframe
#upframe=Frame(root)
#upframe.pack()
downframe=Frame(root)
downframe.pack()
hack=ttk.Progressbar(downframe,orient="horizontal",length=600,mode="determinate")
hack.pack()


#leftframe
leftframe=Frame(root,bg="black",width=200,height=300)
leftframe.pack(side=LEFT,fill="y")

#rightframe
rightframe=Frame(root,bg="black",width=200,height=300)
rightframe.pack(side=RIGHT,fill="y")
rframe=Frame(rightframe,bg="black",pady=50)
rframe.pack()
Label(rframe,text="User Name :",fg="green",bg="black").pack(side=LEFT)
userentry=StringVar()
username=Entry(rframe,textvariable=userentry)
username.pack(side=RIGHT)
rframe1=Frame(rightframe)
rframe1.pack()
Button(rframe1,text="Crack",command=pro,bg="black",fg="green",padx=5).pack(side=LEFT)
Button(rframe1,text="Quit",bg="black",fg="green",padx=5).pack(side=RIGHT)
rframe2=Frame(rightframe,pady=40,bg="black")
rframe2.pack()
progress1=ttk.Progressbar(rframe2,orient="vertical",length=250,mode="indeterminate")
progress1.pack(side=LEFT,padx=10)
progress2=ttk.Progressbar(rframe2,orient="vertical",length=250,mode="indeterminate")
progress2.pack(side=LEFT,padx=10)
progress3=ttk.Progressbar(rframe2,orient="vertical",length=250,mode="indeterminate")
progress3.pack(side=LEFT,padx=10)

root.mainloop()
