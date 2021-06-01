# coding:utf-8

# 1. while循环
# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number += 1
#
# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program."
#
# message = ''
# while message != 'quit':
#     message = input(prompt)
#
#     if message != 'quit':
#         print(message)

# 2. 使用标志
# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "
# active = True
# while active:
#     message = input(prompt)
#
#     if message == 'quit':
#         active = False
#     else:
#         print(message)

# 3. 使用break
# prompt = "\nPlease enter the name of a city you have visited:"
# prompt += "\n(Enter 'quit' when you are finished.) "
#
# while True:
#     city = input(prompt)
#
#     if city == 'quit':
#         break
#     else:
#         print("I'd love to go to " + city.title() + "!")


# 4. 在循环中使用continue
# current_number = 0
# while current_number < 10:
#     current_number += 1
#     if current_number % 2 == 0:
#         continue
#
#     print(current_number)  # 1 3 5 7 9

# 5. 避免无限循环
# x = 1
# while x <= 5:
#     print(x)
#     # x += 1

# 6. 使用while循环来处理列表和字典

# 6.1 在列表之间移动元素
# 首先，创建一个待验证用户列表
# 和一个用于存储已验证用户的空列表
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# 验证每个用户，直到没有未验证用户为止
# 将每个经过验证的列表都移到已验证用户列表中
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

# 显示所有已验证的用户
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

print(confirmed_users)

# 6.2 删除包含特性值的所有列表元素，包含重复项
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

# 6.3 使用用户输入在填充字典
responses = {}

# 设置一个标志，指出调查是否继续
polling_active = True

while polling_active:
    # 提示输入被调查之的名字和回答
    name = input('\nWhat is your name')
    response = input("Which mountain would you like to climb someday?")

    # 将答卷存储在字典里
    responses[name] = response

    # 看看是否还有人要参与调查
    repeat = input('Would you like to let other person respond?(yes,no)')
    if repeat == 'no':
        polling_active = False

# 调查结束，显示结果
print('\n--- Poll Results ---')
for name, response in responses.items():
    print(name + 'would like to climb ' + response + ".")


