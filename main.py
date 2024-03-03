# Library imports
import random
import pygame 
import tobii_research as tr
import time
import numpy as np

found_eyetrackers = tr.find_all_eyetrackers()
my_eyetracker = found_eyetrackers[0]
print("Address : " + my_eyetracker.address)
print("Model: " + my_eyetracker.model)
print("Name: "+ my_eyetracker.device_name)
print("Serial number: " + my_eyetracker.serial_number)



#VARIABLES
colors = ['#F9C6C9', '#F2C6DE', '#DBCDF0', '#C6DEF1', '#C9E4DE', '#FAEDCB', '#F7D9C4', '#E2CFC4', '#D2D2CF']
squares = []
color = colors[0]
# blink = False
# root = Tk()
# root.attributes('-fullscreen',True)
# canvas = Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
# canvas.pack()  
pygame.init()
pygame.font.init()
DISPLAY = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("OptiDoodle")
squareLen = DISPLAY.get_width()/100.0

#CLASSES AND FUNCTIONS
class Grid:

    global pygame, DISPLAY, squareLen
    def __init__(self):
        #width and height are in units of squares
        self.width = 100
        self.height = 64

    #     self.drawGrid(canvas = DISPLAY)


    # def drawGrid(self, canvas):
    #     #draw gridlines
    #     for k in range(self.height):
    #         #canvas.create_line(0, k * squareLen, root.winfo_screenwidth(), k * squareLen)
    #         pygame.draw.line(DISPLAY, 'grey', start_pos = (0, k * squareLen), end_pos = (DISPLAY.get_width(), k * squareLen))
    #     for m in range(self.width):
    #         #canvas.create_line(m * squareLen, 0, m * squareLen, root.winfo_screenwidth())
    #         pygame.draw.line(DISPLAY, 'grey', start = (m * squareLen, 0), end = (m * squareLen, DISPLAY.get_width()))

grid = Grid()

class Square:

    global pygame, DISPLAY, color, squareLen
    def __init__(self, x, y):
        #width and height are in units of pixels
        self.xcoor = x * squareLen
        self.ycoor = y * squareLen

    def colorSquare(self):
        #draw square if looked at
        #canvas.create_rectangle(self.xcoor, self.ycoor, self.xcoor + squareLen, self.ycoor + squareLen, fill='red')
        pygame.draw.rect(DISPLAY, 'red', pygame.Rect(self.xcoor, self.ycoor, squareLen, squareLen))

for i in range(grid.height):
    for j in range(grid.width):
        squares.append(Square(i, j))

#MAIN CODE
def main(x, y):
    print(x, y)
    global root, canvas, color, squareLen
    #collect coordinates of eye position
    #1 is temporary value
    xcoor = x * 100 * squareLen
    ycoor = y * 64 * squareLen
    xcoor = round(xcoor, 0)
    ycoor = round(ycoor, 0)

    #color square based on coordinate
    #squares[ycoor][xcoor].colorSquare()
    #canvas.create_rectangle(xcoor, ycoor, xcoor + 30, ycoor + 30, fill='red')
    #canvas.create_rectangle(xcoor, ycoor, xcoor + squareLen, ycoor + squareLen, fill='red')
    pygame.draw.rect(DISPLAY, color, pygame.Rect(xcoor, ycoor, squareLen, squareLen))

    #blink = False #temporary value
    
    pygame.display.flip()

def blink():
    global color, colors
    color = colors[random.randint(0,len(colors))]


#track gaze data
def gaze_data_callback(gaze_data):
    global blink
     #print("Left eye: ({gaze_le}) \t Right eye: ({gaze_re})".format(
      #   gaze_le = gaze_data['left_gaze_point_on_display_area'],
      #   gaze_re = gaze_data['right_gaze_point_on_display_area']
    # ))
    #print(gaze_data['left_gaze_point_on_display_area'], gaze_data['right_gaze_point_on_display_area'])
    x1, y1 = gaze_data['left_gaze_point_on_display_area']
    x2, y2 = gaze_data['right_gaze_point_on_display_area']
    if np.isnan(x1 and x2):
        blink()
    main(x = (x1+x2)/2, y = (y1+y2)/2)


my_eyetracker.subscribe_to(tr.EYETRACKER_GAZE_DATA, gaze_data_callback, as_dictionary = True) #start tracking
time.sleep(10) #5 seconds of tracking
my_eyetracker.unsubscribe_from(tr.EYETRACKER_GAZE_DATA, gaze_data_callback) #stop tracking