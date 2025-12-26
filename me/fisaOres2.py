import turtle
import math
import tkinter as tk
t1 = turtle.Turtle()

def makeShape():
    t1.goto(0,0)
    t1.clear()
    # First side
    zela1 = int (forwardLen1.get())
    zela2= int (forwardLen2.get())
    # v= int (forwardLen3.get())
    t1.forward(zela1)
    t1.write("sideLen1: " + str(zela1))
    
    # Second side
    t1.left(90)
    t1.forward(zela2)
    t1.write("sideLen2: " + str(zela2))
    
    # Turn by given degree
    # t1.left(degre)
    
    # Add some spacing before writing the angle
    # t1.penup()          # lift pen so it doesn’t draw a line
    forwardLen3 = math.sqrt(zela1**2 + zela2**2)
    vatar.configure(text="وتر: " + str(forwardLen3))
    t1.goto(0,0)    # t1.forward(20)      # move forward a bit to create space
    # t1.pendown()        # put pen back down
    # t1.write("internalAngle: " + str(90))
    
    # Compute the third side using Pythagorean theorem
    
    # 
    
    # Draw the third side
    # t1.forward(forwardLen3)
    # t1.write("sideLen3: " + str(forwardLen3))
    
    # return forwardLen3
root = tk.Tk()
root.title("رسم مثلث قاعم")

tk.Label(root, text="اندازه ی طول 1 :").grid(row=0, column=0)
forwardLen1 = tk.Entry(root)
forwardLen1.grid(row=0, column=1)

tk.Label(root, text="اندازه ی طول 2 :").grid(row=1, column=0)
forwardLen2 = tk.Entry(root)
forwardLen2.grid(row=1, column=1)

vatar=tk.Label(root, text="وتر :") 
vatar.grid(row=2, column=0)
# vatar = tk.Entry(root)
# vatar.grid(row=2, column=1)



tk.Button(root, text=" محاسبه وتر", command=makeShape).grid(row=4, column=1)

root.mainloop()
tk.Frame


