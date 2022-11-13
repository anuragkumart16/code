from tkinter import*
root=Tk()
width=400
height=500
root.geometry(f"{width}x{height}")
cv=Canvas(root,width=width,height=height).pack()
cv.create_line(0,0,800,200)
root.mainloop()
