# python


import csv

with open('history_mirror.csv', encoding='utf-8') as f:
    # открываем файл с таблицей
    reader = csv.reader(f, delimiter=',', quotechar='"')
    answer = list(reader)[1:]
    result = []
    for row in answer:
        if row[2] == 'Победа над смертью':  # сравниваем на совпадение
            result.append([row[0], row[1]])
            if row[0] == '2008-07-22':  # выводим самую раннюю дату
                print(f'Сообщение было зафиксировано: {row[0]} у пользователя {row[1].split()[0]} '
                      f'{row[1].split()[1][0]}.{row[1].split()[2][0]}.')

with open('mirror_error.csv', 'w', newline='', encoding='utf-8') as file:  # записываем в новый файл
    w = csv.writer(file)
    w.writerow(['date', 'username'])
    w.writerows(result)
