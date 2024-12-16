import csv

with open('./test.csv', 'r', encoding='utf-8-sig') as f:
    # 创建csv阅读器对象
    reader = csv.DictReader(f)

    # 获取表头（字段名称）
    fieldnames = reader.fieldnames
    print(f"字段名: {fieldnames}")

    # 遍历所有行
    for row in reader:
        # 使用字段名动态访问数据
        for field in fieldnames:
            print(f"{field}: {row[field]}", end=' | ')
        print()  # 每一行数据后换行
