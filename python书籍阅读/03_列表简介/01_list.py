bicycles = ['hzy', 'hello', 'boy']
print(bicycles)

# 1.访问列表元素
print(bicycles[0])
print(bicycles[0].title())

# 2.索引从0而不是1开始
bicycles = ['hzy', 'hello', 'boy']
print(bicycles[1])
print(bicycles[2])

# 最后一个元素
print(bicycles[-1])

# 3.使用列表中的各个值
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = 'my first bicycle was a ' + bicycles[0].title() + '.'
print(message)
