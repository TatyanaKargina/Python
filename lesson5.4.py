rus = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
rus_numbers = []
with open('numbers.txt', 'r') as f:
    for i in f:
        i = i.split(' ', 1)
        rus_numbers.append(rus[i[0]] + '  ' + i[1])
    print(rus_numbers)

with open('rus_numbers.txt', 'w') as f_2:
    f_2.writelines(rus_numbers)
