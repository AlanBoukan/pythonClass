#while
    
sum = 0
dahgan=0
num1=str(123)
num2=str(14567)
i=(len(num1)-1)
j=(len(num2)-1)
listsum=list()
while(i>=0 or j>=0):
  
    sum= sum + (int(num1[i])) + (int(num2[j]))+dahgan
    yekan=sum%10
    dahgan=sum//10
    i-=1
    j-=1
    listsum.append(yekan)
if dahgan > 0:
    listsum.append(dahgan)

newNumber=listsum[::-1]
print(newNumber) 
