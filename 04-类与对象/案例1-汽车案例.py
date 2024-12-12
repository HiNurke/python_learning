class Car(object):
    car_count = 0  # 计数器

    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color

        Car.car_count += 1  # 每创建一个Car对象，计数器就+1

    # 介绍汽车详细信息的方法
    def get_car_info(self):
        return f"品牌：{self.brand}，型号：{self.model}，颜色：{self.color}"

    # 统计汽车数量的方法
    # 应该通过类变量来调用进行统计输出
    @classmethod
    def get_total_count(cls):
        return cls.car_count

    # 检验颜色合法性
    # 通用的方法，而且需要传参
    @staticmethod
    def is_valid_color(color):
        valid_colors = ["red", "blue", "green"]
        return color.lower() in valid_colors


car1 = Car("Tesla", "Model 3", "red")
car2 = Car("Toyota", "Camry", "gray")

print(car1.get_car_info())
print(car2.get_car_info())

print("汽车数量为：{}台".format(Car.get_total_count()))
print(f"汽车数量为：{Car.get_total_count()}台")

print(Car.is_valid_color(car1.color))
print(Car.is_valid_color(car2.color))
