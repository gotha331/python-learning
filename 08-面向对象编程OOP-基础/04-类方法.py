# Files: 
# Author：jiang liu
# Date ：2020/3/25 13:13
# Tool ：PyCharm


class Student:
    company = 'ichinae'

    @classmethod
    # 类方法
    def printCompany(cls):
        print(cls.company)


Student.printCompany()
