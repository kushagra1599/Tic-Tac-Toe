import tkinter as tk
from PIL import Image,ImageTk
X =Image.open("X.png")
X = X.resize((133,133))
X = ImageTk.PhotoImage(X)
O =Image.open("O.png")
O = O.resize((133,133))
O = ImageTk.PhotoImage(O)
root = tk.Tk()

canvas = tk.Canvas(root,width = 400,height = 400)
canvas.create_line(0,133.33,400,133.33)
canvas.create_line(0,266.66,400,266.66)
canvas.create_line(133.33,0,133.33,400)
canvas.create_line(266.66,0,266.66,400)
canvas.create_image(66.66,66.66,image = X)
canvas.pack()
tk.mainloop()