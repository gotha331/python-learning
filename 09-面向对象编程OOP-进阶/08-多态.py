# Files: 
# Author：jiang liu
# Date ：2020/3/25 19:25
# Tool ：PyCharm


# 多态 是指同一方法调用，由于对象不同可能会产生不同的行为
# 注意：
# 1. 多态是方法的多态，属性没有多态
# 2. 多态的存在有2个必要条件：继承、方法重写


# class Animal:
#     def shout(self):
#         print('动物叫了一声')
#
#
# class Dog(Animal):
#     def shout(self):
#         print('小狗，汪汪汪')


class Man:
    def eat(self):
        print('饿了，要吃饭')


class Chinese(Man):
    def eat(self):
        print("中国人用筷子吃饭")


class English(Man):
    def eat(self):
        print('英国人用叉子吃饭')


class Indian(Man):
    def eat(self):
        print('印度人用右手吃饭')


def ManEat(m):
    if isinstance(m, Man):
        m.eat()  # 多态，一个方法调用，根据对象的不同，调用不同的方法
    else:
        print('不给吃饭')


c = Chinese()
e = English()
i = Indian()
ManEat(c)
ManEat(e)
ManEat(i)
