var_proc = float(input('введите объем выручки'))
var_costs = float(input('введите объем издержек'))
if var_costs > var_proc:
    print('вы работаете в убыток')
else:
    print('рентабельность: ' + str(var_proc / var_costs))
    var_workers = int(input('работающих на предприятии'))
    print('прибыль на человека ' + str((var_proc - var_costs) / var_workers) + ' рубля (ей)')

