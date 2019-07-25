"""This is pong"""

# pong
# setup
import turtle

wn = turtle.Screen()
wn.title('pong by @TokyoEdTech')
wn.bgcolor('black')
wn.setup(width=800, height=600)
wn.tracer(0) 

#  Paddel a
paddel_a = turtle.Turtle()
paddel_a.speed(0)
paddel_a.shape('square')
paddel_a.color('white')
paddel_a.shapesize(stretch_wid = 5, stretch_len = 1)
paddel_a.penup()
paddel_a.goto(-350, 0)

# Paddel b
paddel_a = turtle.Turtle()
paddel_a.speed(0)
paddel_a.shape('square')
paddel_a.color('white')
paddel_a.shapesize(stretch_wid = 5, stretch_len = 1)
paddel_a.penup()
paddel_a.goto(350, 0)

# Ball

# Main game loop
while True:
	wn.update()