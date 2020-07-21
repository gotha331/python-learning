# Files: 
# Author：jiang liu
# Date ：2020/3/24 19:21
# Tool ：PyCharm


print(type(str))


# str1 = "global str"
def outer():
    # str1 = "outer"

    def inner():
        # str1 = "inner"
        print(str1)

    inner()


outer()
