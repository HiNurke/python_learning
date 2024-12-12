import time

def loading(wait, interval):
    print("等待{}s".format(wait), end="")
    for i in range(int(wait / interval)):
        print(".", end='')
        time.sleep(interval)
    print('\n等待结束')

loading(3, 1)
