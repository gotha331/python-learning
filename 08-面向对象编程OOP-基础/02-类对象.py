# Files: 
# Author：jiang liu
# Date ：2020/3/25 10:45
# Tool ：PyCharm


class Student:

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def say_score(self):
        print("{0}的分数是{1}".format(self.name, self.score))


stu2 = Student

s2 = stu2('帅帅刘', 100)

s2.say_score()  # 帅帅刘的分数是100

