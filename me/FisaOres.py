

import turtle
import math

t1 = turtle.Turtle()

def makeShape(degre, forwardLen1, forwardLen2):
    t1.clear()
    # First two sides
    t1.forward(forwardLen1)
    t1.write(forwardLen1)
    t1.left(90)
    t1.forward("sideLen: " + str(forwardLen2))
    t1.write(forwardLen2)
    t1.left(degre)
    t1.write('internalAngle:' + str(degre-90))
    # Compute the third side using Pythagorean theorem
    forwardLen3 = math.sqrt(forwardLen1**2 + forwardLen2**2)
    
    # Draw the third side
    t1.forward(forwardLen3)
    t1.write(forwardLen3)

# Example usage:
#makeShape(117, 100, 50)
#print(forwardLen3)

#turtle.done()

