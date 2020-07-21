# Files: 
# Author：jiang liu
# Date ：2020/3/26 19:21
# Tool ：PyCharm


# 无论是否发生异常，都会执行finally部分
# try:
#     a = input("请输入一个被除数：")
#     b = input("请输入一个除数：")
#     c = float(a) / float(b)
# except BaseException as e:
#     print(e)
# else:
#     print("除的结果是：", c)
# finally:
#     print("我是finally中的语句，无论发生异常与否，都执行！")
#
# print("程序结束！")

# 示例

try:
    f = open("d:/a.txt", "r")
    content = f.readline()
    print(content)
except BaseException as e:
    print(e)
    print("文件未找到")
finally:
    print("run in finally,关闭资源")
    # f.close()
