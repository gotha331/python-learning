'''
# 打印如下效果

0 0 0 0 0
1 1 1 1 1
2 2 2 2 2
3 3 3 3 3
4 4 4 4 4

'''

for x in range(5):
    for y in range(5):
        print(x, end="\t")
    print()

# 利用嵌套循环打印九九乘法表

for m in range(1, 10):
    for n in range(1, m + 1):
        print("{0}*{1}={2}".format(m, n, (m * n)), end='\t')
    print()

# 使用列表和字典存储表格的数据
r1 = dict(name="1shuai", age=18, salary=30000, city="北京")
r2 = dict(name="2shuai", age=19, salary=20000, city="上海")
r3 = dict(name="3shuai", age=20, salary=10000, city="深圳")

tb = [r1, r2, r3]

for x in tb:
    if x.get('salary') >= 15000:
        print(x)
