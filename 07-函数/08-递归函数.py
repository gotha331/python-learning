# Files: 
# Author：jiang liu
# Date ：2020/3/13 14:20
# Tool ：PyCharm


def test01(n):
    print('test01:', n)
    if n == 0:
        print('over')
    else:
        test01(n - 1)

    print("test01*****", n)


test01(4)
"""
test01: 4
test01: 3
test01: 2
test01: 1
test01: 0
over
test01***** 0
test01***** 1
test01***** 2
test01***** 3
test01***** 4
"""
