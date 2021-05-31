# 1. 修改、添加和删除元素

# 1.1 修改列表元素
motorcycles = ['honda', 'yamada', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

# 1.2 列表中添加元素

# 1.2.1 末尾添加,append,不影响列表中其他的所有元素
motorcycles = ['honda', 'yamada', 'suzuki']
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)

# 1.3 在列表中插入元素
motorcycles = ['honda', 'yamada', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)

# 1.4 使用del语句删除元素
motorcycles = ['honda', 'yamada', 'suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)

# 1.4.1 删除任意位置元素
motorcycles = ['honda', 'yamada', 'suzuki']
print(motorcycles)
del motorcycles[1]
print(motorcycles)

# 1.4.2 使用del语句将值从列表中删除,再也无法访问。pop方法修改原数组，返回pop出去的值
motorcycles = ['honda', 'yamada', 'suzuki']
print(motorcycles)  # ['honda', 'yamada', 'suzuki']
popped_motorcycle = motorcycles.pop()
print(motorcycles)  # ['honda', 'yamada']
print(popped_motorcycle)  # suzuki

# 1.4.3 弹出列表中任何位置处的元素
motorcycles = ['honda', 'yamada', 'suzuki']
first_owned = motorcycles.pop(0)
print('The first a ' + first_owned.title() + '.')

# 1.4.4 根据值删除元素,改变列表,remove只会删除第一个指定值，删除多个需要循环
motorcycles = ['honda', 'yamada', 'suzuki']
print(motorcycles)

motorcycles.remove('yamada')
print(motorcycles)

# 1.5 sort()对列表进行永久性排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

# 反序
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

# 1.5.1 使用sorted()进行临时排序，并且不影响原数组，同样可使用reverse来反序
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(sorted(cars))

print('\nHere is the original list again:')
print(cars)

# 1.5.2 倒着打印列表,reverse不是按字母相反，而是反转列表元素的排列顺序。
# 此方法永久性的修改列表元素的排列是顺序，但是可以再次调用reverse来反转回来
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()
print(cars)

# 1.5.3 确定列表的长度
cars = ['bmw', 'audi', 'toyota', 'subaru']
length = len(cars)
print(length) # 4

# 永久排序reverse,临时排序sorted
