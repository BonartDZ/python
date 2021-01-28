import encodings
with open(r'C:\projets\lesson5\Task6.txt', 'r+') as file:
    for line in file:
        data0 = file.readline().split()
        data1 = file.readline().split()
        data2 = file.readline().split()
        print(data0, data1, data2)
    my_dict = {data0[0] : int(data0[1][0:3]) + int(data0[2][0:2]) + int(data0[3][0:2]), data1[0] : int(data1[2][0:2])
    + int(data1[3][0:2]), data2[0] : int(data2[2][0:2])}
    print(my_dict)