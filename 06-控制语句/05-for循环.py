for x in (20, 30, 40):
    print(x * 10)

for x in 'abcdefghijklmn':
    print(x, end="\t")

print()

# 遍历字典

d = {'name': 'shuai', 'age': 18, 'address': 'shaanxixian'}

# 遍历字典所有的key
for x in d:
    print(x, end="\t")  # name	age	address

# 遍历字典所有的key
for x in d.keys():
    print(x)  # # name	age	address

# 遍历字典所有的value
for x in d.values():
    print(x)

# 遍历字典所有的键值对
for x in d.items():
    print(x, end=";")  # ('name', 'shuai');('age', 18);('address', 'shaanxixian');

print()
# range对象
# 计算 1-100之间数的累加和
# 计算 1-100之间奇数的累加和
# 计算 1-100之间偶数的累加和

sum_all = 0
sum_odd = 0
sum_even = 0

for x in range(101):
    sum_all += x

    if x % 2 == 0:
        sum_even += x
    else:
        sum_odd += x

print("1-100之间数的和是：{0},偶数和是：{1},奇数和是：{2}".format(sum_all, sum_even, sum_odd))
