from tkinter import*
#database()
#sign_up()
#condition()



#________________________________database_________________________________________________________________________
def sign_up():
    '''alpha=input("Name:")
    beta=input("Password :")
    gamma=input("confirm password:")
    a=input("wanna confirm?(enter 'Yes' or 'No')")
    sign_up_counter=0
    while sign_up_counter==0:
        if a=="Yes":
            Database_1.append(alpha)
            Database_2.append(beta)
            Database_3.append(gamma)
            sign_up_counter=sign_up_counter+1
            print("User No=",sign_up_counter)
        elif a=="No":
            print("account was not created")
        else:
            print("wrong input")'''
            
def database():
    Database_1=[]
    Database_2=[]
    Database_3=[]

#___________________________________________________________________________

def text():
    text=Label(text='''alpha=input("Name:")
    beta=input("Password :")
    gamma=input("confirm password:")
    a=input("wanna confirm?(enter 'Yes' or 'No')")
    sign_up_counter=0
    while sign_up_counter==0:
        if a=="Yes":
            Database_1.append(alpha)
            Database_2.append(beta)
            Database_3.append(gamma)
            sign_up_counter=sign_up_counter+1
            print("User No=",sign_up_counter)
        elif a=="No":
            print("account was not created")
        else:
            print("wrong input")''')
    text.pack()
    

    
#______________________________tkinter Gui______________________________________________________

def screen_size():
    root=Tk()
    root.title("Mind Slinger")
    root.geometry("400x500")
    root.minsize(200,250)
    
    text()
    root.mainloop()

screen_size()










