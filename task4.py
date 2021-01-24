my_list = [2, 33, 33, 12, 13, 8, 33, 44, 1, 1, 1, 5, 3, 2, 22]
new_list = [el for el in my_list if my_list.count(el) == 1]
print(new_list)