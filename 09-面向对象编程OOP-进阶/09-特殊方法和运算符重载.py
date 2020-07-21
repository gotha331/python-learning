# Files: 
# Author：jiang liu
# Date ：2020/3/25 19:38
# Tool ：PyCharm


class Person:
    def __init__(self, name):
        self.name = name

    def __add__(self, other):
        if isinstance(other, Person):
            return "{0} --- {1}".format(self.name, other.name)
        else:
            return '不是同类对象，不能相加'


p1 = Person('帅帅')
p2 = Person('豆芽')

x1 = p1 + p2
x2 = p1.__add__(p2)
print(x1)
print(x2)
