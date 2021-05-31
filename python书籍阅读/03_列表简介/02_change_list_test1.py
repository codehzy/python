# “3-4 嘉宾名单 ：如果你可以邀请任何人一起共进晚餐（无论是在世的还是故去的），你会邀请哪些人？请创建一个列表，其中包含至少3个你想邀请的人；然后，使用这个列表打印消息，邀请这些人来与你共进晚餐。”

dinner_person = ['hzy', 'xwz', 'lhs']
message = 'i will invite: ' + dinner_person[0] + ' ' + dinner_person[1] + ' ' + dinner_person[2]
print(message)

# “3-5 修改嘉宾名单 ：你刚得知有位嘉宾无法赴约，因此需要另外邀请一位嘉宾。
#
# 以完成练习3-4时编写的程序为基础，在程序末尾添加一条print 语句，指出哪位嘉宾无法赴约。
#
# 修改嘉宾名单，将无法赴约的嘉宾的姓名替换为新邀请的嘉宾的姓名。
#
# 再次打印一系列消息，向名单中的每位嘉宾发出邀请。”
#
dinner_person = ['hzy', 'xwz', 'lhs']
dinner_person.pop(2)
print(dinner_person)
dinner_person.insert(1, 'ct')
dinner_person.insert(0, 'tsm')
dinner_person.append('cwh')
print(dinner_person)

# “3-7 缩减名单 ：你刚得知新购买的餐桌无法及时送达，因此只能邀请两位嘉宾。
#
# 以完成练习3-6时编写的程序为基础，在程序末尾添加一行代码，打印一条你只能邀请两位嘉宾共进晚餐的消息。
#
# 使用pop() 不断地删除名单中的嘉宾，直到只有两位嘉宾为止。每次从名单中弹出一位嘉宾时，都打印一条消息，让该嘉宾知悉你很抱歉，无法邀请他来共进晚餐。
#
# 对于余下的两位嘉宾中的每一位，都打印一条消息，指出他依然在受邀人之列。
#
# 使用del 将最后两位嘉宾从名单中删除，让名单变成空的。打印该名单，核实程序结束时名单确实是空的。”
#
dinner_person = ['tsm', 'hzy', 'ct', 'xwz', 'cwh']
dinner_person.pop()
dinner_person.pop()
dinner_person.pop()
print(dinner_person)
dinner_person.remove('hzy')
dinner_person.remove('tsm')
print(dinner_person)
