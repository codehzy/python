# coding:utf-8

# 1. if语句
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# 1.1 检查书否相等,检查是否相等不考虑大小写
car = 'bmw'
car == 'bmw'  # true

# 1.2 检查是否不相等, !=

requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print('Hold the anchovies')

# 1.3 数字比较
age = 18
age == 18  # ture

# 1.3.1 检查数字是否不等
answer = 17
if (answer != 42):
    print("That is not the correct answer. Please try again!")

age = 19
age < 20
age <= 21
age > 21
age >= 21

# 1.4 检查多个条件

# 1.4.1 and 检查多个条件
age_0 = 22
age_1 = 18
age_0 >= 21 and age_1 >= 21  # false

age_1 = 22
age_0 >= 21 and age_1 >= 21  # true

# 1.4.2 or 检查多个条件
age_0 = 22
age_1 = 18
age_0 >= 21 or age_1 >= 21  # true

age_1 = 22
age_0 >= 21 or age_1 >= 21  # true

# 1.4.3 检查特定值是否包含在列表中 , in
requested_toppings = ['mushrooms', 'onions', 'pineapple']
'mushrooms' in requested_toppings  # true
'pepperoni' in requested_toppings  # false

# 1.4.4 “检查特定值是否不包含在列表中 , not in
user = 'marie'
banned_users = ['andrew', 'carolina', 'david']

if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")

# 1.5 布尔表达式
game_active = True
can_edit = False

# 2. 简单if语句
# if conditional_test:
#     do something

age = 19
if age > 18:
    print('You are old enough to vote')
    print('Have you registered to vote yet?')

# 2.1 if-else语句
age = 17
if age >= 18:
    print("You are old enough to vote")
else:
    print('Please register to vote as soon as you turn 18!')

# 2.2 if-elif-else结构,可用多个elif,可省略else代码块
age = 12
if age < 4:
    print('Your admission cost is $0.')
elif age < 18:
    print('Your admission const is $5.')
elif age < 30:
    print('Your admission const is $8.')
else:
    print('Your admission cost is $10.')

# 3. 检查特殊元素
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    print('Adding ' + requested_topping + '.')
print('\nFinished making you pizza')

# 3.1 确定列表不为空
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print('Adding ' + requested_topping + '.')
    print('\nFinish making your pizza')
else:
    print('Are you sure you want a plain pizza?')

# 3.2 使用多个列表
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print('Adding ' + requested_topping + '.')
    else:
        print('Sorry, we donot  have ' + requested_topping + '.')
print('\nFinished making your pizza')
