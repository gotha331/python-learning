a = {'name': 'shuai', 'age': 18, 'job': 'CEO'}

print(a['name'])
print(a.get('name'))

# 推荐使用get方法，可设置指定键不存在时默认返回的对象
sex = a.get('sex', 'superman')
age = a.get('age', 'superman')

print(sex)  # 'superman'
print(age)  # 18

# 列出所有键值对
print(a.items())  # dict_items([('name', 'shuai'), ('age', 18), ('job', 'CEO')])

# 列出所有的键，列出所有的值
print(a.keys())  # dict_keys(['name', 'age', 'job'])
print(a.values())  # dict_values(['shuai', 18, 'CEO'])

# len() 键值对的个数
print(len(a))  # 3

# 检测一个'键'是否在字典中
print('name' in a)  # True
