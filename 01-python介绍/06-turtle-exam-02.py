import turtle
import math

# 定义多个点
x1, y1 = 100, 100
x2, y2 = 100, -100
x3, y3 = -100, -100
x4, y4 = -100, 100

t = turtle.Pen()

# 绘制折线
t.penup()
t.goto(x1, y1)
t.pendown()
t.goto(x2, y2)
t.goto(x3, y3)
t.goto(x4, y4)

# 计算起始点和终点的距离
distance = math.sqrt((x1 - x4) ** 2 + (y1 - y4) ** 2)
print(int(distance))
t.write(distance)
