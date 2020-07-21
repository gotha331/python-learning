# Files: 
# Author：jiang liu
# Date ：2020/3/25 13:18
# Tool ：PyCharm


# 定义与"类对象"无关的方法，成为"静态方法"

class Student:
    company = 'ichinae'

    @staticmethod
    def add(a, b):  # 静态方法
        print("{0} + {1} = {2}".format(a, b, (a + b)))
        return a + b


Student.add(20, 30)
