import turtle
import random
turtle.speed(100)
turtle.setup(1000,1000)
turtle.title('So Many Squares')
turtle.hideturtle()
def draw_square(x,y,size,tilt_angle,c):
    turtle.up()
    turtle.goto(x,y)
    turtle.down()
    turtle.seth(tilt_angle)
    turtle.fillcolor(c)
    turtle.begin_fill()
    for i in range(4):
         turtle.fd(size)
         turtle.left(90)
    turtle.end_fill()
angle=0
size=300
while size > 0:
    draw_square(0,0,size,angle,(random.uniform(0,1),random.uniform(0,1),random.uniform(0,1)))
    size -= 0.1
    angle+=3
