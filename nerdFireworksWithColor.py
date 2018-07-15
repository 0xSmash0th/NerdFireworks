#!/usr/bin/python

from turtle import *
from Tkinter import *
from math import *


def setPenColor(depth):
    if (depth < 3):
        pencolor("white")
    elif (depth < 7):
        pencolor("cyan")
    else:
        pencolor("red")
        
def branch(length):
    global depth
    global angle
    global ratio
    
    depth += 1

    setPenColor(depth)
    
    forward(length)
    if length > 4:
        currPos = pos()
        currAngle = heading()
        right(angle)
        branch(length * ratio)
        setheading(currAngle)
        setpos(currPos)
        left(angle)
        branch(length * ratio)
        setpos(currPos)
        setheading(currAngle)
        
    setPenColor(depth)        
    depth -= 1



def tree(length):
    global draw
    if not draw.get():
        tracer(0,0)
    else:
        tracer(1, 10)

    bgcolor("black")
    pencolor("white")
    speed(0)
    penup()
    setpos(250,0)
    pendown()
    left(90)
    branch(length)
    update()
    done()
    
def showTree():
    global branchLen
    global angle
    global ratio
    branchLen = int(e1.get())
    ratio = float(e2.get())
    angle = int(e3.get())
    tree(branchLen)

def sierpinski(base, x, y):
    global depth
    global reqDepth

    # start postion at middle of base
    penup()
    setpos(x,y)
    pendown()

    # draw right half of base
    forward(base/2)
    left(120)

    # draw right side
    forward(base)
    left(120)

    # draw left side
    forward(base)
    left(120)

    # finsh base
    forward(base/2)
    
    depth += 1 
    # if we need to draw more, set up the coords and len
    if (depth < reqDepth):
        # coords for triagle A
        pAx = x - base/4
        pAy = y

        # coords for triagle B
        pBx = x + base/4
        pBy = y

        # coords for triagle C
        pCx = x
        pCy = (sqrt(3)/2 * base)/2 + y
        
        pencolor("white")
        sierpinski(base/2, pAx, pAy)
        pencolor("cyan")
        sierpinski(base/2, pBx, pBy)
        pencolor("red")
        sierpinski(base/2, pCx, pCy)
    depth -= 1


def showSierp():
    global draw
    global depth
    global reqDepth
    depth = 0
    reqDepth = int(e5.get())
    base = int(e4.get())
    if not draw.get():
        tracer(0,0)
    else:
        tracer(1, 10)
    bgcolor("black")
    pencolor("white")
    sierpinski(base, 250, 0)
    speed(0)
    update()
    done()
    

def clearTurtle():
    reset()

if __name__ == "__main__":
    master = Tk()
    draw = IntVar()
    setworldcoordinates(0, 0, 500, 500)
    
    depth = 0
    angle = 45
    ratio = .66
    branchLen = 100

    Label(master, text="Branch Start Length").grid(row=0)
    Label(master, text="Branch Length Ratio").grid(row=1)
    Label(master, text="Branch angle").grid(row=2)
    Label(master, text="Sierpinski Base len").grid(row=4)
    Label(master, text="Sierpinski depth").grid(row=5)

    e1 = Entry(master)
    e2 = Entry(master)
    e3 = Entry(master)
    e4 = Entry(master)
    e5 = Entry(master)

    e1.insert(10,100)
    e2.insert(10,.66)
    e3.insert(10,45)
    e4.insert(10,300)
    e5.insert(10,3)
    
    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    e3.grid(row=2, column=1)
    e4.grid(row=4, column=1)
    e5.grid(row=5, column=1)

    Button(master, text='Clear', command=clearTurtle).grid(row=3, column=2, sticky=W, pady=4)
    Button(master, text='Tree', command=showTree).grid(row=3, column=0, sticky=W, pady=4)
    Button(master, text='Sierp', command=showSierp).grid(row=6, column=0, sticky=W, pady=4)
    Checkbutton(master, text="Draw", variable=draw).grid(row=6, column=1, sticky=W) 
  

    mainloop( )    
