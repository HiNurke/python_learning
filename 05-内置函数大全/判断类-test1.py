class MyClass():
    a = 1
    def __init__(self):
        self.b = 2
        c = 3
    def func2(self):
        print("执行了func2")
        e = 5
        return e

print(MyClass().b) # 2
print(MyClass().func2) # 可输出
print(MyClass().func2()) # None