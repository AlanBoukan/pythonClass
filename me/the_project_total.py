
n = int(input("تعداد رقم عددها: "))

# دریافت دو عدد n رقمی
num1 = input(f"عدد اول {n} رقمی را وارد کنید: ")
num2 = input(f"عدد دوم {n} رقمی را وارد کنید: ")




if len(num1) == n and len(num2) == n and num1.isdigit() and num2.isdigit():
    sum_result = int(num1) + int(num2)
    print(f"مجموع دو عدد برابر است با: {sum_result}")



sum_result = num1 + num2


print("مجموع دو عدد برابر است با:", sum_result)


