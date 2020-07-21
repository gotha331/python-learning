# Files: 
# Author：jiang liu
# Date ：2020/3/26 19:52
# Tool ：PyCharm


import traceback

try:
    print("step1")
    num = 1 / 0
except:
    traceback.print_exc()

#  将异常信息输出到指定文件

try:
    print("step1")
    num = 1 / 0
except:
    with open("d:/bb.txt", "a") as f:
        traceback.print_exc(file=f)
