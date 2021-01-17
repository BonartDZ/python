year_list = ['зима', 'весна', 'лето', 'осень']
year_dict = {1 : 'зима', 2 : 'весна', 3 : 'лето', 4 : 'осень'}
month_numb = int(input('введите номер месяца '))
if 3 <= month_numb == 12:
        print(year_list[0])
        print(year_dict.get(1))
if 3 < month_numb <= 5:
    print(year_list[1])
    print(year_dict.get(2))
if 5 < month_numb <= 8:
    print(year_list[2])
    print(year_dict.get(3))
if 8 < month_numb <= 11:
    print(year_list[3])
    print(year_dict.get(4))
if month_numb > 12:
    print('такого номера месяца не существует')




