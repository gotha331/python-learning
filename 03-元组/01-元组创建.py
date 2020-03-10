# 通过()创建元组。小括号可以省略
a = (10, 20, 30)
b = 10, 20, 30

print(a)
print(b)
print(type(a))
print(type(b))

c = tuple('abc')
print(c)  # ('a', 'b', 'c')

d = tuple(range(3))
print(d)  # (0, 1, 2)

e = tuple([2, 3, 4])
print(e)  # (2, 3, 4)
