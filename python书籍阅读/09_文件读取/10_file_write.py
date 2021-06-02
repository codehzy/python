# coding:utf-8

# 写入文件
filename = 'write.txt'

with open(filename, 'w') as file_object:
    file_object.write('I love programming')

# 写入多行
filename = 'write.txt'

with open(filename, 'w') as file_object:
    file_object.write('I love programming')
    file_object.write('\nI love creating new games')

# 附加到文件
filename = 'writeone.txt'
with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets \n")
    file_object.write('I love creating apps that can run in a brower \n')

# 处理读取文件的错误
filename = 'text_files/file_name.txt'

try:
    with open(filename) as file_object:
        lines = file_object.readlines()

except FileNotFoundError:
    string = ''
    for line in lines:
        string += line.strip()

    print(string)
    print(len(string))
