# Files: 
# Author：jiang liu
# Date ：2020/3/11 16:26
# Tool ：PyCharm

for i in [1, 2, 3]:
    print(i)

names = ('刘老大', "刘老二", "刘老三", "刘老四")
ages = (50, 49, 48, 47)
jobs = ('CEO', 'worker', 'farmer', 'teacher')

for name, age, job in zip(names, ages, jobs):
    print("{0}--{1}--{2}".format(name, age, job))
