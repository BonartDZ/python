
my_dict = {}
my_list = []

goods = int(input('введите количества товара '))
n = 1
while n <= goods:
        my_dict = {'Наименование': input('Введите наименование товара: '), 'Цена': input('Введите цену товара: '), 'Количество': input('введите количество ')}
        my_list.append((n, my_dict))
        n += 1
print(my_list)
my_analitics = {}
for el in my_list:
    for key, values in el[1].items():
        if key in my_analitics:
            my_analitics[key].append(values)
        else:
            my_analitics[key] = [values]
print(my_analitics)

