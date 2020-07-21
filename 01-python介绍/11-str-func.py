a = "我叫刘帅帅,我拥有漂亮的老婆和可爱的龙凤胎儿女,老婆很爱很爱我,女儿儿子乖巧懂事,父母身体健康,我们生活的很幸福.现在我也住进了自己的别墅,父母也生活的体面光鲜,村里人再也没有瞧不起我们,对我们都非常非常尊敬.我体会到了幸福的感觉,幸福的无以言表"

# len 字符串长度
print(len(a))

# startswith 以指定字符传开头
# endswith 以指定字符传结束

print(a.startswith('我叫刘帅帅'))
print(a.endswith('幸福的无以言表'))

# find 第一次出现指定字符串的位置
# rfind 最后一次出现指定字符串的位置
# count 指定字符串出现了多少次
# isalnum 所有字符全是字母或者数字

print(a.find('幸福'))
print(a.rfind('幸福'))
print(a.count('幸福'))
print(a.isalnum())

# 去除首位信息

# strip() 去除字符串首尾指定信息
# lstrip() 去除字符串左侧指定信息
# rstrip() 去除字符串右侧指定信息

a = '*s*x*t*'

print(a.strip('*'))  # s*x*t
print(a.lstrip('*'))  # s*x*t*
print(a.rstrip('*'))  # *s*x*t

# # 大小写转换

# capitalize()  产生新的字符串，首字母大写
# title() 产生新的字符串，每个单词都首字母大写
# upper() 产生新的字符串，所有字符全转成大写
# lower() 产生新的字符串，所有字符全转成小写
# swapcase() 产生新的字符串，所有字母大小写转换


b = "Liushuaishuai love programming,love freedom"
print(b.capitalize())  # Liushuaishuai love programming,love freedom
print(b.title())  # Liushuaishuai Love Programming,Love Freedom
print(b.upper())  # LIUSHUAISHUAI LOVE PROGRAMMING,LOVE FREEDOM
print(b.lower())  # liushuaishuai love programming,love freedom
print(b.swapcase())  # lIUSHUAISHUAI LOVE PROGRAMMING,LOVE FREEDOM

# 格式排版  center()、ljust()、rjust()
c = "SXT"
print(c.center(10, '*'))  # ***SXT****
print(c.center(10))  # '   SXT    '
print(c.ljust(10, '*'))  # SXT*******
print(c.rjust(10, '*'))  # *******SXT



# 其他方法
'''
1. isalnum() 是否为字母或数字
2. isalpha() 检测字符串是否只由字母组成(含汉字)。
3. isdigit() 检测字符串是否只由数字组成。
4. isspace() 检测是否为空白符
5. isupper() 是否为大写字母
6. islower() 是否为小写字母

'''

