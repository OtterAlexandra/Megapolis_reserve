# python


import csv

with open('history_mirror.csv', encoding="utf8") as csvfile:
    reader = list(csv.DictReader(csvfile, delimiter=',', quotechar='"'))  # открываеи файл
    for i in range(len(reader)):
        j = i - 1
        key = reader[i]
        while (reader[j]['verdict']) > (key['verdict']) and j >= 0:  # сортируем в алфавитном порядке
            reader[j + 1] = reader[j]
            j -= 1
        reader[j + 1] = key
        count = 1
    for el in reader:  # выводим первые 4 записи
        print(f'{el["date"]} - {el["username"]} - {el["verdict"]}')
        count += 1
        if count == 5:
            break
