my_list = [4, 30, 6, 43, 11, 7, 16]
new_list = [el for el in my_list if el > my_list[my_list.index(el)-1]]

print(new_list)