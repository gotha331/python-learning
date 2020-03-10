a = {'name': 'shuaishuailiu', 'age': 18, 'job': 'CEO'}
print(a.get('name'))
print(a.get('age'))
print(a.get('job'))

# 字典的创建方法
# 1. {}、dict()

b = {'name': '我尼玛', 'job': 'CEO'}
c = dict(name='hello', job='world')
d = dict([('name', 'haha'), ('age', 18)])

print(b)
print(c)
print(d)  # {'name': 'haha', 'age': 18}

print(b.get('name'))
print(b.get('job'))
print(c.get('name'))
print(c.get('job'))

e = {}
f = dict()

print(e)  # 空的字典对象
print(f)  # 空的字典对象

# 2. zip()
k = ['name', 'age', 'job']
v = ['shuai', 18, 'CEO']
w = dict(zip(k, v))
print(w)  # {'name': 'shuai', 'age': 18, 'job': 'CEO'}

# 3. 通过fromkeys创建值为空的字典
p = dict.fromkeys(['name', 'age', 'job'])
print(p)  # {'name': None, 'age': None, 'job': None}
