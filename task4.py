value = int(input('введите число'))
max_value = a % 10

while value > 0:
    if value % 10 > max_value:
        max_value = value % 10
    value = value // 10
print(max_value)

