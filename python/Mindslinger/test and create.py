from tkinter import*
from tkinter.messagebox import showinfo
import webbrowser
from tkinter import filedialog
Userdata=["Anurag"]
Userpass=["anurag"]
Useradmin_no=["0804"]
Userclass=["11"]
User_name="Anurag"
def procode():
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
               a=Userdata.index(User_name)
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
          a=Userdata.index(User_name)
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
                    if cupass.get()==Userpass[b]:
                         Userpass[b]=nowpass.get()
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
     menubar.add_command(label="Exit",command=exit)
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

     
                              





sname="Anurag"
sname=sname+"-profile"
pro=Tk()
pro.iconbitmap("favicon_1.ico")
pro.title(sname)
pro.geometry("455x644")
pro.maxsize(455,644)
procode()

pro.mainloop()
