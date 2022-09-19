import csv


flag = 0
search = input('Search for: ')
with open ('books1.csv') as csvfile:
    books = csv.reader(csvfile, delimiter = ';')
    title = csvfile.readline()
    for row in books:
        lower_znach = row[3].lower()
        index = row[3].find(search)
        if index != -1 and float(row[7]) >= 200:
            flag = 1
            print(row)
    if flag == 0:
        print('Nothing found')
