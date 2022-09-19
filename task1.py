import csv


count = 0
with open ('books1.csv') as csvfile:
    books = csv.reader(csvfile, delimiter = ';')
    title = csvfile.readline()
    for row in books:
        count += 1

print(f'Количество записей в файле: {count}')