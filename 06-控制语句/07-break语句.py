# Files:
# Author：jiang liu
# Date ：2020/3/11 15:30
# Tool ：PyCharm


# 使用break语句结束循环

while True:
    a = input("请输入一个字符（输入Q或者q结束）:")
    if a.upper() == 'Q':
        print("循环结束，退出")
        break
    else:
        print(a)
