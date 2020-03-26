# Files: 
# Author：jiang liu
# Date ：2020/3/25 19:03
# Tool ：PyCharm


# super() 代表父类的定义，而不是父类的对象

class A:

    def say(self):
        print('A:', self)


class B(A):

    def say(self):
        # A.say(self)
        super().say()
        print('B:', self)


B().say()
