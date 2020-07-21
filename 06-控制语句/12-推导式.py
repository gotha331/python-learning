# Files: 
# Author：jiang liu
# Date ：2020/3/11 16:39
# Tool ：PyCharm

# 列表推导式
a = [x for x in range(1, 5)]
print(a)  # [1, 2, 3, 4]

b = [x * 2 for x in range(1, 5)]
print(b)  # [2, 4, 6, 8]

c = [x * 2 for x in range(1, 20) if x % 5 == 0]
print(c)  # [10, 20, 30]

d = [a for a in 'abcdefg']
print(d)  # ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# 字典推导式
# 统计文本中字符出现的次数：
my_text = 'i love china'
char_count = {c: my_text.count(c) for c in my_text}
print(char_count)  # {'i': 2, ' ': 2, 'l': 1, 'o': 1, 'v': 1, 'e': 1, 'c': 1, 'h': 1, 'n': 1, 'a': 1}

# 集合推导式
e = {x for x in range(1, 100) if x % 9 == 0}
print(e)  # {99, 36, 72, 9, 45, 81, 18, 54, 90, 27, 63}

# 生成器推导式（生成元组）
gnt = (x for x in range(4))
print(gnt)
# print(tuple(gnt))  # (0, 1, 2, 3)

for x in gnt:  # gnt是生成器对象，生成器是可迭代的对象，只能使用一次
    print(x)
