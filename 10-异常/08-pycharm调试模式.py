# Files: 
# Author：jiang liu
# Date ：2020/3/26 20:17
# Tool ：PyCharm


def aa():
    print("run in aa() start!")
    print("step1")
    num1 = 3
    num2 = num1 * 4
    num3 = num2 * 5
    print("step2")
    print("run in aa() end!!!")


if __name__ == "__main__":
    print("main:step1")
    aa()
    print("main:step2")
    print("main:end!!!")
