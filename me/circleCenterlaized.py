# دواير متحد المرکز

import turtle
import tkinter as tk

def makePatern():
    
    t1=turtle.Turtle()
    r=int(radiousCircle.get())    
    n=int(numCircles.get())
    dest=r/n
    for i in range (n):
        newDest=dest*i
        newR=r-newDest
        t1.penup()
        t1.goto(0,newDest)
        t1.pendown()
        t1.circle(newR)

# make shape
root=tk.Tk()
root.title("make centerlized circles")

tk.Label(root, text="please insert the number of circles:").grid(row=0, column=0)
numCircles=tk.Entry(root)
numCircles.grid(row=0, column=1)

tk.Label(root, text="please insert the first radious of circle: ").grid(row=1, column=0)
radiousCircle=tk.Entry(root)
radiousCircle.grid(row=1, column=1)

tk.Button(root, text="make Shape", command=makePatern).grid(row=2, column=1)


#tk.Label(root, text="please insert the widget of circles:").grid(row=3, column=0)
#numCircles=tk.Canvas(root)
#numCircles.grid(row=3, column=1)
#tk.Button(root, text="make Shape", command=makePatern).grid(row=3, column=1)


root.mainloop()



