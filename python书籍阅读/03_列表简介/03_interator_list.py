# coding:utf-8

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

# 1. 在for循环中执行更多操作
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
# Alice, that was a great trick!
# David, that was a great trick!
# Carolina, that was a great trick!

# 2. 函数range()
for value in range(1, 5):
    print(value)
    # 1 2 3 4

for value in range(1, 6):
    print(value)
    # 1 2 3 4 5

# 2.1. 使用range()配合list()创建数字函数
numbers = list(range(1, 6))
print(numbers)  # [1,2,3,4,5]

# 2.2 使用range()指定步长
even_numbers = list(range(2, 11, 2))
print(even_numbers)  # [2, 4, 6, 8, 10]

# 2.3 常见一个list包含前十个数的平方
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 2.4 “对数字列表执行简单的统计计算”
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
min_number = min(digits)
print(min_number)

max_number = max(digits)
print(max_number)

sum_number = sum(digits)
print(sum_number)

# 3. 列表解析

# 3.1 使用列表解析创建平方数列表
squares = [value ** 2 for value in range(1,11)]
print(squares)


# 4. 使用列表的一部分

# 4.1 切片,不影响原列表
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3]) # index 0 -> index 3
print(players[1:])  # 到index:1 -> 末尾
print(players[-3:]) # 最后三个
print(players)


# 4.2 遍历切片
players = ['charles', 'martina', 'michael', 'florence', 'eli']
for player in players[:3]:
    print(player.title())
# Charles
# Martina
# Michael

# 4.3 复制列表
players = ['charles', 'martina', 'michael', 'florence', 'eli']
new_players = players[:]
print(new_players)