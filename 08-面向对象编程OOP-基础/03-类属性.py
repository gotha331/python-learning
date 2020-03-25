# Files: 
# Author：jiang liu
# Date ：2020/3/25 10:49
# Tool ：PyCharm


class Student:
    company = 'ichinae'  # 类属性
    count = 0  # 类属性

    def __init__(self, name, score):
        self.name = name  # 实例属性
        self.score = score
        Student.count = Student.count + 1

    def say_score(self):  # 实例方法
        print("my company is :", Student.company)
        print(self.name, '的分数是：', self.score)


s1 = Student("张三", 99)  # s1是实例对象，自动调用__init__()方法
s1.say_score()

s2 = Student("李四", 88)
s2.say_score()
print("一共创建{0}个Student对象".format(Student.count))
