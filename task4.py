my_list_str = (input('введите слова через пробел '))
my_list = my_list_str.split( )
print(my_list)    # подсказка чтоб не забыть что вводил =)
n = 1
i = 0
while i < len(my_list):
    if len(my_list[i]) <= 10:
        print((str(n) + '. ' + str(my_list[i])))
    else:
        print((str(n) + '. ' + str(my_list[i][0:10])))
        i += 1
        n += 1
