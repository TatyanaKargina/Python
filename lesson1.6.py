revenue = int(input('Введите размер выручки фирмы'))
costs = int(input('Введите размер издержек фирмы'))
profit = revenue-costs
if revenue > costs:
    profitability = profit / revenue
    print('Прекрасно, Ваша компания получила прибыль', profit)
    print(f'Рентабельность составила {profitability:.25f}')
    persons = int(input('Введите численность сотрудников'))
    print('Прибыль на одного сотрудника составила', profit / persons)
elif revenue < costs:
    print('Ваша компания работает в убыток')
else:
    print('Ваша компания работает в ноль')
