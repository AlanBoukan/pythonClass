num1=int(input("عدد را درج نماييد"))
num2=0
for i in range( num1 + 1):
    if i % 2==1:
        #print(i)
        num2 += i
print(num2)
