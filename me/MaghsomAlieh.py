def maghsomAlieh():
    #alan براي تعداد مقسوم غليه ها مي باشد
    alan=0
    num1=int(input('pleas enter the number'))
    list1=list()
    for i in range(1, num1 +1):
             if num1%i==0:
                 alan+=1
    print(alan)
                 
                 
