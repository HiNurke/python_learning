file_path = "./example.txt"
try:
    file = open(file_path, 'r')
    content = file.read()
    print(content)
except FileNotFoundError:
    print("文件不存在")

new_file_path = "./example2.txt"
data = "这是写入文件的内容"
new_file = open(new_file_path, 'w')
new_file.write(data)

log_file_path = './log.txt'
log_entry = "\n这是一条新的日志信息"
with open(log_file_path, 'a') as log_file:
    log_file.write(log_entry)