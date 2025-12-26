
# تبدیل لیست از ارقام به عدد نهایی
def makeNumber(num_list):
    result = 0
    for i in range(len(num_list)):
        result += num_list[i] * (10 ** (len(num_list) - i - 1))
    return result

# گرفتن ورودی
num1 = input("please insert the first number: ")
num2 = input("please insert the second number: ")

# مساوی کردن طول رشته‌ها با اضافه کردن صفر در ابتدای عدد کوتاه‌تر
max_len = max(len(num1), len(num2))
num1 = num1.zfill(max_len)
num2 = num2.zfill(max_len)

# جمع رقم به رقم
listSum = []
carry = 0
for i in range(max_len - 1, -1, -1):
    s = int(num1[i]) + int(num2[i]) + carry
    digit = s % 10
    carry = s // 10
    listSum.append(digit)

# اگر بعد از پایان حلقه هنوز باقی‌مانده داریم، اضافه کن
if carry > 0:
    listSum.append(carry)

# برعکس کردن لیست و ساخت عدد نهایی
listSum.reverse()
print("Sum =", makeNumber(listSum))
