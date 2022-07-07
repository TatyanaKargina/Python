def int_func(word):
    return word.title()

words = input('Введите слова, разделив их пробелами').split()
for w in words:
    result = int_func(w)
    if result:
        print(int_func(w))