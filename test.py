print("Hello World")

a = 10
b = 20

def greet(name):
    return f"Hello, {name}"
print(greet("Alice"))

class MyClass(object):
    def __init__(self, x):
        self.x = x
mc = MyClass(20)
print(mc.x)