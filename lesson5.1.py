with open('value.txt', 'w') as f:
    list = []
    while True:
        el_list = input('Введите значения: ')
        list.append(el_list)
        if el_list == ' ':
            break
    for el in list:
        f.write(el + '\n')