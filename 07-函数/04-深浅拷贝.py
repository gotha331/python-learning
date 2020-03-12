# Files: 
# Author：jiang liu
# Date ：2020/3/12 15:22
# Tool ：PyCharm


import copy


def testCopy():
    """ 测试浅拷贝 """
    a = [10, 20, [5, 6]]
    b = copy.copy(a)

    print("a:", a)  # b: [10, 20, [5, 6]]
    print("b:", b)  # b: [10, 20, [5, 6]]

    b.append(30)
    b[2].append(7)
    print('浅拷贝')
    print("a:", a)  # a: [10, 20, [5, 6, 7]]
    print("b:", b)  # b: [10, 20, [5, 6, 7], 30]


def testDeepCopy():
    """ 测试深拷贝 """
    a = [10, 20, [5, 6]]
    b = copy.deepcopy(a)

    print("a:", a)  # b: [10, 20, [5, 6]]
    print("b:", b)  # b: [10, 20, [5, 6]]

    b.append(30)
    b[2].append(7)
    print('深拷贝')
    print("a:", a)  # a: [10, 20, [5, 6]]
    print("b:", b)  # b: [10, 20, [5, 6, 7], 30]


testCopy()
print()
print('*' * 30)
print()
testDeepCopy()



