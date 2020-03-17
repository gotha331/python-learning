# Files: 
# Author：jiang liu
# Date ：2020/3/13 16:36
# Tool ：PyCharm

#  嵌套函数： 在函数内部定义的函数


def outer():
    print('outer running...')

    def inner():
        print('inner running...')

    inner()


outer()


# def printChineseName(name, familyName):
#     print("{0}-{1}".format(familyName, name))
#
#
# def printEnglishName(name, familyName):
#     print("{0}-{1}".format(name, familyName))


def printName(isChinese, name, familyName):
    def inner_print(a, b):
        print("{0}-{1}".format(a, b))

    if isChinese:
        inner_print(familyName, name)
    else:
        inner_print(name, familyName)


printName(1, 'shuaishuai', 'liu')
printName(0, 'shuaishuai', 'liu')
