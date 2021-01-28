from functools import reduce

with open(r'task5.txt', 'w') as file:
    file.write('2 33 1 44 55')
with open(r'task5.txt', 'r') as file:
    list = file.readline().split()
    i = 0
    for i in range(len(list)):
        list[i] = int(list[i])
        i += 1
    def my_func(el_p, el):
        return el_p + el


    print('сумма всех чисел составляет: ', reduce(my_func, list))
