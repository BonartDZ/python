from math import factorial
def my_fact (n):
    for el in n:
        yield factorial(el)

res = my_fact([el for el in range (1, 22)]) #это чтоб проверить как оно работает, ограничил в пределах 1-22

for n in range(0, 10):
   print(next(res))