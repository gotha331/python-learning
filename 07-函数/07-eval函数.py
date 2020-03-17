# Files: 
# Author：jiang liu
# Date ：2020/3/13 14:05
# Tool ：PyCharm


s = "print('abcd')"
eval(s)

a = 10
b = 20
c = eval("a + b")
print(c)  # 30

dict1 = dict(a=100, b=200)

d = eval("a+b", dict1)
print(d)  # 300
