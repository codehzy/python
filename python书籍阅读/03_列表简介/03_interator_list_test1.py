# coding:utf-8
import datetime

dogs = ['Husky', 'golden', 'welsh']
for dog_name in dogs:
    print('I like:' + dog_name)
print('this is my favorite dogs')

dogs = ['Husky', 'golden', 'welsh']
for dog_name in dogs:
    print('A dog would make a great pet')
print("Any if these animals would like make a great pet!")

# 数到20 ：使用一个for 循环打印数字1~20（含）。
for value in range(1, 21):
    print(value)

# 一百万 ：创建一个列表，其中包含数字1~1 000 000，再使用一个for 循环将这些数字打印出来（如果”“输出的时间太长，按Ctrl + C停止输出，或关闭输出窗口）。
# million = []
# for value in range(1, 1000001):
#     million.append(value)
# print(million)

# for value in million:
#     print(value)

# “计算1~1 000 000的总和 ：创建一个列表，其中包含数字1~1 000 000，再使用min() 和max() 核实该列表确实是从1开始，到1 000 000结束的。另外，对这个列表调用函数sum() ，看看Python将一百万个数字相加需要多长时间。
# million = []
# for value in range(1, 1000001):
#     million.append(value)
# print(million)
# sum_million = sum(million)
# print(sum_million)

# 通过给函数range() 指定第三个参数来创建一个列表，其中包含1~20的奇数；再使用一个for 循环将这些数字都打印出来。
# for value in range(1,20,2):
#     print(value)

# 3的倍数 ：创建一个列表，其中包含3~30内能被3整除的数字；再使用一个for 循环将这个列表中的数字都打印出来。
# thirty = []
# for value in range(3,30,3):
#     thirty.append(value)
# print(thirty)
#
# for value in thirty:
#     print(value)

# “立方 ：将同一个数字乘三次称为立方。例如，在Python中，2的立方用2**3 表示。请创建一个列表，其中包含前10个整数（即1~10）的立方，再使用一个for 循环将这些立方数都打印出来。”
# ten = []
# for value in range(1,11):
#     temp = value ** 3
#     ten.append(temp)
# print(ten)


# 4-9 立方解析 ：使用列表解析生成一个列表，其中包含前10个整数的立方
# number = [value ** 3 for value in range(1, 11)]
# print(number)

# “4-10 切片 ：选择你在本章编写的一个程序，在末尾添加几行代码，以完成如下任务。
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print('The first three items in list are')
print(players[0:3])
print(players[1:4]) # 中间三个
print(players[2:5]) # 后三个元素
print(players[-3:]) # 后三个元素


travel_place = ['beijing', 'shanxi', 'nanjing', 'ain']
travel_place_one = travel_place[:]
print(travel_place_one)
travel_place.append('xian')
travel_place_one.append('shanxi')
print('this i diff area')
# ['beijing', 'shanxi', 'nanjing', 'ain', 'xian']
print(travel_place)
# ['beijing', 'shanxi', 'nanjing', 'ain', 'shanxi']
print(travel_place_one)


