staff = {
 # id号  姓名            年龄        工资
    1: {'name': '张三', 'age': 25, 'salary': 8000},
    2: {'name': '李四', 'age': 30, 'salary': 7000},
    3: {'name': '王五', 'age': 35, 'salary': 15000},
}

# 添加一个员工信息
staff[4] = {'name': '赵六', 'age': 27, 'salary': 9000}

# 查询全部员工信息
for key, value in staff.items():
    print(f"id: {key}, message: {value}")

# 查询薪资大于8000的员工信息
for key, value in staff.items():
    if value['salary'] > 8000:
        print(f"id: {key}, message: {value}")

# 查询id为3的员工薪资
print(staff[3]['salary'])
for key, value in staff.items():
    if key == 3:
        print(value['name'], ":", value['salary'])