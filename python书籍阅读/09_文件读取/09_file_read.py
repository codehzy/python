# coding:utf-8

# 读取文件
with open('test.txt') as file_object:
    contents = file_object.read()
    # print(contents)

# 文件路径
with open('text_files/file_name.txt') as file_object:
    contents = file_object.read()
    # print(contents)

# 逐行读取
filename = 'text_files/file_name.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line)

# 创建一个包含文件各行内容的列表
filename = 'text_files/file_name.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

print(lines)

for line in lines:
    print(line.rstrip())

# 使用文件内容
filename = 'text_files/file_name.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

string = ''
for line in lines:
    string += line.strip()

print(string)
print(len(string))

