from itertools import cycle, count

n_start = int(input('Стартовое число: '))
n_stop = n_start * 10

my_list = [i for i in range(n_stop)]
count = 0
for b in cycle(my_list):
    if count < n_stop + 8:
        print(b)
        count += 1
    else:
        break

