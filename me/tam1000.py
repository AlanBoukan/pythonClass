def tam_number2():
    num = int(input("عدد را درج نماييد: "))
    num2 = 0  

    for i in range(1, num  ):
        if num % i == 0:
            #print(i)
            num2 += i 
            if num==num2:
                tam_number1=num2
                #print('tam number:', tam_number1)
                for y in range(1, 1001):
                    if tam_number1==y:
                        
                        print(y)


