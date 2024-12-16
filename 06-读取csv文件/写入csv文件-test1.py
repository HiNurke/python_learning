import csv

with open('./test.csv', 'a', newline='', encoding='utf-8-sig') as f:
    writer = csv.writer(f)

    # writer.writerow([])
    # writer.writerow([6, 13, '妲己', '女', '约会'])

    data = [
        [7, 49, '孙悟空', '男', '打架'],
        [8, 14, '猪八戒', '男', '吃饭'],
        [9, 20, '沙悟净', '男', '干活']
    ]
    writer.writerows(data)
