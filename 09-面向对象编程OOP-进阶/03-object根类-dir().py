# Files: 
# Author：jiang liu
# Date ：2020/3/25 17:44
# Tool ：PyCharm


# 通过类的方法mro()或者类的属性__mro__可以输出这个类的继承层次结构

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_age(self):
        print(self.name, "的年龄是：", self.age)


obj1 = object()
print(dir(obj1))

s2 = Person('刘帅帅', 25)
print(dir(s2))
