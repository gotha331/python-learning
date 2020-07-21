# Files: 
# Author：jiang liu
# Date ：2020/3/25 18:50
# Tool ：PyCharm


# 多重继承

class A:

    def aa(self):
        print('aa')


class B:

    def bb(self):
        print("bb")


class C(B, A):

    def cc(self):
        print('cc')


c = C()
c.cc()
c.bb()
c.aa()
