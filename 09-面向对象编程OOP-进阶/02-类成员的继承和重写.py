# Files: 
# Author：jiang liu
# Date ：2020/3/25 16:58
# Tool ：PyCharm


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_age(self):
        print(self.name, "的年龄是：", self.age)

    def say_name(self):
        print("我的名字是{0}".format(self.name))


class Student(Person):

    def __init__(self, name, age, score):
        Person.__init__(self, name, age)
        self.score = score

    # 重写父类的方法
    def say_name(self):
        print("报告,重写后我的名字是{0}".format(self.name))


s = Student('刘帅帅', 25, 100)
s.say_age()
s.say_name()
