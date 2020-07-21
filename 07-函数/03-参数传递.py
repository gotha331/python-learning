# Files: 
# Author：jiang liu
# Date ：2020/3/12 14:40
# Tool ：PyCharm


# 传递可变对象
a = [10, 20]
print(id(a))
print(a)


def test01(m):
    print(id(m))
    m.append(300)
    print(id(m))


test01(a)
print(a)

# 传递不可变对象

b = 100
print(id(b))
print(b)


def test02(n):
    print(id(n))  # 传递进来的是b对象的地址
    n = n + 200  # 由于b是不可变对象，因此创建新的对象n
    print(id(n))  # n 变为新的对象
    print(n)


test02(b)
print(b)
print(id(b))

print()
print("*" * 30)
print()

# 传递不可变对象时，如果发生拷贝，用的是浅拷贝

c = 10
print("c:", id(c))


def test03(m):
    print("m:", id(m))
    m = 20
    print(m)
    print("m:", id(m))


test03(c)

print()

# 传递不可变对象时，不可变对象里面包含的子对象是可变的，则方法内修改了这个可变对象，源对象也发生了改变
d = (10, 20, [5, 6])
print("d:", id(d))


def test04(k):
    print("k:", id(k))
    k[2][0] = 888
    print(k)  # (10, 20, [888, 6])
    print("k:", id(k))


test04(d)
