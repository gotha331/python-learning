# 测试文件读取

with open(r"e.txt", "r", encoding="utf-8") as f:
    # str1 = f.read()
    str2 = f.read(3)
    # print(str1)
    print(str2)

with open("e.txt", "r", encoding="utf-8") as f:
    for a in f:
        print(a, end="")
