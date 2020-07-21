with open("aa.PNG", "rb") as f:
    with open("aa_copy.PNG", "wb") as w:
        for line in f.readlines():
            w.write(line)

print("图片拷贝完成。。。")
