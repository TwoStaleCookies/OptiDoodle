# Library imports
import random

#VARIABLES
colors = []
squares = []
xcoor = 0
ycoor = 0

#CLASSES AND FUNCTIONS
class Grid:

    def __init__(self):
        #width and height are in units of squares
        self.width = 20 #random numbers ngl
        self.height = 20

    def drawGrid(self):
        #draw gridlines

grid = Grid()

class Square:
    def __init__(self, x, y):
        #width and height are in units of pixels
        self.width = 10 #change as needed
        self.height = 10
        self.xcoor = x
        self.ycoor = y

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
    #color square based on coordinate
    #if blink, change to random color
