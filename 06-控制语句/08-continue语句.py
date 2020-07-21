# Files: 
# Author：jiang liu
# Date ：2020/3/11 15:44
# Tool ：PyCharm

# 要求：输入员工的薪资，若薪资小于0则重新输入。最后打印出录入员工的数量和薪资明细，以及平均薪资

empNum = 0
salarySum = 0
salarys = []
while True:
    s = input('请输入员工的薪资（按Q或者q结束）：')

    if s.upper() == 'Q':
        print('录入完成，退出')
        break
    if float(s) < 0:
        continue
    empNum += 1
    salarys.append(float(s))
    salarySum += float(s)

print("员工数{0},录入薪资{1},平均薪资{2}".format(empNum, salarys, salarySum / empNum))
