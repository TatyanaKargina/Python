def my_func():
    x = int(input('Введите действительное положительное число'))
    y = int(input('Введите целое отрицательное число'))
    result = x**y
    return result

total = my_func()
print(total)