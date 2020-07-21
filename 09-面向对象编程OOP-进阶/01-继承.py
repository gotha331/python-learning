# Files: 
# Author：jiang liu
# Date ：2020/3/25 16:23
# Tool ：PyCharm


class Person:

    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def say_age(self):
        print('我也不知道年龄')


class Student(Person):

    def __init__(self, name, age, score):
        Person.__init__(self, name, age)
        self.score = score


# 继承关系：Student ->Person ->object类
print(Student.mro())

s = Student('刘帅帅', 25, 100)
print(s.name)
print(s._Person__age)
print(dir(s))
print(s.score)
s.say_age()
