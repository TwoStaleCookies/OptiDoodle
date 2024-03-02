from tkinter import *

root = Tk()

#root.geometry("500x500")
root.attributes('-fullscreen',True)

canvas = Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
canvas.pack()

canvas.create_rectangle(0, 0, root.winfo_screenwidth(), root.winfo_screenheight(), fill='red')

root.mainloop()


