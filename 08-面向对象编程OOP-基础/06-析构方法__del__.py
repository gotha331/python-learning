# Files: 
# Author：jiang liu
# Date ：2020/3/25 13:27
# Tool ：PyCharm


class Person:

    def __del__(self):
        print('销毁对象{0}'.format(self))


p1 = Person()
p2 = Person()

# del p2
print('程序结束')
print(p1)
# print(p2)
