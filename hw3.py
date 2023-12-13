'''
Niharika Agrawal
CSC 161
Homework 3: Graphics Drawing a House
'''

from graphics import *

def main():
    win = GraphWin("House", 500, 500)
    textlocation= Point(250,480)

    #mark lower left
    m1=Text(textlocation, "Click on the lower left corner of the house frame.").draw(win)
    p1 = win.getMouse()
    p1.draw(win)
    m1.undraw()

    #mark upper right
    m2=Text(textlocation, "Click on the upper right corner of the house frame.").draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    m2.undraw()

    '''HOUSE'''

    #draw house
    house = Rectangle(p1,p2)
    house.draw(win)

    #mark door point
    m3=Text(textlocation, "Click on the center of the top of the door.").draw(win)
    d1 = win.getMouse()
    d1.draw(win)
    m3.undraw()

    '''DOOR'''

    #draw door
    doorWidth = 0.2*(p2.getX()-p1.getX())
    dc1 = Point((d1.getX() - 0.5*doorWidth),d1.getY())
    dc2 = Point((d1.getX() + 0.5*doorWidth),p1.getY())

    door = Rectangle (dc1, dc2)
    door.draw(win)

    #draw doorknob
    doorHeight = d1.getY()- p1.getY()
    center = Point((dc2.getX() - doorWidth/10),(d1.getY()- doorHeight/2))
    doorknob = Circle(center, doorWidth/15)
    doorknob.draw(win)

    '''WINDOW'''

    #mark window point
    m4 = Text(textlocation, "Click on the center of the window.").draw(win)
    w1 = win.getMouse()
    w1.draw(win)
    m4.undraw()

    #draw window
    winWidth = 0.75*doorWidth
    wc1 = Point((w1.getX() - 0.5*winWidth),(w1.getY() + 0.5*winWidth))
    wc2 = Point((w1.getX() + 0.5*winWidth),(w1.getY() - 0.5*winWidth))

    window = Rectangle (wc1, wc2)
    window.draw(win)

    #draw crosshatching of window
    vert = Line(Point(wc1.getX() + 0.5*winWidth, wc1.getY()), Point(wc2.getX() - 0.5*winWidth, wc2.getY()))
    vert.draw(win)

    horiz = Line(Point(wc1.getX(), wc1.getY() - 0.5*winWidth), Point(wc2.getX(), wc2.getY() + 0.5*winWidth))
    horiz.draw(win)

    '''ROOF'''

    #mark roof peak
    m5 = Text(textlocation, "Click on the peak of the roof.").draw(win)
    r1 = win.getMouse()
    r1.draw(win)
    m5.undraw()

    #draw roof
    rc1 = Point(p1.getX(), p2.getY())
    roof = Polygon(rc1, r1, p2)
    roof.draw(win)

    #quit program
    Text(textlocation, "Click anywhere to quit.").draw(win)
    win.getMouse()
    win.close()

main()

    
