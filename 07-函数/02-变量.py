# Files: 
# Author：jiang liu
# Date ：2020/3/12 14:20
# Tool ：PyCharm


a = 3  # 全局变量

print(a)


def test01():
    b = 4  # 局部变量
    print(b * 10)

    global a  # 如果要在函数内改变全局变量的值，增加global关键字声明
    a = 3000
    print(a)

    print(locals())  # 打印输出的局部变量
    print(globals())  # 打印输出的全局变量


test01()
print(a)
