a = {'name': 'shuai', 'age': 18, 'job': 'CEO'}

# 添加
# 1. 直接新增，键存在时，值会覆盖
a['dream'] = '升官发财，名利双收'
print(a)  # {'name': 'shuai', 'age': 18, 'job': 'CEO', 'dream': '升官发财，名利双收'}

# 2. update()将新字典中所有键值对全部添加到旧字典对象上。如果key有重复，则直接覆盖
b = {'name': 'shuaishuailiu', 'money': 1000000000}
a.update(b)
print(a)  # {'name': 'shuaishuailiu', 'age': 18, 'job': 'CEO', 'dream': '升官发财，名利双收', 'money': 1000000000}

# 删除 del();
# clear()删除所有键值对
# pop()删除指定键值对，并返回对应的"值对象"

del (a['name'])
print(a)  # {'age': 18, 'job': 'CEO', 'dream': '升官发财，名利双收', 'money': 1000000000}

c = {'name': 'shuaishuailiu', 'money': 1000000000}
d = c.pop('name')

print(c)  # {'money': 1000000000}
print(d)  # shuaishuailiu

# popitem() 随机删除和返回该键值对
