commodity = []

# 添加商品到购物车
def add_item(item_name, item_price):
    item = {
        "name": item_name,
        "price": item_price
    }
    commodity.append(item)

def display_items():
    if len(commodity) == 0:
        print("购物车为空")
    else:
        print("购物车的商品如下：")
        for item in commodity:
            print(f"商品名称：[{item["name"]}]，价格：{item["price"]}")

def calculate_total_price():
    total_price = 0
    for item in commodity:
        total_price += item["price"]
    return total_price


add_item("手机", 1999)
add_item("电视", 3999)
add_item("电脑", 5999)

display_items()

total_price = calculate_total_price()
print(f"购物车共计：{total_price}元")