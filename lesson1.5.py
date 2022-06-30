revenue = int(input('Введите размер выручки фирмы'))
costs = int(input('Введите размер издержек фирмы'))

if revenue > costs:
    print('Прекрасно, Ваша компания получила прибыль!')
elif revenue < costs:
    print('Ваша компания работает в убыток')
else:
    print('Ваша компания работает в ноль')

