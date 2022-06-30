value = int(input('Введите целочисленное положительное число'))
maximum = value % 10
num = value

while num > 0:
    last_digit = num % 10
    if last_digit > maximum:
        maximum = last_digit

    if last_digit == 9:
        break
    num = num // 10
    print(num)

print(f'Самая больщя цифра в числе {value} = {maximum}')