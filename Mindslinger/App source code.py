from tkinter import*
import webbrowser
from tkinter.messagebox import showinfo
from tkinter import filedialog
#Database
Userdata=["Anurag"]
Passdata=["anurag"]
Useradmin_no=["0804"]
Userclass=["11"]

#signup_________________________________________________________________________________________________
def sign_up():
     def sign__up():
          for widget in dframe.winfo_children():
               widget.destroy()
          if sname.get()=="":
               a="Please enter a user name"
          elif sname.get()  in Userdata:
               a="User Name is Already Taken"
          else:
               if spass1.get()!=spass2.get():
                    a="Please Enter The Same Password"
               elif spass1.get()=="":
                    a="Please Create A Password"
               elif spass1.get()==spass2.get():
                    Userdata.append(sname.get())
                    Passdata.append(spass1.get())
                    a="Account Created Sucessfully"
          Label(dframe,text=a,fg="red").pack()
     
     sign_root=Toplevel()
     sign_root.geometry("344x484")
     sign_root.title("Sign Up")
     sign_root.maxsize(344,484)
     sign_root.iconbitmap("favicon_1.ico")
     
    
     #frame
     frame=Frame(sign_root,padx=8)
     frame.pack()
     logo=PhotoImage(file="Logo-Mind Slinger.png")
     Label(frame,image=logo).pack()
     #frame1
     frame1=Frame(sign_root,pady=10)
     frame1.pack()
     Label(frame1,text="User Name :").pack(side=TOP,anchor="nw")
     global sname
     sname=StringVar()
     Sign_name=Entry(frame1,textvariable=sname)
     Sign_name.pack(side=BOTTOM,anchor="sw")
     #frame2
     frame2=Frame(sign_root,pady=10)
     frame2.pack()
     Label(frame2,text="Password :").pack(side=TOP,anchor="nw")
     spass1=StringVar()
     Sign_pass1=Entry(frame2,textvariable=spass1)
     Sign_pass1.pack(side=BOTTOM,anchor="sw")
     #frame3
     frame3=Frame(sign_root,pady=10)
     frame3.pack()
     Label(frame3,text="Confirm Password :").pack(side=TOP,anchor="nw")
     spass2=StringVar()
     Sign_pass1=Entry(frame3,textvariable=spass2)
     Sign_pass1.pack(side=BOTTOM,anchor="sw")
     #frame4
     def login_sign():
         ''' if sname.get() in Userdata:
               for a in Userdata:
                    if sname.get()==a:
                         b=Userdata.index(a)
                         if Passdata[b]==spass2.get():
                              mindslingersignpro()
                         elif Passdata[b]!=spass2.get():
                              Label(dframe,text="Password Is Incorrect",fg="red").pack()
          
          else:
                    Label(dframe,text="Account Not Found ! Create An account before login in",fg="red").pack()'''
         User_name.set(sname.get())
         user_pass.set(spass1.get())
         sign_root.destroy()#undestroy sig_root
         log_in()
     frame4=Frame(sign_root,pady=10)
     frame4.pack()
     Button(frame4,text="Sign Up",command=sign__up).pack(side=LEFT,padx=5)
     Button(frame4,text="log In",command=login_sign).pack(side=LEFT,padx=5)
     #Display frame
     dframe=Frame(sign_root)
     dframe.pack()
     
     sign_root.mainloop()

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#profile
def procode():
     pro=Toplevel()
     Title=User_name.get()+" Profile"
     pro.title(Title)
     pro.iconbitmap("favicon_1.ico")
     pro.geometry("455x644")

     #updatedata
     def update_data():
          for widget in workarea.winfo_children():
               widget.destroy()
          #pframe
          pframe=Frame(workarea)
          pframe.pack()
          pname=StringVar()
          Label(pframe,text="Name :").pack(side=TOP,anchor="nw")
          name_entry=Entry(pframe,textvariable=pname)
          name_entry.pack(side=BOTTOM)
          #pframe1
          pframe1=Frame(workarea,pady=5)
          pframe1.pack()
          padmin=StringVar()
          Label(pframe1,text="Admin No :").pack(side=TOP,anchor="nw")
          name_entry=Entry(pframe1,textvariable=padmin)
          name_entry.pack(side=BOTTOM)
          #pframe2
          pframe2=Frame(workarea,pady=5)
          pframe2.pack()
          Label(pframe2,text="Class :").pack(side=TOP,anchor="nw")
          pclass=StringVar()
          namess=Entry(pframe2,textvariable=pclass)
          namess.pack(side=BOTTOM)
          #update_it
          def update_it():
               for widget in pframe4.winfo_children():
                    widget.destroy()
               a=Userdata.index(User_name.get())
               if pname.get()=="":
                    Label(pframe4,text="Please Enter Name",fg="red").pack()
               elif padmin.get()=="":
                    Label(pframe4,text="Please Enter Admin No,",fg="red").pack()
               elif pclass.get()=="":
                    Label(pframe4,text="Please Enter Class",fg="red").pack()
               else:
                    Userdata[a]==pname.get()
                    Useradmin_no[a]==padmin.get()
                    Userclass[a]==pclass.get()
                    Label(pframe4,text="Your Data Is Updated",fg="red").pack()
          #pframe3
          pframe3=Frame(workarea,pady=10)
          pframe3.pack()
          Button(pframe3,text="Update",command=update_it).pack()
          #pframe4
          pframe4=Frame(workarea)
          pframe4.pack()
          
     #userdata
     def showdata():
          for widget in workarea.winfo_children() :
               widget.destroy()
          a=Userdata.index(User_name.get())
           #pframe
          pframe=Frame(workarea)
          pframe.pack()
          pname=StringVar()
          Label(pframe,text="Name :").pack(side=TOP,anchor="nw")
          name_entry=Entry(pframe,textvariable=pname)
          name_entry.pack(side=BOTTOM)
          #pframe1
          pframe1=Frame(workarea,pady=5)
          pframe1.pack()
          padmin=StringVar()
          Label(pframe1,text="Admin No :").pack(side=TOP,anchor="nw")
          name_entry=Entry(pframe1,textvariable=padmin)
          name_entry.pack(side=BOTTOM)
          #pframe2
          pframe2=Frame(workarea,pady=5)
          pframe2.pack()
          Label(pframe2,text="Class :").pack(side=TOP,anchor="nw")
          pclass=StringVar()
          namess=Entry(pframe2,textvariable=pclass)
          namess.pack(side=BOTTOM)
          #set data
          pname.set(Userdata[a])
          padmin.set(Useradmin_no[a])
          pclass.set(Userclass[a])
     def online_class():
          showinfo("Online Class","You Have No Online Class At This Moment")
     def elearn():
          webbrowser.open("https://www.youtube.com")
     def notes():
          webbrowser.open("https://mindslingeranu1.blogspot.com")
     def uploadwork():
          for widget in workarea.winfo_children():
               widget.destroy()
          #uframe
          uframe=Frame(workarea)
          uframe.pack()
          Label(uframe,text="Subject Name :").pack(side=LEFT)
          En=Entry(uframe)
          En.pack(side=LEFT)
          #uframe1
          uframe1=Frame(workarea,pady=5)
          uframe1.pack()
          
          def Open():
               pro.filename=filedialog.askopenfilename(initialdir="",title="open",filetypes=(("pdf files",'*.pdf'),('all files','*.*')))
          def submit():
               for widget in uframe2.winfo_children():
                    widget.destroy()
               Label(uframe2,text="file Submited",fg="red").pack()
          Button(uframe1,text="Open",command=Open).pack(side=LEFT,padx=5)
          Button(uframe1,text="Submit",command=submit).pack(side=LEFT)
          #uframe2
          uframe2=Frame(workarea,pady=5)
          uframe2.pack()
     def Doubt():
          for widget in workarea.winfo_children():
               widget.destroy()
          #uframe
          uframe=Frame(workarea)
          uframe.pack()
          Label(uframe,text="Subject : ").pack(side=LEFT)
          En=Entry(uframe)
          En.pack(side=LEFT)
          #uframe1
          uframe1=Frame(workarea,pady=5)
          uframe1.pack()
          Label(uframe1,text="Doubt   : ").pack(side=LEFT)
          En2=Entry(uframe1)
          En2.pack(side=LEFT)
          #Submit
          def Submit():
               for widget in uframe3.winfo_children():
                    widget.destroy()
               Label(uframe3,text="Your Doubt Was Sent",fg="red").pack()
          #uframe2
          uframe2=Frame(workarea)
          uframe2.pack()
          Button(uframe2,text="Submit",command=Submit).pack()
          #uframe3
          uframe3=Frame(workarea)
          uframe3.pack()
     def give_exam():
          showinfo("Give Exam","You Have No Sheduled Exam At This Moment")
     def syllabus():
          showinfo("Syllabus","You Have No Exam Syllabus At This Moment")
     def timetable():
          showinfo("Time Table","You Have No Sheduled Exam Time Table At This Moment")
     def feedetails():
          showinfo("Fee Details","Contact Office")
     def feepayment():
          webbrowser.open("https://erp.dpsmohanapurgkpedu.in/parents/default.aspx")
     def notice():
          showinfo("Notice","You Are All Caught up")
     def passchange():
          for widget in workarea.winfo_children():
               widget.destroy()
          #uframe
          uframe=Frame(workarea)
          uframe.pack()
          Label(uframe,text="User Name").pack(side=TOP,anchor="nw")
          usname=StringVar()
          En=Entry(uframe,textvariable=usname)
          En.pack(side=BOTTOM)
          #uframe1
          uframe1=Frame(workarea,pady=5)
          uframe1.pack()
          Label(uframe1,text="Password").pack(side=TOP,anchor="nw")
          cupass=StringVar()
          En1=Entry(uframe1,textvariable=cupass)
          En1.pack()
          #uframe2
          uframe2=Frame(workarea,pady=5)
          uframe2.pack()
          Label(uframe2,text="New Password").pack(side=TOP,anchor="nw")
          nowpass=StringVar()
          En3=Entry(uframe2,textvariable=nowpass)
          En3.pack(side=BOTTOM)
          #uframe3
          uframe3=Frame(workarea,pady=5)
          uframe3.pack()
          #changepassword
          def changepassword():
               if usname.get() not in Userdata:
                    a="Please Enter A Valid User Name"
               elif usname.get() in Userdata:
                    b=Userdata.index(usname.get())
                    if cupass.get()==Passdata[b]:
                         Passdata[b]=nowpass.get()
                         a="Password Changed Sucessfully"
                    else:
                         a="Wrong Password !"
               for widget in uframe4.winfo_children():
                    widget.destroy()
               Label(uframe4,text=a,fg="red").pack()
                         
          Button(uframe3,text="Change Password",command=changepassword).pack()
          #uframe4
          uframe4=Frame(workarea,pady=5)
          uframe4.pack()
     #---------------------------------------------------------------------------------------------------------     
     #menu
     menubar=Menu(pro)
     #Account data
     Us_data=Menu(menubar,tearoff=0)
     Us_data.add_command(label="About Me",command=showdata)
     Us_data.add_command(label="Update Data",command=update_data)
     menubar.add_cascade(menu=Us_data,label="User Data")
     #online Class
     Liveclass=Menu(menubar,tearoff=0)
     Liveclass.add_command(label="Online Class",command=online_class)
     Liveclass.add_command(label="E-Learn Videos",command=elearn)
     Liveclass.add_command(label="Upload Class Work",command=uploadwork)
     Liveclass.add_command(label="Doubt/Query",command=Doubt)
     Liveclass.add_command(label="Notes",command=notes)
     menubar.add_cascade(menu=Liveclass,label="Classes")
     #Examination
     Examination=Menu(menubar,tearoff=0)
     Examination.add_command(label="Give Exam",command=give_exam)
     Examination.add_command(label="Syllabus",command=syllabus)
     Examination.add_command(label="Time Table",command=timetable)
     menubar.add_cascade(menu=Examination,label="Examination")
     #fee
     Fee=Menu(menubar,tearoff=0)
     Fee.add_command(label="Fee Details",command=feedetails)
     Fee.add_command(label="Fee Payment",command=feepayment)
     menubar.add_cascade(menu=Fee,label="Fee")
     #notice
     menubar.add_cascade(label="Notice",command=notice)
     #Settings
     Settings=Menu(menubar,tearoff=0)
     Settings.add_command(label="Change Password",command=passchange)
     menubar.add_cascade(menu=Settings,label="Settings")
     menubar.add_command(label="Exit")
     pro.config(menu=menubar)
     #menu Ends
     #display
     pframe=Frame(pro,)
     pframe.pack()
     photo=PhotoImage(file="Logo-Mind Slinger.png")
     Label(pframe,image=photo).pack()
     #workarea
     workarea=Frame(pro)
     workarea.pack()
     
     #bottom
     bframe=Frame(pro)
     bframe.pack(side=BOTTOM)
     Label(bframe,text=" ",bg="white",padx=455).pack()

     pro.mainloop()

     


