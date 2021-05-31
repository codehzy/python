age = 12
age_1 = 22
if age > 10 or age_1 < 20:
    print("True")

message = ['hzy', 'cwh', 'xwz']
if 'hzy' in message:
    print('hzy存在')

if 'ct' not in message:
    print('ct不存在')

# “5-3 外星人颜色#1 ：假设在游戏中刚射杀了一个外星人，请创建一个名为alien_color 的变量，并将其设置为'green' 、'yellow' 或'red' 。
#
# 编写一条if 语句，检查外星人是否是绿色的；如果是，就打印一条消息，指出玩家获得了5个点。
#
# 编写这个程序的两个版本，在一个版本中上述测试通过了，而在另一个版本中未通过（未通过测试时没有输出）。”
#
alien_color = 'green'
if (alien_color == 'green'):
    print('该玩家获得5个点')

# “5-4 外星人颜色#2 ：像练习5-3那样设置外星人的颜色，并编写一个if-else 结构。
#
# 如果外星人是绿色的，就打印一条消息，指出玩家因射杀该外星人获得了5个点。
#
# 如果外星人不是绿色的，就打印一条消息，指出玩家获得了10个点。
#
# 编写这个程序的两个版本，在一个版本中执行if 代码块，而在另一个版本中执行else 代码块。”
#
alien_color = 'green'
if (alien_color == 'green'):
    print('该玩家获得5个点')
else:
    print('该玩家获得10个点')

# 题目省略自己看代码
alien_color = 'yellow'
if (alien_color == 'green'):
    print('该玩家获得5个点')
elif (alien_color == 'yellow'):
    print('该玩家获得10个点')
else:
    print('该玩家获得15个点')

alien_color = 'black'
if (alien_color == 'green'):
    print('该玩家获得5个点')
elif (alien_color == 'yellow'):
    print('该玩家获得10个点')
elif (alien_color == 'black'):
    print('该玩家获得13个点')
else:
    print('该玩家获得15个点')

# “5-7 喜欢的水果 ：创建一个列表，其中包含你喜欢的水果，再编写一系列独立的if 语句，检查列表中是否包含特定的水果。
#
# 将该列表命名为favorite_fruits ，并在其中包含三种水果。
#
# 编写5条if 语句，每条都检查某种水果是否包含在列表中，如果包含在列表中，就打印一条消息，如“You really like bananas!”。”
#
# 摘录来自: [美] Eric Matthes. “Python编程：从入门到实践。” Apple Books.

favorite_fruits = ['mongo', 'apple', 'watermelons', 'pear']
if (
        'mongo' in favorite_fruits and 'apple' in favorite_fruits and 'watermelons' in favorite_fruits and 'pear' in favorite_fruits):
    print('You really like banans!')

# “5-8 以特殊方式跟管理员打招呼 ：创建一个至少包含5个用户名的列表，且其中一个用户名为'admin' 。想象你要编写代码，在每位用户登录网站后都打印一条问候消息。遍历用户名列表，并向每位用户打印一条问候消息。
#
# 如果用户名为'admin' ，就打印一条特殊的问候消息，如“Hello admin, would you like to see a status report?”。
#
# 否则，打印一条普通的问候消息，如“Hello Eric, thank you for logging in again”。”
#
# 摘录来自: [美] Eric Matthes. “Python编程：从入门到实践。” Apple Books.
user_name = 'admin'
users = ['admin', 'teacher', 'student', 'body', 'girl']
if user_name == 'admin':
    print("hello " + user_name + ' would you like to see a status reports?')
else:
    print('Hello Eric,thank you for logging in again')

# “5-9 处理没有用户的情形 ：在为完成练习5-8编写的程序中，添加一条if 语句，检查用户名列表是否为空。
#
# 如果为空，就打印消息“We need to find some users!”。”
# 删除列表中的所有用户名，确定将打印正确的消息。
user_name = 'admin'
users = ['admin', 'teacher', 'student', 'body', 'girl']
if users:
    if user_name == 'admin':
        print("hello " + user_name + ' would you like to see a status reports?')
    else:
        print('Hello Eric,thank you for logging in again')

# “5-10 检查用户名 ：按下面的说明编写一个程序，模拟网站确保每位用户的用户名都独一无二的方式。
#
# 创建一个至少包含5个用户名的列表，并将其命名为current_users 。
#
# 再创建一个包含5个用户名的列表，将其命名为new_users ，并确保其中有一两个用户名也包含在列表current_users 中。
#
# 遍历列表new_users ，对于其中的每个用户名，都检查它是否已被使用。如果是这样，就打印一条消息，指出需要输入别的用户名；否则，打印一条消息，指出这个用户名未被使用。
#
# 确保比较时不区分大消息；换句话说，如果用户名'John' 已被使用，应拒绝用户名'JOHN' 。
#
current_users = ['admin', 'teacher', 'student', 'body', 'girl']
new_users = ['human', 'person', 'male', 'female', ]
for value in new_users:
    if value.lower() == 'human' or value.lower() == 'person' or value.lower() == 'female' or value.lower() == 'person':
        print('用户名被使用，请输入别的用户名')
    else:
        print('这个用户名没有被使用')

# “5-11 序数 ：序数表示位置，如1st和2nd。大多数序数都以th结尾，只有1、2和3例外。
#
# 在一个列表中存储数字1~9。
#
# 遍历这个列表。
#
# 在循环中使用一个if-elif-else 结构，以打印每个数字对应的序数。输出内容应为1st 、2nd 、3rd 、4th 、5th 、6th 、7th 、8th 和9th ，但每个序数都独占一行。”
#
numbers = []
for value in range(1, 10):
    numbers.append(value)
print(numbers)
for value in numbers:
    if value == 1:
        print(str(value) + 'st')
    elif value == 2:
        print(str(value) + 'nd')
    elif value == 3:
        print(str(value) + 'rd')
    else:
        print(str(value) + 'th')
print('循环输出结束')
