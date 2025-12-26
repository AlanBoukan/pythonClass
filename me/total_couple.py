#مجحوع اعداد زوج تا يک عدد دلخواه
def couple_number():
    
    num1=int(input("عدد را درج نماييد"))
    num2=0
    list1=list()
    for i in range(1,  num1 + 1):
        if i % 2==0:
            #print(i)
            list1.append(i)
            #num2 += i
    print("محموع اعداد زوج برابر است با:   ",sum(list1))
    print("تعداد اعداد زوج برابر است با:   ",len(list1))
