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

def a(x):
    """Разбивает текстовые строки lines, преобразуя строку в 
        список слов по разделителю

        Если аргумент split_symbol не задан, в качестве разделителя
        используется пробел

        Parameters
        ----------
        split_symbol : str, optional
            разделитель
        """
    return x

#Дописала что-то))) ради проверки чего-то
# ещё что-то
