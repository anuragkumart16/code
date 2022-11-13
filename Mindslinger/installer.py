from tkinter import *
from tkinter import ttk
import threading
import time

a=1
def cancekl():
     root.destroy()
def upnext():
     threading.Thread(target=yo).start()
     for c in nextframe.winfo_children():
          c.destroy()
     nextbutton=Button(nextframe,text=" Next ",command=upnext).pack(side=RIGHT)
     cancelbutton=Button(nextframe,text="Cancel",command=cancekl).pack(side=RIGHT,padx=3)
def yo():
     global a
     if a ==1:
          for b in frame1.winfo_children():
               b.destroy()
          Label(frame1,text="Welcome to Mind Slinger's App installer.").pack(anchor="nw")
          Label(frame1,text="Press Next to continue...").pack(anchor="nw")
          
          a=a+1
     elif a==2:
          for b in frame1.winfo_children():
               b.destroy()
          Label(frame1,text="Welcome to Mind Slinger's App installer.").pack(anchor="nw")
          Label(frame1,text=" ").pack(anchor="nw")
          Label(frame1,text="Status : Checking system requirements").pack(anchor="nw",pady=5)
          progress=ttk.Progressbar( frame1, orient="horizontal", length=210,mode="determinate",value=10)
          progress.pack(anchor="nw",padx=3)
          root.update_idletasks()
          time.sleep(5)
          
          for b in frame1.winfo_children():
               b.destroy()
          Label(frame1,text="Welcome to Mind Slinger's App installer.").pack(anchor="nw")
          Label(frame1,text=" ").pack(anchor="nw")
          Label(frame1,text="Status : Copying packages...").pack(anchor="nw",pady=5)
          progress=ttk.Progressbar( frame1, orient="horizontal", length=210,mode="determinate",value=40)
          progress.pack(anchor="nw",padx=3)
          root.update_idletasks()
          time.sleep(3)
          for b in frame1.winfo_children():
               b.destroy()
          Label(frame1,text="Welcome to Mind Slinger's App installer.").pack(anchor="nw")
          Label(frame1,text=" ").pack(anchor="nw")
          Label(frame1,text="Status : Finishing up...").pack(anchor="nw",pady=5)
          progress=ttk.Progressbar( frame1, orient="horizontal", length=210,mode="determinate",value=70)
          progress.pack(anchor="nw",padx=3)
          root.update_idletasks()
          time.sleep(2)
          progress.configure(value=100)
          root.update_idletasks()
          time.sleep(1)
          for b in frame1.winfo_children():
               b.destroy()
          Label(frame1,text="App successfully installed !").pack(anchor="nw")
          Label(frame1).pack(anchor="nw")
          Label(frame1,text="Press next to launch the application").pack(anchor="nw")
          a=a+1
     else:
          import App_source_code
          
          
          
          
          
          

     
     

     
root=Tk()
root.title("SQL Installer")
root.iconbitmap("favicon_2.ico")
root.geometry("550x300")

upframe=Frame(root)
upframe.pack()

frame=Frame(upframe)
frame.pack(side=LEFT,padx=30,fill="y")
logo=PhotoImage(file="Logo-Mind Slinger1.png")
Label(frame,image=logo).pack()

frame1=Frame(upframe,padx=30,pady=60)
frame1.pack(side=RIGHT,fill="y")
'''progress=ttk.Progressbar(frame1, orient="horizontal", mode="determinate",length=300)
progress.pack()'''
Label(frame1,text="Welcome to Mind Slinger's App installer.").pack(anchor="nw")
Label(frame1,text="Thanks for choosing us..").pack(anchor="nw")
Label(frame1,text="In order to continue click next...").pack(anchor="nw")
nextframe=Frame(root,padx=5,pady=3)
nextframe.pack(side=BOTTOM,fill="x")

nextbutton=Button(nextframe,text=" Next ",command=upnext).pack(side=BOTTOM,anchor="se")






root.mainloop()
