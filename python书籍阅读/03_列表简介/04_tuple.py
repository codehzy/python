# 元组
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# 1. 元组中禁止修改
# dimensions[0] = 250 # 报错，元组禁止修改

# 2. 遍历元组中所有值
dimensions = (200, 50, 100)
for dimension in dimensions:
    print(dimension)

# 3. 修改元组变量，不能修改元组元素，但是可以给存储元组的变量赋值
dimensions = (200, 50, 100)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (100,400)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
