def total1():
    sum = 0
    dahgan=0
    num1=input('pleas enter the firs number')
    num2=input('pleas enter the second number')
    i=(len(num1)-1)
    j=(len(num2)-1)
    listsum=list()
    while(i>=0 or j>=0):
        
        num_1=int(num1[i]) if i >= 0 else 0
        num_2=int(num2[j]) if j >= 0 else 0
        sum= num_1+num_2+dahgan
 
        yekan=sum%10
        dahgan=sum//10
        i-=1
        j-=1
        listsum.append(yekan)
    if dahgan > 0:
        listsum.append(dahgan)
    newNumber=listsum[::-1]
    print('sum =', newNumber) 

