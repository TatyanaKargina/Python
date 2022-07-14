with open('data.txt', 'r') as f:
    lines =0
    words = 0
    for line in f:
        lines += 1
        words += len(line.split())

print('Количество строк: ', lines)
print('Количество слов: ', words)
