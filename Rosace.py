# Example for VSFX 705 - adapted from
# From http://home.foni.net/~heikos/data/tkinter.pdf
# added window sizing
# Rosette

import turtle
from turtle import *

def part( total, length, breadth, col ):
    angleInc = 360/total
    width( breadth )
    color( col )
    for i in range(total):
        forward( length )
        left( angleInc )

def rosette( total, length, width, color, angleInc ):
    for i in range( int(360/angleInc) ):
        part( total, length, width, color )
        left( angleInc )

# set up the turtle
turtle.setup( 500, 500, 100, 100 ) # specify width, height, position on screen
turtle.speed(0) # draw as fast as possible
turtle.bgcolor('black')

# call the functions
title("Rosette - original from website no longer active")
a = 36
rosette(10,40,1,"blue",a)
rosette(5,80,1,"yellow",a)
turtle.exitonclick()