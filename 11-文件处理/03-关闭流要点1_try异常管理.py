# 使用异常机制管理文件对象的关闭操作
try:
    f = open(r"bb.txt", "a", encoding="utf-8")
    s = ["帅帅\n", "好想爱这个世界呀\n", "此时此刻\n"]
    f.writelines(s)
except BaseException as e:
    print(e)
finally:
    f.close()
