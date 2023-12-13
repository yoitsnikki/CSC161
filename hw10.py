'''
Niharika Agrawal
CSC 161
HW 10
'''

from turtle import *

#define the turtle screen
def init(size):
    reset()
    setup(600,600)
    setworldcoordinates(-size, -size, 2*size, size)
    speed(0)
    pensize(2)
    up()
    color("#04B45F")

#draw a rectangle
def one_rectangle(size):
    for i in range(2):
        down()
        forward(size)
        left(90)
        forward(size/2)
        left(90)
        up()

#draw many rectangles using one_rectangle recursively
def rectangles(size, depth):
    if depth == 0:
        return False

    elif depth == 1:
        one_rectangle(size)

    else:
        c = depth/2 + 0.5
        n = size/2
        one_rectangle(size)

        forward(size)
        rectangles(size/2, depth-1)
        backward(size*(c))

        rectangles(size/2, depth-1)
        forward(size*(c))
            
#main function to call previous functions with user input          
def main():
    
    size = int(input("Give the length of the first rectangle: "))
    depth = int(input("Give depth of recursively created rectangles: "))

    init(size)
    rectangles(size, depth)
      
main()

