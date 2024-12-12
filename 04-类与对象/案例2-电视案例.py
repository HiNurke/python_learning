class TV:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
        self.is_on = False
        self.volume = 50
        self.channel = 1

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def change_channel(self, channel):
        self.channel = channel

    def volume_up(self):
        if self.volume < 100:
            self.volume += 1
        elif self.volume == 100:
            print("电视机音量已达最大")
        print(f"当前音量为：{self.volume}")

    def volume_down(self):
        if self.volume > 0:
            self.volume -= 1
        else:
            print("电视机音量已达最小")
        print(f"当前音量为：{self.volume}")

tv = TV("Sony", 55)

tv.turn_on()
print("电视已打开" if tv.is_on == True else "电视已关闭")

tv.change_channel(5)

tv.volume_up()
tv.volume_up()
tv.volume_down()

print(f"品牌: {tv.brand}, 尺寸: {tv.size}, 频道: {tv.channel}, 音量: {tv.volume}")

tv.turn_off()
print("电视已打开" if tv.is_on == True else "电视已关闭")