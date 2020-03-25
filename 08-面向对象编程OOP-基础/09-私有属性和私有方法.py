# Files: 
# Author：jiang liu
# Date ：2020/3/25 14:15
# Tool ：PyCharm


class Employee:
    __company = "samaung"

    def __init__(self, name, age):
        self.name = name
        self.__age = age  # 私有属性

    def __work(self):  # 私有方法
        print('暴富')
        print(Employee.__company)


e = Employee('帅帅', 25)

print(e.name)
# print(e.age)
print(dir(e))

print(e._Employee__age)  # 调用私有属性
e._Employee__work()  # 调用私有方法
print(Employee._Employee__company)
