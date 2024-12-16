import csv

cols_to_read = [1, 2, 4]

with open('./test.csv', 'r', encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    for row in reader:
        for cols_num in cols_to_read:
            print(row[cols_num - 1], end=' ')
        print()