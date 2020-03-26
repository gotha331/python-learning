# Files: 单例模式
# Author：jiang liu
# Date ：2020/3/26 9:45
# Tool ：PyCharm


class MySingleton:
    __obj = None  # 类属性
    __init_flag = True  # 私有化标记

    def __new__(cls, *args, **kwargs):
        if cls.__obj is None:
            cls.__obj = object.__new__(cls)

        return cls.__obj

    def __init__(self, name):
        if self.__init_flag:
            print("init.....")
            self.name = name
            self.__init_flag = False


a = MySingleton('aa')
b = MySingleton('bb')
c = MySingleton('cc')
print(a)
print(b)
print(c)
