import csv


Tags = []
with open ('books1.csv') as csvfile:
    books = csv.reader(csvfile, delimiter = ';')
    title = csvfile.readline()
    for row in books:
        Tags.append(row[12])

Tags_str = ''.join(Tags)
Tags_new = Tags_str.split('#')
print(set(Tags_new))

#Дописала что-то))) ради проверки чего-то
