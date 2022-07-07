def my_func(a, b, c):
   value = [a, b, c]
   max_1 = max(value)
   value.remove(max_1)
   max_2 = max(value)
   sum = max_1 + max_2
   print(sum)

my_func(9,6,7)

