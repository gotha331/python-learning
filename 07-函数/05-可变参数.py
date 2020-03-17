# Files: 
# Author：jiang liu
# Date ：2020/3/13 10:28
# Tool ：PyCharm


# 可变参数 两种情况：
# 1. *param(一个星号)，将多个参数收集到一个"元组"对象中
# 2. **param(两个星号)，将多个参数收集到一个"字典"中


def f1(a, b, *c):
    print(a, b, c)


f1(10, 20, 30, 40)  # 10 20 (30, 40)


def f2(a, b, **c):
    print(a, b, c)


f2(10, 20, name="shuai", age=25)  # 10 20 {'name': 'shuai', 'age': 25}


def f3(a, b, *c, **d):
    print(a, b, c, d)


f3(10, 20, 30, 40, 50, name="shuai", age=25)  # 10 20 (30, 40, 50) {'name': 'shuai', 'age': 25}
