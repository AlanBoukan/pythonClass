#make any shape with tkinter windows
import turtle
import tkinter as tk
t1 = turtle.Turtle()
def refresh(self):
    self.destroy()
    self.__init__()
def makeShape(tedadZela, forwardLen):
    degre=360/tedadZela
    for i in range(tedadZela):
        t1.forward(forwardLen)
        t1.left(degre)
    
def makePattern():
    t1.clear()
    forwardLen = int(andazehZela.get())       # اندازه ي يک صلع
    numShape = int(numShapes.get())         # تعداد شکل
    numZela=int(numZels.get())
    pen_w = int(penWidth.get())       # ضخامت قلم
    color = colorChoice.get()         # رنگ انتخابی
    
    t1.pensize(pen_w)
    t1.color(color)
    t1.speed(5)
    dest = (forwardLen/2)/ numShape
    for i in range(numShape):
        newDest = dest * i
        newforwardLen = forwardLen - (newDest*2)
        t1.penup()
        t1.goto(newDest, newDest)
        t1.pendown()
        makeShape(numZela, newforwardLen)

# رابط کاربری
root = tk.Tk()
root.title("رسم اشکال متحد المرکز")

tk.Label(root, text="تعداد شکل").grid(row=0, column=0)
numShapes = tk.Entry(root)
numShapes.grid(row=0, column=1)

tk.Label(root, text="تعداد صلع").grid(row=1, column=0)
numZels = tk.Entry(root)
numZels.grid(row=1, column=1)

tk.Label(root, text="اندازه  يک ظلع").grid(row=2, column=0)
andazehZela = tk.Entry(root)
andazehZela.grid(row=2, column=1)

tk.Label(root, text="ضخامت قلم:").grid(row=3, column=0)
penWidth = tk.Scale(root, from_=1, to=10, orient="horizontal")
penWidth.grid(row=3, column=1)

tk.Label(root, text="رنگ دایره‌ها:").grid(row=4, column=0)
colorChoice = tk.StringVar(root)
colorChoice.set("red")  # مقدار پیش‌فرض
colors = ["red", "blue", "green", "black", "purple", "orange", "yellow", "pink", "gold", "gray", "brown"]
tk.OptionMenu(root, colorChoice, *colors).grid(row=4, column=1)


tk.Button(root, text="رسم شکل", command=makePattern).grid(row=5, column=1)

root.mainloop()
