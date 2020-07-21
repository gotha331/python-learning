# 输入一个学生成绩，将其转化成简单描述：不及格(<60)、及格(60-79)、良好(80-89)、优秀(90-100)

# 方法1(使用完整的条件表达式)
score = int(input('请输入分数:'))
grade = ''

if score < 60:
    grade = '不及格'
elif 60 < score < 79:
    grade = '及格'
elif 80 < score < 89:
    grade = '良好'
elif 90 < score < 100:
    grade = '优秀'
else:
    print('请输入正确的分数')

print("分数是{0},等级是{1}".format(score, grade))
