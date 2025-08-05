# Sum two big numbers
def makeNumber(num):
    result=0
    for i in range(len(num)):
        result=result+num[i]*(10**(len(num)- (i-1)))
    return result
num1=input("please insert the first number")
num2=input("please insert the second number")

max_len = max(len(num1), len(num2))
num1 = num1.zfill(max_len)
num2 = num2.zfill(max_len)

listSum=list()
dahgan=0

for i in range(max_len -1,-1,-1):
    s=int(num1[i])+int(num2[i])+dahgan
    yekan=s%10
    dahgan=s//10

    listSum.append(yekan)
if dahgan > 0:
    listsum.append(dahgan)

#listSum.revrse()
    
newNumber=listSum[::-1]
print("sum =", makeNumber(newNumber))
#print(sum)


