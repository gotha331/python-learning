import time

time01 = time.time()  # 起始时间

a = ""
for i in range(10000):
    a += "sxt"

time02 = time.time()  # 终止时间
print("运行时间:" + str(time02 - time01))
print(a)

time03 = time.time()
li = []

for i in range(10000):
    li.append('sxt')
a = "".join(li)
time04 = time.time()

print("运行时间:" + str(time04 - time03))

# 成员操作符 in/not in
k = "abcdef"
print("bcd" in k)  # True
print("oo" not in k)  # True
