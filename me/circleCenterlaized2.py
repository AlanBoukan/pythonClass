import turtle
import tkinter as tk

def makePattern():
    t1 = turtle.Turtle()
    r = int(radiusCircle.get())       # شعاع اولین دایره
    n = int(numCircles.get())         # تعداد دایره‌ها
    pen_w = int(penWidth.get())       # ضخامت قلم
    color = colorChoice.get()         # رنگ انتخابی
    
    t1.pensize(pen_w)
    t1.color(color)
    t1.speed(5)
    dest = r / n
    for i in range(n):
        newDest = dest * i
        newR = r - newDest
        t1.penup()
        t1.goto(0, -newR)
        t1.pendown()
        t1.circle(newR)

# رابط کاربری
root = tk.Tk()
root.title("رسم دایره‌های متحدالمرکز")

tk.Label(root, text="تعداد دایره‌ها:").grid(row=0, column=0)
numCircles = tk.Entry(root)
numCircles.grid(row=0, column=1)

tk.Label(root, text="شعاع اولین دایره:").grid(row=1, column=0)
radiusCircle = tk.Entry(root)
radiusCircle.grid(row=1, column=1)

tk.Label(root, text="ضخامت قلم:").grid(row=2, column=0)
penWidth = tk.Scale(root, from_=1, to=10, orient="horizontal")
penWidth.grid(row=2, column=1)

tk.Label(root, text="رنگ دایره‌ها:").grid(row=3, column=0)
colorChoice = tk.StringVar(root)
colorChoice.set("red")  # مقدار پیش‌فرض
colors = ["red", "blue", "green", "black", "purple", "orange", "yellow", "pink", "gold", "gray", "brown"]
tk.OptionMenu(root, colorChoice, *colors).grid(row=3, column=1)

tk.Button(root, text="رسم شکل", command=makePattern).grid(row=4, column=1)

root.mainloop()

tk.frame
