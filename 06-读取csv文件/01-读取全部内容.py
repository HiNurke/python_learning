import csv

with open('./test.csv', 'r', encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)