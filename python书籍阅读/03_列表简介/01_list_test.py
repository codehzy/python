# “3-1 姓名： 将一些朋友的姓名存储在一个列表中，并将其命名为names 。依次访问该列表中的每个元素，从而将每个朋友的姓名都打印出来”
friends = ['hzy', 'cwh', 'xwz', 'lhs']
print(friends[0])
print(friends[1])
print(friends[2])
print(friends[3])

# “3-2 问候语： 继续使用练习3-1中的列表，但不打印每个朋友的姓名，而为每人打印一条消息。每条消息都包含“相同的问候语，但抬头为相应朋友的姓名。”
print(friends[0] + ": hello my name is " + friends[0])
print(friends[1] + ": hello my name is " + friends[1])
print(friends[2] + ": hello my name is " + friends[2])
print(friends[3] + ": hello my name is " + friends[3])

# “3-3 自己的列表： 想想你喜欢的通勤方式，如骑摩托车或开汽车，并创建一个包含多种通勤方式的列表。根据该列表打印一系列有关这些通勤方式的宣言，如“I would like to own a Honda motorcycle”。”
move = ['bicycle', 'motorcycle', 'underground']
print('i like own a :' + move[2])

