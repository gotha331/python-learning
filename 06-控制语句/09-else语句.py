# Files: 
# Author：jiang liu
# Date ：2020/3/11 15:56
# Tool ：PyCharm


# else语句
'''
while、for循环可以附带—个else语句（可选）.
如果for、 while语句没有被 break语句结束，则会执行else子句，否则不执行。

语法格式如下：

Whle条件表达式：
    循环体
else：
    语句块

或者

for变量in可迭代对象
    循环体
else
    语句块

'''

# 要求：员工一共4人。录入这4人的薪资。全部录入后，打印提示："您已全部录入4名员工的薪资"。最后，打印输出录入的薪资和平均薪资

salarySum = 0
salarys = []
for i in range(4):
    s = input('请输入员工的薪资（按Q或者q结束）：')

    if s.upper() == 'Q':
        print('录入完成，退出')
        break
    if float(s) < 0:
        continue

    salarys.append(float(s))
    salarySum += float(s)

else:
    print("您已全部录入4名员工的薪资")

print("录入薪资{0},平均薪资{1}".format(salarys, salarySum / 4))
