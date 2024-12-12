class MyClass(object):
    def __init__(self):
        self.x = 1  # 定义实例属性

    def func1(self):
        print("我是实例方法")

    @classmethod
    def func(cls, n):
        print(f'测试传入的参数n:{n}')
        # print(f'实例属性a为{cls.x}')  # 无法调用
        cls().func1() # 调用实例方法成功

MyClass.func(10)