# coding:utf-8

travel_place = ['beijing', 'shanxi', 'nanjing', 'ain']
print(travel_place)

# sorted字母顺序,不修改原数组
travel_place_one = sorted(travel_place);
print('sorted字母顺序')
print(travel_place_one)
print('原数组未变')
print(travel_place)  # 未变

# 反序
travel_place_Two = sorted(travel_place, reverse=True)
print('sorted反转')
print(travel_place_Two)
print('原数组未变')
print(travel_place)

# reverse,无返回值，修改原始数组
travel_place_Three = travel_place.reverse() # 这一行无返回值
print('reverse以后数组')
print(travel_place_Three)  # None
print(travel_place)

len = len(travel_place)
print(len) # 4




