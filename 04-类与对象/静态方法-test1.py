class MyClass(object):
    def func1(self):  # 定义一个实例方法
        print('实例方法')

    @staticmethod
    def func2():  # 定义一个静态方法
        # func1()  # 直接调用实例方法(无法调用)
        MyClass().func1()  # 通过类调用实例方法(无法调用)

MyClass.func2()