# Files: 
# Author：jiang liu
# Date ：2020/3/25 18:56
# Tool ：PyCharm


# 多重继承

class A:

    def aa(self):
        print('aa')

    def say(self):
        print('say AAA')


class B:

    def bb(self):
        print("bb")

    def say(self):
        print('say BBB')


class C(B, A):

    def cc(self):
        print('cc')


c = C()
c.cc()
c.bb()
c.aa()

c.say()  # say BBB  取决于C多重继承时的顺序，谁在前，继承谁的
