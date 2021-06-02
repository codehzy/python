# coding:utf-8

# 捕获异常
try:
    print(5 / 0)
except ZeroDivisionError:
    print("You can't divide by zero")

# 妥善处理异常
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_name = input("\n First number:")
    if first_name == 'q':
        break
    second_number = input("Second number:")
    if second_number == 'q':
        break
    try:
        answer = int(first_name) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero")
    else:
        print(answer)
