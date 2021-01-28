with open(r'text.txt', 'w') as file:
    file.write('hello\nworld\nrandom string\n')
    content = file.read
    print(content)


