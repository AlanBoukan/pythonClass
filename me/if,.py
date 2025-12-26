def alan(n):
    #n=int(input ("pleas type the number"))

    if n%2==0:
        return 0
    else:
        return 1

def an():
    a=0
    list1=[]
    sum=0
    #if alan() (n=0):
        #for n in range(1,101):
    #if alan() (n=1):
        #for n in range(1,101):
    for n in range(1,101):
        if alan(n)==0:
            list1.append(n)
            
            #print(n,end=',')
            sum +=n
    
    print(sum)

    #list1==list
    

    print(len(list1))
      
        

    
