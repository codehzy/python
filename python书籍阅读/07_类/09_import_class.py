# coding:utf-8

# 导入方法一
# from car import Car
# from car import ElectricCar

# 导入方法二
# from car import Car, ElectricCar

# my_new_car = Car('audi', 'a4', 2016)
# print(my_new_car.get_descriptive_name())
#
# my_new_car.odometer_reading = 23
# my_new_car.read_odometer()
#
# my_tesla = ElectricCar('tesla', 'model s', 2016)
#
# print(my_tesla.get_descriptive_name())
# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()

# 导入方法三

import car

my_new_car = car.Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

my_tesla = car.ElectricCar('tesla', 'model s', 2016)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

# 导入方法四： 导入模块中的所有类
# for module_name import *

# 模块一
# car

# class Car():
#     --snip--

# 模块二
# electric_car

# from car import Car
# class Battery():
#     --snip--
#
# class ElectricCar(Car):
#     --snip--



