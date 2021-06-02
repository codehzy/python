from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

for name, language in favorite_languages.items():
    print(name.title() + " 's favorite language is " + language.title() + ".")

# 模块random 包含以各种方式生成随机数的函数，其中的randint() 返回一个位于指定范围内的整数，例如，下面的代码返回一个1~6内的整数
from random import randint

class Die():
    def __init__(self):
        self.sides = 6

    def update_sides(self,change_side):
        self.sides = change_side

    def roll_die(self):
        print(randint(1,6))


six_die = Die()
for cur in range(1,11):
    six_die.roll_die()

six_die.update_sides(10)
ten_die = Die()

ten_die.update_sides(20)
twenty_die = Die()

for cur in range(1,11):
    print('十面的骰子投10次')
    ten_die.roll_die()
    print('二十面的骰子十次')
    twenty_die.roll_die()