#مقسوم عليه هاي يک عدد
num=int(input("عدد را درج نماييد"))

for i in range(1,num+1):
    if num%i==0:
        print(i)
