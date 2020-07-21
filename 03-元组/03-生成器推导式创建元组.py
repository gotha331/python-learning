# 生成器的使用测试

s = (x * 2 for x in range(5))
print(s)

print(tuple(s))  # (0, 2, 4, 6, 8)

s = (x * 2 for x in range(5))
# print(list(s))  # [0, 2, 4, 6, 8]

print(s)
print(s.__next__())  # 0
print(s.__next__())  # 2
print(s.__next__())  # 4
print(s.__next__())  # 6
print(s.__next__())  # 8
