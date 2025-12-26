
num=int(input("عدد را درج نماييد"))
num2 = 0
for i in range(1, num + 1):
    if num % i==0:
        print(i)
        num2 += i
print(num2)

