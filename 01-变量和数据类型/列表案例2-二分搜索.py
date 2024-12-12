arr = [1, 12, 4, 6, 7, 3]
target = 7

def binary_search(arr, target):
    arr.sort()
    low = 0 # 定义虽小索引
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

index = binary_search(arr, target)
print("目标元素的索引：", index)