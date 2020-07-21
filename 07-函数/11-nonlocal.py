# Files: 
# Author：jiang liu
# Date ：2020/3/13 16:58
# Tool ：PyCharm


# nonlocal 用来声明外层的局部变量
# global   用来声明全局变量
def outer():
    b = 10

    def inner():
        nonlocal b  # 声明外部函数的局部变量
        print("inner b:", b)  # 10
        b = 20

        global a  # 声明全局变量
        a = 1000

    inner()
    print("outer b:", b)  # 20


outer()
print("a:", a)