def mindslingersignpro():
     procode()
#________________________________________________________________________________________________________________________
#LoginWindow
root=Tk()
root.title("Mindslinger")
root.iconbitmap("favicon_1.ico")
root.geometry("344x444")
root.maxsize(344,444)
#frame
frame=Frame(root)
frame.pack()
Photo=PhotoImage(file="Logo-Mind Slinger.png")
image=Label(frame,image=Photo)
image.pack(side=LEFT)
#frame1
frame1=Frame(root)
frame1.pack()
Label(frame1,text="Log In",font="10").pack()

#frame2
frame2=Frame(root,pady=10)
frame2.pack()
User_name=StringVar()
Label(frame2,text="User Name :").pack(side=LEFT)
Username=Entry(frame2,textvariable=User_name)
Username.pack(padx=10)

#frame3
frame3=Frame(root,pady=10)
frame3.pack()
user_pass=StringVar()
Label(frame3,text="Password   :").pack(side=LEFT)
Password=Entry(frame3,textvariable=user_pass)
Password.pack(side=LEFT,padx=10)

#frame4
def log_in():
     for remove in frame5.winfo_children():
          remove.destroy()
     if User_name.get() in Userdata:
          for a in Userdata:
               if User_name.get()==a:
                    b=Userdata.index(a)
               else:
                    pass
          if Passdata[b]==user_pass.get():
               procode()
          elif user_pass.get()=="":
               Label(frame5,text="Please enter your password",fg="red").pack()
          else:
                Label(frame5,text="Incorrect Password",foreground="red").pack()
               
     elif User_name.get()=="":
          Label(frame5,text="Please enter a User name",fg="red").pack()
     else:
                    Label(frame5,text="No  User name Found", foreground="red").pack()
   
frame4=Frame(root,pady=10)
frame4.pack()
Button(frame4,text="Log In",command=log_in).pack(side=LEFT,padx=5)
Button(frame4,text="Sign Up",command=sign_up).pack(side=LEFT,padx=5)

#frame5 (the error frame)
frame5=Frame(root,pady=10)
frame5.pack()

root.mainloop()

#_____________________________________________________________________________________________________________________

