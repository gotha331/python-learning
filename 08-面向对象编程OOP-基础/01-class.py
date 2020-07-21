# Files: 
# Author：jiang liu
# Date ：2020/3/24 19:45
# Tool ：PyCharm


class GoodStudent:  # 类名一般首字母大写，多个单词采用驼峰命名
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def say_score(self):
        print("{0}的分数是{1}".format(self.name, self.score))


s1 = GoodStudent("shuaishuai", 25)  # 通过类名()调用构造函数
s1.say_score()

GoodStudent.say_score(s1)

# 其他操作

'''
1. dir(obj)可以获得对象的所有属性、方法
2. obj.__dict__ 对象的属性字典
3. pass 空语句
4. isinstance(对象,类型)  判断"对象"是不是"指定类型"
'''


class Man:
    pass


print(dir(s1))
print(s1.__dict__)
print(isinstance(s1, Man))  # False
