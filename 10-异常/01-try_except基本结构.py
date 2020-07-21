# Files: 
# Author：jiang liu
# Date ：2020/3/26 11:21
# Tool ：PyCharm


print('step0')
try:
    print('step1')
    n = 3 / 0
    print('step2')

except BaseException as e:
    print('step3')
    print(e)
    print(type(e))

print('end!!!')


# 示例：循环输入数字，如果不是数字则处理异常，直到输入88，则循环结束


while 1:
    try:
        x = int(input("请输入一个数字："))
        print("输入的数字是：", x)

        if x == 88:
            print('end!!')
            break

    except BaseException as e:
        print(e)
        print('异常，输入的不是一个数字')

print("程序结束")
