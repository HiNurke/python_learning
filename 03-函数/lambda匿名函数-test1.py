age = {'小李': 18, "小王": 27, "小张": 23}
print(age.items())

# 需求：保留值大于20的键值对
age_processed = dict(filter(lambda item: item[1] > 20, age.items()))
print(age_processed)