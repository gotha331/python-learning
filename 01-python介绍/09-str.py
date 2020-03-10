# str()实现数字转型字符串

a = str(5.20)
print(a)  # '5.2'

b = str(3.14e2)
print(b)  # '314.0'

c = str(314)
print(c)  # 314

d = str(True)
print(d)  # 'True'

# 使用[]提取字符串中的字符

e = 'abcdefghijklmnopqrstuvwxyz'
print(e[1])  # b
print(e[-2])  # y

print(a)

# replace() 实现字符串替换

f = 'abcdefg'

ff = f.replace('c', '帅帅刘')
print(f)
print(ff)

# 字符串切片 slice

print(e[1:5])  # bcde (默认步长为1)
print(e[1:5:1])  # 步长为1  bcde
print(e[1:5:2])  # 步长为2  bd

print(e[:3])  # abc
print(e[3:])  # defghijklmnopqrstuvwxyz

print(e[-3:])  # xyz

print(e[-8:-3])  # stuvw
print(e[:-3])  # abcdefghijklmnopqrstuvw

print(e[::-1])  # zyxwvutsrqponmlkjihgfedcba
print(e[::-2])  # zxvtrpnljhfdb

# 步长为负值，逆序


'''
练习:
1.将 "to be or not to be"字符串倒序输出
2.将 "sxtsxtsxtsxtsxt" 字符串中所有的s输出

'''

# 1.
r = "to be or not to be"
print(r[::-1])  # eb ot ton ro eb ot

# 2

p = "sxtsxtsxtsxt"
print(p[::3])  # ssss

# split()分割
o = r.split()
print(o)  # ['to', 'be', 'or', 'not', 'to', 'be']

# join()

l = '*'.join(o)
print(l)
