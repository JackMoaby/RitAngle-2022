import turtle
import time

screen_size = 1000
global resolution
resolution = 0.0001

global wn
wn = turtle.Screen()
wn.setup(screen_size, screen_size)
wn.tracer(0)

turtle = turtle.Turtle()
turtle.penup()
turtle.goto(-100, -50)
turtle.right(90)
turtle.pendown()

global counter
counter = 0


def depoint(pointyness):
    unpoint = round(-1 * (180 * (pointyness - 1)))
    return unpoint


def move_up(depth):
    global counter
    while True:
        turtle.forward(depth)
        counter += depth
        if turtle.ycor() > 50:
            break


def move_down(depth):
    global counter
    while True:
        turtle.forward(depth)
        counter += depth
        if turtle.ycor() < -50:
            break


turtle.left(depoint(0))
move_up(resolution)
wn.update()
turtle.right(depoint(0.1))
move_down(resolution)
wn.update()
turtle.left(depoint(0.2))
move_up(resolution)
wn.update()
turtle.right(depoint(0.3))
move_down(resolution)
wn.update()
turtle.left(depoint(0.4))
move_up(resolution)
wn.update()
turtle.right(depoint(0.5))
move_down(resolution)
wn.update()
turtle.left(depoint(0.6))
move_up(resolution)
wn.update()
turtle.right(depoint(0.7))
move_down(resolution)
wn.update()

print(counter / 100)

time.sleep(10)
