# coding:utf-8

# 1.使用方法修改字符串大小写
name = 'ada lovelace'
# title方法是以首字母大写方法来输出字符
print(name.title())

# 全大写或者全小写
name = 'adaq lovelace'
print(name.upper())
print(name.lower())

# 2.合并拼接字符串
first_name = 'ada'
last_name = 'lovelace'
full_name = first_name + '' + last_name
print(full_name)

# 3.使用制表符或换行符来添加空白
print('Python')
print('\tPython')
print('Languages:\nPython\nC\npython\nJavaScript')

# 4.删除空白
favorite_language = 'python '
print(favorite_language)
favorite_language.rstrip()
print(favorite_language)
print(favorite_language)

# 永久删除空格，需存存回变量中
favorite_language = 'hello '
favorite_language = favorite_language.rstrip()
print(favorite_language)

'''
    1. rstrip(): 删除末尾空格，需要存回变量中，否则只是临时删除
    2. lstrip(): 删除开头空格
    3. strip(): 删除两端空格
'''
