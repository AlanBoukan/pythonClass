
num = int(input("عدد را درج نماييد: "))
sum_divisors = 0  # متغیر برای جمع مقسوم‌علیه‌ها

for i in range(1, num + 1):
    if num % i == 0:
        print(i)
        sum_divisors += i  # اضافه کردن i به مجموع

print("مجموع مقسوم‌علیه‌ها:", sum_divisors)

