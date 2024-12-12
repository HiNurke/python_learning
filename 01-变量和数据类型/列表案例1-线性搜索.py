# 定义一个列表
arr = [4, 2, 7, 1, 9, 5]
# 需要查找的值
target = 7

def linear_search(arr, target):
    # 遍历该数组的长度
    for i in range(len(arr)):
        # 通过索引来判断这个值是否为真
        if arr[i] == target:
            return i
    return -1

index = linear_search(arr, target)
print(f"元素{target}的索引为：{index}")
