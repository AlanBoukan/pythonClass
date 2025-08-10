def tam_number(num): 
    #num = int(input("عدد را درج نماييد: "))
    num2 = 0 
    
    for i in range(1, num  ):
        if num % i == 0:
            #print(i)
            num2 += i 
    if num==num2:
        return 1
    else:
        return 0
       
        #print('tam number:', tam_number1)
    #else:
        #print('its not a tum number')

def checkAll():
    numEnd=int(input("لطفا حد عدد نهايي را درج نماييد"))
    list1=list()
    for i in range(1, numEnd+1):
        if tam_number(i)==1:
            list1.append(i)
    print(list1)
        
    print(sum(list1))
    
