# python


import csv


def hash(s):  # функция генерации hash по имени
    alf = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ '
    d = {l: i for i, l in enumerate(alf, 1)}
    p = 67
    m = 10 ** 9 + 9
    hash_value = 0
    p_pow = 1
    for c in s:
        hash_value = (hash_value + d[c] * p_pow) % m
        p_pow = (p_pow * p) % m
    return int(hash_value)


answer = []
with open('history_mirror.csv', encoding="utf8") as csvfile:  # открываем файл с исходной таблицей
    reader = list(csv.DictReader(csvfile, delimiter=',', quotechar='"'))
    for row in reader:  # проходим по таблице, создавая hash и записывая в результат новой таблицы
        row['ID'] = hash(row['username'])
        print(row)
        answer.append(row)

with open('users_with_hash.csv', 'w', newline='', encoding='utf-8') as file:  # запись в новую таблицу
    w = csv.DictWriter(file, fieldnames=['ID', 'date', 'username', 'verdict'])
    w.writeheader()
    w.writerows(answer)
