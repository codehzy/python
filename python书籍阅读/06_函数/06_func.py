# coding:utf-8

# 1. 定义函数
def greet_user():
    """"显示简单的问候语"""
    print("Hello")


greet_user()


# 1.1 向函数传递信息
def greet_user(username):
    """显示简单的问候语"""
    print("Hello, " + username.title() + "!")


greet_user('jesse')


# 1.2 实参和形参

# 1.3 传递实参

# 1.3.1 位置参数
def describe_pet(amimal_type, pet_name):
    """显示宠物的信息"""
    print('\nI have a ' + amimal_type + ".")
    print("My " + amimal_type + " 's name is " + pet_name.title() + ".")


describe_pet('Hicky', 'Marry')


# 1.3.2.1 一个函数多次调用
def describe_pet(amimal_type, pet_name):
    """显示宠物的信息"""
    print('\nI have a ' + amimal_type + ".")
    print("My " + amimal_type + " 's name is " + pet_name.title() + ".")


describe_pet('Hicky', 'Marry')
describe_pet('dog', 'willie')


# 1.3.2.2 位置实参的顺序很重要

# 1.3.2.3 关键字实参
def describe_pet(animal_type, pet_name):
    """显示宠物信息"""
    print('\nI have a ' + animal_type + ".")
    print("My " + animal_type + " 's name is " + pet_name.title() + ".")


describe_pet(animal_type='hyic', pet_name='hello')
describe_pet(pet_name='hello', animal_type='hyic')


# 1.3.2.4 默认值,注意顺序，默认参数只能在后面
def describe_pet(animal_type, pet_name='dog'):
    """显示宠物信息"""
    print('\nI have a ' + animal_type + ".")
    print("My " + animal_type + " 's name is " + pet_name.title() + ".")


describe_pet(animal_type='hicky')
# 最简单调用
describe_pet('code')
# 传递参数，则默认值失效,按照传递的参数来
describe_pet(animal_type='hicky', pet_name='cat')


# 1.4 等效函数调用
def describe_pet(animal_type, pet_name='dog'):
    describe_pet(animal_type='hicky', pet_name='cat')
    describe_pet('harry', 'hamster')


# 1.5 返回值
def get_formatted_name(first_name, last_name):
    """返回简洁的姓名"""
    full_name = first_name + " " + last_name
    return full_name.title()


muician = get_formatted_name('jimi', 'hendrix')
print(muician)


# 1.6 可选参数
def get_formatted_name(first_name, last_name, middle_name=' '):
    """返回整洁的姓名"""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name + ' '
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('jhon', 'hooker', 'lee')
print(musician)


# 1.7 返回字典
def build_person(first_name, last_name):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {'first': first_name, 'last': last_name}
    return person


musician = build_person('jimi', 'hendrix')
print(musician)


def build_person(first_name, last_name, age=''):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


musician = build_person('jimi', 'hendrix', age=27)
print(musician)


# 1.8 结合使用函数和while循环
def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name + ' ' + last_name
    return full_name.title()


# 这是一个无线循环
# while True:
#     print("\nPlease tell me your name:")
#     f_name = input("First name: ")
#     l_name = input("Last name: ")
#
#     formatted_name = get_formatted_name(f_name, l_name)
#     print("\nHello, " + formatted_name + "!")


# 使用break语句退出循环

# def get_full_name(f_name, l_name):
#     full_name = f_name + " " + l_name
#     return full_name.title()
#
#
# while True:
#     print("请告诉我你的名字:")
#     print("如果想退出请输入q")
#
#     f_name = input("First name: ")
#     if f_name == 'q' or 'Q':
#         break
#     l_name = input("Last name: ")
#     if l_name == 'q' or 'Q':
#         break
#
#     formatted_name = get_formatted_name(f_name, l_name)
#     print('\nHello, ' + formatted_name + "!")


# 1.9 传递列表

def greet_users(names):
    """向列表中的每位用户都发出简单的问候"""
    for name in names:
        msg = 'Hello, ' + name.title() + '!'
        print(msg)


usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

# 2. 在函数中修改列表

# 首先创建一个列表，其中包含一些要打印的设计
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

# 模拟打印每个设计，直到没有未打印的设计为止
# 打印每个设计后，都将其移到列表completed_models中
while unprinted_designs:
    current_design = unprinted_designs.pop()

    # 模拟根据设计制作3D打印模型的过程
    print("Printing model: " + current_design)
    completed_models.append(current_design)

# 显示打印好的所有模型
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)

##### 改写方法代码为函数
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []


def print_models(unprinted_designs, completed_models):
    """
    :param unprinted_designs:
    :param completed_models:
    :return:
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        print('Printing model: ' + current_design)
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """显示打印好的所有模型"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)


# 2.1　禁止函数修改列表
# 调用函数的时候可以使用切片来获得传入参数的副本

# 2.2 传递任意数量的实参
def make_pizza(*toppings):
    """打印顾客点的所有配料"""
    print(toppings)


make_pizza('perpo')
make_pizza('perpo', 'hello')
make_pizza('perpo', 'hello', 'dsa')


# 2.3 结合使用位置参数和任意数量参数
# python先匹配位置实参和关键字实参，再讲余下的实参收集到最后一个形参中
def make_pizza(size, *toppings):
    """概述要制作的比萨"""
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print('- ' + topping)


make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# 2.4 使用任意数量的关键字实参
def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)

# 2.5 将函数存储在模块中
# 看pizza.py文件和making_pizzas.py文件的关联
import pizza
# 按照需要函数导入
# from modules_name import make_pizza

# 2.6 使用as给函数指定别名
# from module_name import function_name as fn

# from pizza import make_pizza as mp
# mp(16,'pepole')

# 2.7 给模块指定别名
# import module_name as mn

# 2.8 导入模块中的所有函数
from pizza import *

make_pizza(16, 'asdx')
