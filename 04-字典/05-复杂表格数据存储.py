r1 = {'name': 'liushuai1', 'age': 18, 'salary': 10000, 'city': 'xian'}
r2 = {'name': 'liushuai2', 'age': 19, 'salary': 20000, 'city': 'beijing'}
r3 = {'name': 'liushuai3', 'age': 20, 'salary': 30000, 'city': 'shanghai'}

tb = [r1, r2, r3]
print(tb)

# 获得第二行的人的薪资
print(tb[1].get('salary'))  # 20000

# 打印表格中的所有薪资
for i in range(len(tb)):
    print(tb[i].get('salary'))

# 打印表的所有数据
for i in range(len(tb)):
    print(tb[i].get('name'),
          tb[i].get('age'),
          tb[i].get('salary'),
          tb[i].get('city'))
