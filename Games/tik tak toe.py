from tkinter import *
import random


def window():
    root.geometry("235x100")
    root.title("Tik Tak Toe")


turn = 'X'
board = [' ', ' ', ' ',
         ' ', ' ', ' ',
         ' ', ' ', ' ' ]

def display_board():
  
  Button(text=board[0],width=5).grid(column=1,row=1)
  Button(text=board[1],width=5).grid(column=2,row=1)
  Button(text=board[2],width=5).grid(column=3,row=1)
  
  Button(text=board[3],width=5).grid(column=1,row=2)
  Button(text=board[4],width=5).grid(column=2,row=2)
  Button(text=board[5],width=5).grid(column=3,row=2)
  
  Button(text=board[6],width=5).grid(column=1,row=3)
  Button(text=board[7],width=5).grid(column=2,row=3)
  Button(text=board[8],width=5).grid(column=3,row=3)


Alpha=["Choose Any Position from 1 to 9","Oops!,The \nPosition Is \nAlready Taken","Bot's Turn","Your Turn"]
def monitor():
    Label(text=Alpha[1],background="black",foreground="white").grid(column=4)


def mainmenu():
    mainmenu=Menu(root)
    #new game
    mainmenu.add_command(label='New Game',command=newgame)
    #difficulty
    Difficulty=Menu(mainmenu,tearoff=0)
    Difficulty.add_command(label="Easy",command=difficulty_easy)
    Difficulty.add_command(label="Medium",command=difficulty_medium)
    Difficulty.add_command(label="Hard",command=difficulty_hard)
    mainmenu.add_cascade(menu=Difficulty,label="Difficulty")
    #Multiplayer
    mainmenu.add_command(label="Multiplayer",command=multiplayer)
    #Exit
    mainmenu.add_command(label="Quit",command=quit)
    root.config(menu=mainmenu)
    
def newgame():
        print()
def difficulty_easy():
    print()
def difficulty_medium():
    print()
def difficulty_hard():
    print()
def multiplayer():
    print()

root=Tk()
window()
mainmenu()
display_board()
monitor()
root.mainloop()
