import sys

def my_sum():
    sum_result = 0
    while True:
        number = input('Введите числа через пробел. Для выхода из программы нажмите ! ').split()
        result = 0
        for n in range(len(number)):
            if number[n] == '!':
                print('Финальная сумма: ', sum_result)
                sys.exit('Выход из программы')
            else:
                result = result + int(number[n])
        sum_result = sum_result + result
        print(f'Сумма составила: {sum_result}')
    print(f'финальная сумма: {sum_result}')

my_sum()