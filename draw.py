from tkinter import *

root = Tk()

root.geometry("500x500")

canvas = Canvas(root, width=500, height=500)
canvas.pack()

canvas.create_line(100,200,200,35, fill="green", width=5)


root.mainloop()


