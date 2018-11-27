# from https://www.geeksforgeeks.org/turtle-programming-python/
import turtle

colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
t = turtle.Turtle()
t.hideturtle()
t.speed()
turtle.bgcolor('black')
for x in range(360):
    t.pencolor(colors[x % 6])
    t.width(x / 100 + 1)
    t.forward(x)
    t.left(59)

turtle.exitonclick()