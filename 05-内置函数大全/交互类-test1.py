def func1():
    num = int(input('务必输入1-100数字'))
    if (num < 1 or num > 100):
        func1()
    else:
        print('输入正确', num)
func1()