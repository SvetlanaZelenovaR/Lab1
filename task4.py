import csv
import random


books_new = []
with open ('books1.csv') as csvfile:
    books = csv.reader(csvfile, delimiter = ';')
    title = csvfile.readline()
    f = open('generator.txt', 'w')
    for row in books:
        books_new.append(row[3] + '. ' + row[1] + ' - ' + row[6])

for i in range (1, 21):
    f.write(str(i) + ' ' + random.choice(books_new) + '\n')