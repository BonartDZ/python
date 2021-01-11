var_time = int(input('введите количество секунд'))
var_hour = var_time//3600
var_min = (var_time - var_hour*3600)//60
var_sec = var_time - (var_hour*3600 + var_min * 60)
print(f"время в формате чч {var_hour} мм {var_min} сс {var_sec} ")

