import turtle
import turtle as p
import random

# 定义画圆函数
def drawCircle(x,y,c='red'):
    p.pu()        # 抬起画笔
    p.goto(x, y)  # 绘制圆的起始位置
    p.pd()        # 放下画笔
    p.color(c)
    p.circle(30, 360)

# 画笔基本设置
p = turtle
p.pensize(3)

# 绘制五环图，调用画圆函数
drawCircle(0, 0, "blue")
drawCircle(60, 0, "black")
drawCircle(120, 0, "red")
drawCircle(90, -30, "green")
drawCircle(30, -30, "yellow")

p.done()


