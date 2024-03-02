# Library imports
import colorsys
import random
import draw
from tkinter import *
from tkinter.ttk import *

#VARIABLES
colors = ['F9C6C9', 'F2C6DE', 'DBCDF0', 'C6DEF1', 'C9E4DE', 'FAEDCB', 'F7D9C4', 'E2CFC4', 'D2D2CF']
squares = []
color = colorsys.BLACK
blink = False
xcoor = 0
ycoor = 0
squareLen = draw.root.winfo_screenwidth()/100

#CLASSES AND FUNCTIONS
class Grid:

    def __init__(self):
        #width and height are in units of squares
        self.width = 100
        self.height = 60

    def drawGrid(self):
        #draw gridlines
        for k in range(self.height):
            Canvas.create_line(0, k * squareLen, draw.root.winfo_screenwidth(), k * squareLen)
        for m in range(self.width):
            Canvas.create_line(m * squareLen, 0, m & squareLen, draw.root.winfo_screenwidth())

grid = Grid()

class Square:
    def __init__(self, x, y):
        #width and height are in units of pixels
        self.xcoor = x * self.length
        self.ycoor = y * self.length

    def colorSquare(self, xcoor, ycoor):
        #draw square if looked at
        Canvas.create_rectangle(self.xcoor, self.ycoor, self.xcoor + squareLen, self.ycoor + squareLen, fill=color)

for i in range(grid.height):
    for j in range(grid.width):
        squares.append(Square(i, j))

#MAIN CODE
while True:
    #collect coordinates of eye position
    #1 is temporary value
    xcoor = 1 / squareLen
    ycoor = 1 / squareLen

    #color square based on coordinate
    for i in range(grid.height):
        for j in range(grid.width):
            sq = squares[i][j]
            if (xcoor == sq.xcoor and ycoor == sq.ycoor):
                sq.colorSquare(xcoor, ycoor)

    blink = False #temporary value
    if (blink):
        color = colors[random.randint(0,len(colors))]
        blink = False