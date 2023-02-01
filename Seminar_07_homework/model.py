import csv

reader_object = "telephone_book.csv"

def read_file_csv(x):
    with open(x, encoding = 'utf-8') as r_file:
        data = []
        file_reader = csv.reader(r_file, delimiter = "_")
        for i in file_reader:
            data.append(i)
    return(data)