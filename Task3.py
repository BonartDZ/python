import encodings
import math
with open(r'C:\projets\lesson5\task3.txt', 'r+', encoding='utf-8') as file:
    lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = list(lines[i].split())
        if int(lines[i][1]) < 20000:
           print(lines[i][0], ', получает меньше 20к')
    sal = list(lines)

    print(sal)
    sum_sr = ((int(sal[0][1])) + (int(sal[1][1])) + (int(sal[2][1])) + (int(sal[3][1])) + (int(sal[4][1])) + (int(sal[5][1])) + (int(sal[6][1])) + (int(sal[7][1])) + (int(sal[8][1])) + (int(sal[9][1]))) / 10
    # я понимаю, что сделал очень плохо выше, но не понимаю как обратиться к sal[i][1], он то пишет, что не итерируется i
    # то ругается на то что инт со строкой не складывается.

    print(sum_sr)