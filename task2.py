import csv


count_30 = 0
with open ('books1.csv') as csvfile:
    books = csv.reader(csvfile, delimiter = ';')
    title = csvfile.readline()
    for row in books:
        if len(row[1]) > 30:
            count_30 += 1

print(f'Количество записей, у которых в поле НАЗВАНИЕ строка длиннее 30 символов: {count_30}')