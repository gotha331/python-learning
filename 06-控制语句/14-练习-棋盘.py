# Files: turtle绘图练习 - 绘制10*10棋盘
# Author：jiang liu
# Date ：2020/3/12 9:49
# Tool ：PyCharm


import turtle

t = turtle.Pen()
t.hideturtle()  # 隐藏箭头
t.width(2)
t.speed(10)

for i in range(11):
    t.penup()
    t.goto(-200, 200 - i * 40)
    t.pendown()
    t.goto(200, 200 - i * 40)
    t.penup()
    t.goto(-200 + i * 40, 200)
    t.pendown()
    t.goto(-200 + i * 40, -200)

turtle.done()  # 程序执行完，保留窗口显示
