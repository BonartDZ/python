
a = int(input('введите число: '))
b = input('введите число: ')
c = int(input('введите число: '))
d = input('введите число: ')
e = float(input('введите число: '))
my_list = [a, b, c, d, e]
print(my_list)
print(type(my_list))
k = len(my_list) - 1
i = 0
while i < k:
    i += 1
    print(type(my_list[i]))
