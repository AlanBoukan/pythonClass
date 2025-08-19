 
def maghsomAlieh(num):
    return [i for i in range(1, num + 1) if num % i == 0]

def commonMaghsum(num1, num2):
    return list(set(maghsomAlieh(num1)) & set(maghsomAlieh(num2)))

def bmm(num1, num2):
    return max(commonMaghsum(num1, num2))

def kmm(num1, num2):
    return (num1 * num2) // bmm(num1, num2)

def surat(num1, num2, num3, num4):
    lcm = kmm(num1, num2)
    s1 = (lcm // num1) * num3
    s2 = (lcm // num2) * num4
    return s1, s2, lcm

def Endnum():
    num1 = int(input('Please enter the denominator of fraction 1: '))
    num2 = int(input('Please enter the denominator of fraction 2: '))
    num3 = int(input('Please enter the numerator of fraction 1: '))
    num4 = int(input('Please enter the numerator of fraction 2: '))
    op = input('Enter operation (+, -, *, /): ')

    if op in ['+', '-']:
        s1, s2, lcm = surat(num1, num2, num3, num4)
        result = s1 + s2 if op == '+' else s1 - s2
        print(f'Result: {result}/{lcm}')

    elif op == '*':
        result_num = num3 * num4
        result_den = num1 * num2
        print(f'Result: {result_num}/{result_den}')

    elif op == '/':
        result_num = num3 * num2
        result_den = num1 * num4
        print(f'Result: {result_num}/{result_den}')

    else:
        print('Invalid operation.')

# Run the program
Endnum()

