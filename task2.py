import encodings
with open(r'C:\projets\lesson5\task2.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    print("количество строк", len(lines))
    for i in range(len(lines)):
        lines[i] = list(lines[i].split())
        print('количество слов в строке',i + 1, ': ', len(lines[i]))







