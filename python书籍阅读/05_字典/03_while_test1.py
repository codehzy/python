# coding:utf-8

# 7-8 熟食店 ：创建一个名为sandwich_orders 的列表，在其中包含各种三明治的名字；再创建一个名为finished_sandwiches 的空列表。遍历列表sandwich_orders ，对于其中的每种三明治，都打印一条消息，如I made your tuna sandwich ，并将其移到列表finished_sandwiches 。所有三明治都制作好后，打印一条消息，将这些三明治列出来。
sandwich_orders = ['nice', 'beauty', 'pretty']
finished_sandwiches = []

while sandwich_orders:
    new_sandwich_order = sandwich_orders.pop()
    print(new_sandwich_order.title())

    finished_sandwiches.append(new_sandwich_order)
print(finished_sandwiches.sort(reverse=True))
