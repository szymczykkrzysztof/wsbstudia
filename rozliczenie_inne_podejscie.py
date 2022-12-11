import os

with open(os.path.join(os.getcwd(), 'rozliczenie-1.csv'), encoding="utf16", errors='ignore') as plik:
    zawartosc = plik.readlines()

suma = 0
na_macierzynskim = 0
for index in range(1, len(zawartosc)):
    items = zawartosc[index].split(',')
    suma += int(items[1])
    if str.strip(items[4]) == 't' and items[3] == 'k':
        na_macierzynskim += 1

print(f'Srednia: {round(suma / (len(zawartosc) - 1), 2)}')
print(f'Na macierzynskim:{na_macierzynskim}')
