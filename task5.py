my_list = [7, 7, 5, 4, 4, 2]
new_value = (input('введите число: '))
i = 0
for i in range(len(my_list)):
    if int(new_value) >= int(my_list[i]):
        my_list.insert((i), new_value)
        print(my_list)
        break
    else:
        print('значение меньше минимально установленного')
        break
