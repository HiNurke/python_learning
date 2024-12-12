class Shape:
    def __init__(self):
        self.area = 100
        self.perimeter = 40

shape_obj = Shape()
user_input = input("请输入要查询的属性（area或perimeter）")
result = getattr(shape_obj, user_input, None)
if result is not None:
    print(f"该形状的{user_input}为：{result}")
else:
    print("输入的属性不存在")
# print(shape_obj.user_input) # 错误