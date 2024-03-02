# Library imports
import random
from tkinter import *
from tkinter.ttk import *

#VARIABLES
colors = ['F9C6C9', 'F2C6DE', 'DBCDF0', 'C6DEF1', 'C9E4DE', 'FAEDCB', 'F7D9C4', 'E2CFC4', 'D2D2CF']
squares = []
color = 'red'
blink = False
xcoor = 0
ycoor = 0
root = Tk()
root.attributes('-fullscreen',True)
canvas = Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
canvas.pack()  
squareLen = root.winfo_screenwidth()/100.0

#CLASSES AND FUNCTIONS
class Grid:

    global root, canvas, squareLen
    def __init__(self):
        #width and height are in units of squares
        self.width = 100
        self.height = 64

        self.drawGrid(canvas = canvas)
        root.mainloop()

    def drawGrid(self, canvas):
        #draw gridlines
        for k in range(self.height):
            canvas.create_line(0, k * squareLen, root.winfo_screenwidth(), k * squareLen)
        for m in range(self.width):
            canvas.create_line(m * squareLen, 0, m * squareLen, root.winfo_screenwidth())

grid = Grid()

class Square:

    global root, canvas, color, squareLen
    def __init__(self, x, y):
        #width and height are in units of pixels
        self.xcoor = x * squareLen
        self.ycoor = y * squareLen

    def colorSquare(self):
        #draw square if looked at
        canvas.create_rectangle(self.xcoor, self.ycoor, self.xcoor + squareLen, self.ycoor + squareLen, fill=color)

for i in range(grid.height):
    for j in range(grid.width):
        squares.append(Square(i, j))

#MAIN CODE
def main(x, y):
    #collect coordinates of eye position
    #1 is temporary value
    xcoor = x * 100
    ycoor = y * 64
    xcoor = round(xcoor, 0)
    ycoor = round(ycoor, 0)

    #color square based on coordinate
    squares[ycoor][xcoor].colorSquare()

    blink = False #temporary value
    if (blink):
        color = colors[random.randint(0,len(colors))]
        blink = False
