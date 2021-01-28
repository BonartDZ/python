import encodings
import math

with open(r'C:\projets\lesson5\Task4.txt', 'r+', encoding='utf-8') as file:
    read_data = file.read()
read_data = read_data.replace('one', 'один')
read_data = read_data.replace('two', 'два')
read_data = read_data.replace('three', 'три')
read_data = read_data.replace('four', 'четыре')
#как обращаться к каждой строке? можно прописать через цикл, проиндексировать строку? в комментарий
# к заданию скиньте плз ссылку на литературу, обсуждение. очень интересно, а то получается много кода, охото понять
# как это лаконично писать. заранее спасибо
with open(r'C:\projets\lesson5\Task4.1.txt', 'w') as file:
    file.write(read_data)
    print(file)
