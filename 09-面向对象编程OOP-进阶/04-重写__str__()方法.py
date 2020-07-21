# Files: 
# Author：jiang liu
# Date ：2020/3/25 17:54
# Tool ：PyCharm


# object有一个__str__()方法，用于返回一个对于"对象的描述"

class Person:  # 默认继承object类

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "名字是：{0}".format(self.name)


p = Person("刘帅帅")
print(p)
