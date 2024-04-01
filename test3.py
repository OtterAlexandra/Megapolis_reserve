# python


import csv

with open('history_mirror.csv', encoding="utf8") as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')  # открытие файла
    answer = list(reader)[1:]
    name = input()  # ввод данных
    while name != 'stop':
        n = 0
        for row in answer:
            if name in row[1]:
                print(f'Предсказание для {row[1].split()[0]} {row[1].split()[1][0]}.{row[1].split()[2][0]}. - {row[2]}')  # вывод предсказания

        name = input()  # ввод данных повторно
