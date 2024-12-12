class Animal:  # 父类
    '''动物类'''
    name = '[3号]'

class Dog(Animal):  # 继承动物类
    '''小狗类'''
    def sound(self):
        print(f"{self.name} 汪汪汪！")
class Cat(Animal):  # 继承动物类
    '''小猫类'''
    def sound(self):
        print(f"{self.name} 喵喵喵！")
class Cow(Animal):  # 继承动物类
    '''小牛类'''
    def sound(self):
        print(f"{self.name} 哞哞哞！")

# 四个类中的方法完全一致，封装一个函数，实现调用这些类中的同个方法，但是不同效果
def make_sound(x):
    # 参数x是传入的实例化对象
    x.sound() # 调用对象所属类的方法

# 首先实例化这几个动物类
dog = Dog()
cat = Cat()
cow = Cow()

# 向函数传入不同的类，调用同名方法
make_sound(dog)
make_sound(cat)
make_sound(cow)