# we try to solve the equation y=ax+b
# we get a, b and y
def translator():
    #num1=input('pleas enter the majhul '))
    print("In this function we will calculate x in y=ax+b")
    a=int(input('pleas enter the a'))
    b=int(input('pleas enter b'))
    y=int(input('pleas enter y'))
    num2=y-b
    #print(num2)
    x=num2/a
    return x
