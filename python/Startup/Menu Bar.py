from tkinter import *

def file():
    print("hi")


#file functions
def new():
    print()
def save():
    print()
def save_as():
    print()
def Print():
    print()



#Edit functions
def undo():
    print()
def redo():
    print()
def cut():
    print()
def copy():
    print()
def paste():
    print()
def select_all():
    print()


#View functions
def zoom():
    print()


#Help functions
def send_feedback():
    print()
def about():
    print()

#_________________________________________________________________
root=Tk()

#main menu code start from here
Menu_=Menu(root)
#File
File=Menu(Menu_,tearoff=0)
File.add_command(label="New",command=new)
File.add_command(label="Open",command=open)
File.add_command(label="Save",command=save)
File.add_command(label="Save As",command=save_as)
File.add_command(label="Print",command=Print)
File.add_separator()
File.add_command(label="Exit",command=quit)
#Edit
Edit=Menu(Menu_,tearoff=0)
Edit.add_command(label="Undo",command=undo)
Edit.add_command(label="Redo",command=redo)
Edit.add_command(label="Cut",command=cut)
Edit.add_command(label="Copy",command=copy)
Edit.add_command(label="Paste",command=paste)
Edit.add_command(label="Select All",command=select_all)
#View
View=Menu(Menu_,tearoff=0)
View.add_command(label="Zoom",command=zoom)
#Help
Help=Menu(Menu_,tearoff=0)
Help.add_command(label="View Help",command=help)
Help.add_command(label="Send Feedback",command=send_feedback)
Help.add_separator()
Help.add_command(label="About",command=about)

root.config(menu=Menu_)
Menu_.add_cascade(label="File",menu=File)
Menu_.add_cascade(label="Edit",menu=Edit)
Menu_.add_cascade(label="View",menu=View)
Menu_.add_cascade(label="Help",menu=Help)

#main menu code ends here
root.mainloop()
