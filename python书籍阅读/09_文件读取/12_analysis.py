# coding:utf-8

# filename = 'book.txt'
#
# with open(filename) as file_object:
#     lines = file_object.readlines()
#
# print(lines)


# 计算文件包含多少个单词
filename = 'book.txt'

try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = 'Sorry, the file ' + filename + 'does not exist.'
    print(msg)
else:
    # 计算问价大致包含多少个单词
    words = contents.split()
    print(words)
    num_words = len(words)
    print("The file " + filename + " has about " + str(num_words) + " words.")
