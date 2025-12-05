
import turtle
import random

def fractal(t, size, levels):
    if levels ==0:
        return
    t.forward(size)
    angle = random.randint(15,45)
    t.left(angle)
    fractal (t, size * 0.7, levels - 1)
    t.right(2*angle)
    fractal (t, size * 0.7, levels - 1)
    t.left(angle)
    t.backward(size)

screen = turtle.Screen()
screen.bgcolor('black')
t = turtle.Turtle()
t.color('white')

t.speed(0)
t.left(90)
t.up()
t.backward(100)
t.down()
fractal(t, 100, 5)
screen.exitonclick()

    
    