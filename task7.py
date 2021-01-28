import encodings
import json
with open(r'C:\projets\lesson5\task7.txt', 'r+') as file:
    for line in file:
        data0 = file.readline().split()
        data1 = file.readline().split()
        data2 = file.readline().split()
        print(data0, data1, data2)
    my_dict = {data0[0] : int(data0[2]) - int(data0[3]), data1[0] : int(data1[2]) - int(data1[3]), data2[0] : int(data2[2]) - int(data2[3])}
    print(my_dict)
    average_list = [my_dict.get(data0[0]), my_dict.get(data1[0]), my_dict.get(data2[0])]
    print(average_list)
    filt_list = list(filter(lambda el: el > 0, average_list))
    print(filt_list)
    average_profit = sum(filt_list) / len(filt_list) + 1
    print(average_profit)
    my_dict2 = {'average_profit' : average_profit}
    print(my_dict2)
    total_list = [my_dict, my_dict2]
    print(total_list)
    with open ('my_json_file.json', 'w') as write_f:
            json.dump(total_list, write_f)


