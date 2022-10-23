import csv


# чтение csv-файла
def read_file (file):
    resultat = []
    with open(file, encoding="utf8") as csvfile:
        reader = csv.reader(csvfile, delimiter=';',)
        for row in reader:
            resultat.append (row)
        return (resultat)

# чтение в словарь
def print_console (file,lable):    
    with open(file, encoding="utf8") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        expensive = sorted(reader, key=lambda x: int(x[lable]), reverse=True)
    for record in expensive:
        print(record)

# запись в файл полностью
def re_file (file,text):    
    with open(file, 'w', encoding="utf8", newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        for row in text:
            writer.writerow(row)

# запись в файл (для перезаписи режим 'w')
def add_text (file,text):    
    with open(file, 'a', encoding="utf8", newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow(text)
   



