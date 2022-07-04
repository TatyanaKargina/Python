my_list = [7, 5, 4, 3, 2]
element = int(input('Введите новый элемент рейтинга'))

for i in range(len(my_list)):
    if element == my_list[i]:
        my_list.insert(i + 1, element)
        break
    elif element > my_list[0]:
        my_list.insert(0, element)
    elif element < my_list[-1]:
        my_list.append(element)
print(my_list)

