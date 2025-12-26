
import turtle
import random

t1 = turtle.Turtle()
screen = turtle.Screen()

def makecolor():
    # تولید رنگ تصادفی به صورت کد هگز
    hex_chars = [0,1,2,3,4,5,6,7,8,9,'a','b','c','d','e','f']
    c = ''
    for i in range(6):
        index = random.randint(0, 15)
        c += str(hex_chars[index])
    return c

def shapeDraw(n, forwardNumber):
    # رسم چندضلعی با n ضلع
    t1.color('#' + makecolor())
    for i in range(n):
        w = random.randint(1, 10)   # ضخامت خط تصادفی
        t1.width(w)
        t1.forward(forwardNumber)
        t1.left(360 / n)

def makeShape(numShape, numEdge, forwardNumber):
    # numShape = تعداد شکل‌ها
    # numEdge = تعداد اضلاع هر شکل
    # forwardNumber = طول هر ضلع
    colors = ['red', 'yellow', 'brown', 'green', 'black', 'pink']
    for i in range(numShape):
        indexColor = random.randint(0, 5)
        color = colors[indexColor]
        t1.color(color)
        shapeDraw(numEdge, forwardNumber)
        t1.left(360 / numShape)


# ذخیره‌ی خروجی به صورت PostScript روی دسکتاپ
canvas = screen.getcanvas()
canvas.postscript(file=r"C:\Users\ALAN\Desktop\shape.ps")

turtle.done()


