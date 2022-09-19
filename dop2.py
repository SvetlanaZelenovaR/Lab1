import csv


all_books = []
with open ('books1.csv') as csvfile:
    books = csv.reader(csvfile, delimiter = ';')
    title = csvfile.readline()
    for row in books:
        all_books.append([row[1]] + [row[8]])

all_books.sort(reverse = True, key = lambda book: int(book[1]))
print(all_books[:21])

