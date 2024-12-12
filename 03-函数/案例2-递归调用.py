def delete_file():
    user_input = input("是否删除文件(y/n)：")
    if user_input == "y":
        print("成功删除文件file.txt")
    elif user_input == "n":
        print("取消删除文件file.txt")
    else:
        delete_file()

delete_file()