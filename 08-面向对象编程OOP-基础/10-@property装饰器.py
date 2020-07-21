# Files: 
# Author：jiang liu
# Date ：2020/3/25 15:21
# Tool ：PyCharm


# @property 可以将一个方法的调用方式变成“属性调用”


# class Employee:
#
#     @property
#     def salary(self):
#         print("salary run ...")
#         return 10000
#
#
# emp1 = Employee()
# print(emp1.salary)


"""
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary


    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if 1000 < salary < 50000:
            self.__salary = salary
        else:
            print('录入错误！薪水在1000到50000之间')
            

emp1 = Employee('刘帅帅', 50000)
# print(emp1._Employee__salary)
print(emp1.get_salary())
emp1.set_salary(20000)
print(emp1.get_salary())
emp1.set_salary(100)
print(emp1.get_salary())

"""


class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        if 1000 < salary < 50000:
            self.__salary = salary
        else:
            print('录入错误！薪水在1000-50000之间')


emp2 = Employee('宝帅', 30000)
print(emp2.salary)

emp2.salary = 666
print(emp2.salary)


emp2.salary = 9999
print(emp2.salary)