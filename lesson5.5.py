def summary():
    try:
        with open('sum.txt', 'w+') as f:
            line = input('Введите цифры через пробел \n')
            f.writelines(line)
            my_numb = line.split()

            print(sum(map(int, my_numb)))
    except ValueError:
        print('Ошибка ввода')

summary()
