# Files: 
# Author：jiang liu
# Date ：2020/3/11 17:15
# Tool ：PyCharm

import turtle

t = turtle.Pen()
t.width(4)
t.speed(1000)

my_colors = ('red', 'blue', 'green', 'pink', 'grey', 'black', 'yellow', '#965633')

for i in range(100):
    t.color(my_colors[i % len(my_colors)])
    t.penup()
    t.goto(0, -i * 20)
    t.pendown()
    t.circle(20 + i * 20)

turtle.done()  # 程序执行完，保留窗口显示
