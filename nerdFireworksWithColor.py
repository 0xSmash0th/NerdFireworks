from turtle import *
from Tkinter import *
from tkFileDialog   import askopenfilename



depth = 0
angle = 45
ratio = .66
branchLen = 100

def setPenColor(depth):
    if (depth < 3):
        pencolor("white")
    elif (depth < 7):
        pencolor("blue")
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
    bgcolor("black")
    pencolor("white")
    speed(0)
    setpos(0, -100)
    left(90)
    branch(length)
    done()
    
def show():
    global branchLen
    global angle
    global ratio
    branchLen = int(e1.get())
    ratio = float(e2.get())
    angle = int(e3.get())
    tree(branchLen)

def clearTurtle():
    reset()

if __name__ == "__main__":
    global branchLen

    master = Tk()
    Label(master, text="Branch Start Length").grid(row=0)
    Label(master, text="Branch Length Ratio").grid(row=1)
    Label(master, text="Branch angle").grid(row=2)

    e1 = Entry(master)
    e2 = Entry(master)
    e3 = Entry(master)

    e1.insert(10,100)
    e2.insert(10,.66)
    e3.insert(10,45)
    
    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    e3.grid(row=2, column=1)

    Button(master, text='Clear', command=clearTurtle).grid(row=3, column=1, sticky=W, pady=4)
    Button(master, text='Show', command=show).grid(row=3, column=0, sticky=W, pady=4)
    
  

    mainloop( )
    
