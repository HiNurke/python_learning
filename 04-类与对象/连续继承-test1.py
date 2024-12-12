class A():
    def func(self):
        print("A类")

class B(A):
    def func(self):
        print("B类")

class C(B):
    def func(self):
        # 带上self参数是为了确认调用父类函数给哪个子类实现诸如定义类属性的操作
        A.func(self)
        B.func(self)

C().func()