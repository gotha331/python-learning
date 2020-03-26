# Files: 
# Author：jiang liu
# Date ：2020/3/26 16:21
# Tool ：PyCharm


# 未发生异常时，执行else部分
try:
    a = input('请输入被除数：')
    b = input('请输入除数：')
    c = float(a) / float(b)
except BaseException as e:
    print(e)
else:
    print('除的结果是：', c)

print('程序结束')
