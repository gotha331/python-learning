a = {1, 3, 5, 7, 9}
print(a)

a.add(1111)
print(a)

# 使用set(),将列表、元组等可迭代对象转成集合。如果原来数据存在重复数据，则只保留一个。

a = ['a', 'b', 'c', 'b']

b = set(a)
print(b)  # {'c', 'b', 'a'}

# remove()删除指定元素; clear()清空整个集合
a = {10, 20, 30, 40, 50}
a.remove(20)
print(a)

a.clear()
print(a)  # set()
