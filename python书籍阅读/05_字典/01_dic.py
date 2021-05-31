# coding:utf-8
alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

# 1. 使用字典，键值对

# 1.1 修改字段
alien_0 = {'color': 'green', 'points': 5}
alien_0 = {'color': 'green'}

# 1.2 访问字典中的值
alien_0 = {'color': 'green'}
print(alien_0['color'])

# 1.3 添加键值对
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# 1.4 创建一个空字典
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

# 1.5 修改字典中的值
alien_0 = {'color': 'green'}
print('the alien is ' + alien_0['color'] + '.')

alien_0['color'] = 'yellow'
print('the alien is ' + alien_0['color'] + '.')

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # 这个外星人的速度一定很快
    x_increment = 3

# 新位置等于老位置加上增量
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))

# 1.6 删除键值对,删除的键值对永远消失
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['color']
print(alien_0)

# 1.7 由类似对象组成的字典
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

# 2. 遍历字典

# 2.1 遍历所有的键值对
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for key, value in favorite_languages.items():
    print('\nKey:' + key)
    print('Value:' + value)

for k, v in favorite_languages.items():
    print('\nKey:' + k)
    print('\nValue:' + v)

# 2.1.1 遍历场景
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is" + language.title() + ".")

# 2.2 遍历字典中的所有键
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

# “for name in favorite_languages.keys(): 替换为for name in favorite_languages: ，输出将不变”
#
for name in favorite_languages.keys():
    print(name.title())

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'phil': 'python',
    'edward': 'ruby',

}

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print("  Hi " + name.title() +
              ", I see your favorite language is " +
              favorite_languages[name].title() + "!")

# 是否所有人都接受了调查
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'phil': 'python',
    'edward': 'ruby',

}

if 'erin' not in favorite_languages.keys():
    print('Erin,please take our poll!')

# 2.3 “按顺序遍历字典中的所有键”
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'phil': 'python',
    'edward': 'ruby',
}

for name in sorted(favorite_languages.keys()):
    print(name.title() + ",thank you for taking the poll.")

# 2.4 “遍历字典中的所有值”
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'phil': 'python',
    'edward': 'ruby',
}

print('The following languages have been mentioned:')
for language in favorite_languages.values():
    print(language.title())

# 2.5 取值并用set来去重
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'phil': 'python',
    'edward': 'ruby',
}

print('The following languages have been mentioned:')
for language in set(favorite_languages.values()):
    print(language.title())

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'phil': 'python',
    'edward': 'ruby',
}

for name in favorite_languages.keys():
    if name in favorite_languages.keys():
        print(name + '感谢你的参加')
    else:
        print('请参加邀请')

# 2.6 嵌套

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

# 使用range生成多个

# 创建一个用于存储外星人的空列表
aliens = []

# 创建30个绿色的外星人
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# 显示前5个外星人
for alien in aliens[:5]:
    print(alien)
print('...')

# 显示创建了多少个外星人
print('Total number of aliens: ' + str(len(aliens)))

# 新思想
# 创建一个用于存储外星人的空列表
aliens = []
# 创建30个绿色的外星人
for alien_number in range(0, 30):
    new_alien = {'color': 'green', 'point': 5, 'speed': 'slow', }
    aliens.append(new_alien)

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
# 显示前五个外星人
for alien in aliens[0:5]:
    print(alien)
print('....')

# 2.7 在字典中存储列表


# 存储所点比萨的信息
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

# 概述所点的披萨
print("You odered a " + pizza['crust'] + '-crust pizza ' + 'with the following toppings:')

for topping in pizza['toppings']:
    print('\t' + topping)


# 不同的人
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

for username,user_info in users.items():
    print('\nUsername:' + username)
    full_name = user_info['first'] + '' + user_info['last']
    location = user_info['location']

    print('\tFull name: ' + full_name.title())
    print('\tLocation: ' + location.title())
