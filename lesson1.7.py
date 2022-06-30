firstday_km = float(input('Введите количество километров первого дня пробежки'))
result_km = float(input('Введите желаемый результат километров'))
day = 1

while firstday_km < result_km:
    firstday_km = firstday_km * 1.1
    day = day + 1
print(f'На {day} день спортсмен достиг результата — не менее {result_km} км.')


