# a = ["我love u!", "真爱和自由", "升官发财，名利双收"]
# b = enumerate(a)
#
# print(a)
# print(b)
# print(list(b))
#
# c = [temp + " #" + str(index) for index, temp in enumerate(a)]

# print(c)

with open("e.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    lines = [line.rstrip() + " #" + str(index) + '\n' for index, line in enumerate(lines)]   # 推导式生成列表

with open("e.txt", "w", encoding="utf-8") as f:
    f.writelines(lines)
