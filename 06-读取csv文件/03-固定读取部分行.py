import csv


# with open(r'test.csv', 'r', encoding='utf-8-sig') as f:
#     reader = csv.reader(f)
#     for _ in range(2):
#         next(reader)
#     for i in range(3):
#         row = next(reader)
#         print(row)

lines_to_read = [2, 4, 6]

with open(r'test.csv', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line_num in lines_to_read:
        if line_num <= len(lines):
            # 读取并去掉末尾换行符
            print(lines[line_num - 1].strip())
