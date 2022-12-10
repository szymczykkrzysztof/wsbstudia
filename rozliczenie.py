import os

with open(os.path.join(os.getcwd(), 'rozliczenie-1.csv'), encoding="utf16", errors='ignore') as plik:
    data = plik.readline()
    data = plik.readlines()

sum = 0
na_macierzynskim = 0
for index in range(0, len(data)):
    items = data[index].split(',')
    sum += int(items[1])
    if str.strip(items[4]) == 'n':
        na_macierzynskim += 1

print(f'Srednia: {round(sum / len(data), 2)}')
print(f'Na macierzynskim:{na_macierzynskim}')
