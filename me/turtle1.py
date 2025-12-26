
import turtle
import random

t1= turtle.Turtle()

def makecolor():
    list1=list
    list1=[0,1,2,3,4,5,6,7,8,9,'a','b','c','d','e','f']
    c=''
    for i in range(6):
        index=random.randint(0,15)
        c+=str(list1[index])

    return c
    
def shapeDraw(n, forwardNumber):
    t1.color('#'+makecolor())
    for i in range(n):
        w=random.randint(1,10)
        t1.width(w)
        #t1.color('#'+makecolor())
        t1.forward(forwardNumber)
        t1.left(360/n)
    
def makeShape(numShape,numEdge, forwardNumber):
    #m تغداد شکل
    #n غداد ظلغ
    list1=[]
    list1=['red','yellow','brown','green','black','pink']
    #print(color)
    dest=0
    for i in range(numShape):
        indexColor=random.randint(0,5)
        color=(list1[indexColor])
        #t1.begin_fill()
        #t1.fillcolor(color)
        shapeDraw(numEdge, forwardNumber)
        #t1.end_fill()
        t1.left(360/numShape)
        dest+=5
        
        
    
