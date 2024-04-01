# python


import csv

with open('history_mirror.csv', encoding="utf8") as csvfile:
    classes = {}  # словарь для новой информации
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')  #
    answer = list(reader)[1:]
    for row in answer:  # прохождение по всему файлу и заполнение словаря
        if row[0].split('-')[0] not in classes:
            classes[row[0].split('-')[0]] = {'count': 0}
            classes[row[0].split('-')[0]]['count'] += 1

        else:
            classes[row[0].split('-')[0]]['count'] += 1

for i in classes:  # вывод всех годов
    count = classes[i]['count']
    print(f'В {i} году зеркало было использовано {count}.')
