# coding=utf-8
# Files:
# Author：jiang liu
# Date ：2020/3/26 19:42
# Tool ：PyCharm


# with不是用来取代try...except...finally结构的，只是作为补充，方便我们在文件管理，网络通信时的开发

# 示例：with上下文管理文件操作
with open("d:/bb.txt") as f:
    for line in f:
        print(line)
