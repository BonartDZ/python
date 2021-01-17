
my_list_str = (input('введите переменные через пробел'))
my_list = my_list_str.split( )
print(my_list)
print(type(my_list))
k = len(my_list) - 1
i = 0
while i < k:
    my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
    i += 2

print(my_list)
