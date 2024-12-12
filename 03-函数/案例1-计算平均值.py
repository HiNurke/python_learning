def average(*num):
    print(num) # 传入的是一个元组
    total = sum(num)
    average = total / len(num)
    return int(average)

average_value = average(10, 30, 30, 65)
print("平均值：" , average_value)