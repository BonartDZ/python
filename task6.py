from itertools import count, cycle

for el in count(3):
    if el > 10:
        break
    else:
        print(el)




food_list = ["морковь", "картофель", "курица", "лук", "колбаса"]
print(food_list)
iter = cycle(food_list)
for i in range(0, 10):
   print(next(cycle(iter)))




