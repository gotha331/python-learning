# 测试写入中文
# f = open(r"b.txt", "w")

f = open(r"c.txt", "w", encoding="utf-8")
f.write("尚学堂\n百战程序员\n")

f.close()
