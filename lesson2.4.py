sum = int(input('Введите количество посещенных городов'))
n = 0
i = 0
city = []
while n < sum:
    city.append(input('Введите название города'))
    n += 1
print(city)

for el in range(int(len(city)/2)):
    city[i], city[i + 1] = city[i + 1], city[i]
    i += 2
print(city)