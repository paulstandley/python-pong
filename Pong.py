# pong
# setup
import turtle

wn = turtle.Screen()
wn.title('pong by @TokyoEdTech')
wn.bgcolor('black')
wn.setup(width=800, height=600)
wn.tracer(0)

# Main game loop
while True:
	wn.update()