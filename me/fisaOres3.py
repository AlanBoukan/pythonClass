import turtle
import math
import tkinter as tk

t1 = turtle.Turtle()

def makeShape():
    t1.goto(0,0)
    t1.clear()

    # First side
    zela1 = int(forwardLen1.get())
    zela2 = int(forwardLen2.get())

    t1.forward(zela1)
    t1.write("sideLen1: " + str(zela1))

    # Second side
    t1.left(90)
    t1.forward(zela2)
    t1.write("sideLen2: " + str(zela2))

    # Hypotenuse length
    forwardLen3 = math.sqrt(zela1**2 + zela2**2)
    vatar.configure(text="وتر : " + str(forwardLen3))

    # Draw hypotenuse back to origin
    t1.goto(0,0)
    t1.write("sideLen3: " + str(round(forwardLen3,2)))

root = tk.Tk()
root.title("رسم مثلث قاعم")

tk.Label(root, text="اندازه ی طول 1 :").grid(row=0, column=0)
forwardLen1 = tk.Entry(root)
forwardLen1.grid(row=0, column=1)

tk.Label(root, text="اندازه ی طول 2 :").grid(row=1, column=0)
forwardLen2 = tk.Entry(root)
forwardLen2.grid(row=1, column=1)

vatar = tk.Label(root, text="وتر :")
vatar.grid(row=2, column=0)

tk.Button(root, text="محاسبه وتر", command=makeShape).grid(row=4, column=1)

root.mainloop()
