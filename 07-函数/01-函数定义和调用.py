# Files: 
# Author：jiang liu
# Date ：2020/3/12 13:36
# Tool ：PyCharm


def test01():
    print("*" * 10)
    print("@" * 10)


print(id(test01))
print(type(test01))
test01()


def printMax(a, b):
    """
    输出两个数字中较大的值
    :param a:
    :param b:
    :return:
    """

    if a > b:
        print('较大值是：', a)
    else:
        print('较大值是：', b)


printMax(10, 20)

# 查看函数文档说明
help(printMax.__doc__)
