def prime_number(num):
    #num=int(input('عدد را درج نماييد'))
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count+=1
    if count==2:
        return 1
    else:
        return 0
def checkAll():
    numEnd=int(input("لطفا حد عدد نهايي را درج نماييد"))
    list1=list()
    for i in range(1, numEnd+1):
        if prime_number(i)==1:
            list1.append(i)
    print(list1)

    print(sum(list1))  
            
            
            
            
