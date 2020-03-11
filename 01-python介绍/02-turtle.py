import turtle  # 导入 turtle模块

t = turtle.Pen()

t.showturtle()  # 显示箭头
t.write('shuaishuailiu')  # 写字符转
t.forward(300)  # 前进300像素
t.color('red')  # 画笔颜色改为red
t.left(90)  # 箭头左转90度
t.forward(300)
t.goto(0, 50)  # 去坐标（0，50）
t.goto(0, 0)
t.goto(0, 50)
# t.penup()   # 抬笔。这样，路径就不会画出来
t.goto(50, 50)
t.pendown()  # 下笔
t.circle(100)  # 画圆  值为 半径
