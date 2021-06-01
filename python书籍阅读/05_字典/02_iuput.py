# coding:utf-8

# 1. input
# message = input('Tell me somthing,and I will repeat it back to you:')
# print(message)
#
# name = input('Please enter your name.')
# print('Hello, ' + name + '!')

# 1.1 提示超过一行，建议存在变量中再传入
# prompt = 'if you tell us who you are , we can personalize the messages you see.'
# prompt += '\nWhat is your first name?'
#
# name = input(prompt)
# print('\nHello, ' + name + '!' )

# 1.2 使用int()来获取数值的输入,但是这个数字不可用来使用，只可打印
# age = input('How old are you?')
# print(age)
# 不可将存储在字符串中的'21'与数字18 进行比较
# age >= 18  # TypeError: '>=' not supported between instances of 'str' and 'int'

# 解决上述问题,使用int()
# age = input('How old are you?')
# age = int(age)
# print(age >= 18)

# 场景问题
# 如何在实际程序中使用函数int() 呢？请看下面的程序，它判断一个人是否满足坐过山车的身高要求
# height = input('How tall are you, in inches?')
# height = int(height)
#
# if height >= 36:
#     print("\nYou're tall enough to ride!")
# else:
#     print("\nYou'll be able to ride when you're a little older.")

# 1.3 求模运算符
print(4 % 3)
print(5 % 3)
print(6 % 3)

number = input("Enter a nuber, and i'will tell you if it's even or odd:")
number = int(number)

if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")

