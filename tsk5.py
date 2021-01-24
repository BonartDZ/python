from functools import reduce
# new_list = [el for el in range(100, 1001)] - формирование списка работает
## print(new_list) - список выводится
def my_func (el_p, el):
    return el_p * el

print('произведение всех чисел составляет: ', reduce(my_func, [el  for el in range(100, 1001)]))