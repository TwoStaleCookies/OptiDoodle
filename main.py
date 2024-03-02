# Library imports
import colorsys
import random
import draw

#VARIABLES
colors = ['F9C6C9', 'F2C6DE', 'DBCDF0', 'C6DEF1', 'C9E4DE', 'FAEDCB', 'F7D9C4', 'E2CFC4', 'D2D2CF']
squares = []
color = colorsys.BLACK
blink = False
xcoor = 0
ycoor = 0

#CLASSES AND FUNCTIONS
class Grid:

    def __init__(self):
        #width and height are in units of squares
        self.width = 100
        self.height = 60

    def drawGrid(self):
        #draw gridlines

grid = Grid()

class Square:
    def __init__(self, x, y):
        #width and height are in units of pixels
        self.length = draw.root.winfo_screenwidth()/100
        self.xcoor = x * self.length
        self.ycoor = y * self.length

    def colorSquare(self):
        #draw square based on 

for i in range(grid.height):
    for j in range(grid.width):
        squares.append(Square(i, j))

def color(xcoor, ycoor):
    #use coordinates to color chosen square

#MAIN CODE
while True:
    #collect coordinates of eye position
    #1 is temporary value
    xcoor = 1 / squares[0].length
    ycoor = 1 / squares[0].length
    
    #color square based on coordinate
    color(xcoor, ycoor)

    blink = #boolean if blink is registered
    if (blink)
        color = colors[random.randint(0,len(colors))]
        blink = False