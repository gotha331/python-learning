x, y, z = (20, 30, 10)
print(x, end='\t')
print(y, end="\t")
print(z, end="\t")
print()

(a, b, c) = (10, 11, 12)
print(a, end="\t")
print(b, end="\t")
print(c, end="\t")
print()

[d, e, f] = [66, 88, 99]
print(d, end="\t")
print(e, end="\t")
print(f, end="\t")
print()

s = {'name': 'shuai', 'age': 18, 'job': 'CEO'}
a, b, c = s  # 默认对键进行操作
print(a)  # 'name'
print(b)  # 'age'
print(c)  # 'job'

name, age, job = s.items()  # 对键值进行操作

print(name)  # ('name', 'shuai')
print(name[0])  # name
print(name[1])  # shuai
print(age)  # ('age', 18)
print(job)  # ('job', 'CEO')

name1, age1, job1 = s.values()  # 对值进行操作
print(name1)  # shuai
print(age1)  # 18
print(job1)  # CEO
