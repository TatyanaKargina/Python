with open('salary.txt', 'r') as f:
    salary = []
    min_salary = []
    my_list = f.read().split('\n')
    for i in my_list:
        i = i.split()
        if int(i[1]) < 20000:
            min_salary.append(i[0])
        salary.append(i[1])
print(f'Оклад меньше 20.000 {min_salary}, средний оклад {sum(map(int, salary)) / len(salary)}')

