from itertools import permutations, repeat, combinations

my_list = [5, 3, 6, 32, 5, 3, 6, 12, 45, 75]
new = [el for el in my_list if my_list.count(el) == 1]
print(new)