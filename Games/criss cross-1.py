


from tkinter import*



root=Tk()
root.title("Criss Cross")
root.geometry("300x400")
root.maxsize(300,400)
root.minsize(300,400)
#header
header=Frame(root)
header.pack(fill="x",side=TOP)
Label(header,text="Criss Cross",fg="white",font="20", bg="magenta",height=3).pack(fill="x")
Label(header,text="",bg="black").pack(fill="x")
#-----------------------------------------------------------------------------------------------------------------------------------------------------
#game_frame
game_frame=Frame(root)
game_frame.pack(fill="x",side=TOP)
#left_margin
left_margin=Frame(game_frame,width=3)
left_margin.pack(fill="y",side=LEFT)
Label(left_margin,bg="black",height=17,width=3).pack(side=LEFT)
#right_margin
right_margin=Frame(game_frame,width=3)
right_margin.pack(fill="y",side=RIGHT)
Label(right_margin,bg="black",height=17,width=3).pack(side=RIGHT)
#------------------------------------------------------------------------------------------------------------------------------------------------------
#game_box
game_box=Frame(game_frame)
game_box.pack()
Label(game_box,text="anurag").pack()



#footer
footer=Frame(root)
footer.pack(side=BOTTOM,fill="x")
Label(footer,text="",bg="black").pack(fill="x",side=TOP)
Label(footer,text="",bg="magenta",height=3).pack(fill="x",side=BOTTOM)
root.mainloop()
