import tkinter as tk

state = [[0 for i in range(3)] for j in range(3)]
window = tk.Tk()
canvas = tk.Canvas(window,width = 400,height = 400,bg = "white")
canvas.create_line(0,133.33,400,133.33)
canvas.create_line(0,266.66,400,266.66)
canvas.create_line(133.33,0,133.33,400)
canvas.create_line(266.66,0,266.66,400)
button = [[0 for i in range(3)] for j in range(3)]
c = 0
def check_state(state):
    if (state[0][0]==state[0][1] and state[0][1] == state[0][2] and state[0][2]=="x" or
        state[1][0]==state[1][1] and state[1][1] == state[1][2] and state[1][2]=="x" or
        state[2][0] == state[2][1] and state[2][1] == state[2][2] and state[2][2]=="x" or
        state[0][0] == state[1][0] and state[1][0] == state[2][0] and state[2][0]=="x" or
        state[0][1] == state[1][1] and state[1][1] == state[2][1] and state[2][1]=="x" or
        state[0][2] == state[1][2] and state[1][2] == state[2][2] and state[2][2] =="x" or
        state[0][0] == state[1][1] and state[1][1] == state[2][2] and state[2][2] == "x" or
        state[0][2] == state[1][1] and state[1][1] == state[2][0] and state[2][0] == "x" ):
        canvas.create_text(200,200,text = "Player1 has won")
        window.after(5000,window.destroy)
    elif (state[0][0]==state[0][1] and state[0][1] == state[0][2] and state[0][2]=="o" or
        state[1][0]==state[1][1] and state[1][1] == state[1][2] and state[1][2]=="o" or
        state[2][0] == state[2][1] and state[2][1] == state[2][2] and state[2][2]=="o" or
        state[0][0] == state[1][0] and state[1][0] == state[2][0] and state[2][0]=="o" or
        state[0][1] == state[1][1] and state[1][1] == state[2][1] and state[2][1]=="o" or
        state[0][2] == state[1][2] and state[1][2] == state[2][2] and state[2][2] =="o" or
        state[0][0] == state[1][1] and state[1][1] == state[2][2] and state[2][2] == "o" or
        state[0][2] == state[1][1] and state[1][1] == state[2][0] and state[2][0] == "o" ):
        canvas.create_text(200,200,text = "Player2 has won")
        window.after(5000,window.destroy)


for turn in range(1):
    def X_turn(x,y):
        canvas.create_rectangle(133.3*x,133.33*y,133.33*(x+1),133.33*(y+1),fill = "white")
        canvas.create_line(133.3*x+15,133.33*y+15,133.33*(x+1)-15,133.33*(y+1)-15)
        canvas.create_line(133.33*(x+1)-15,133.33*y+15,133.33*x+15,133.33*(y+1)-15)
        x = int(x)
        y = int(y)
        print (x,y)
        state[x][y] = "x"
        check_state(state)

    def O_turn(x,y):
        canvas.create_rectangle(133.3 * x, 133.33 * y, 133.33 * (x + 1), 133.33 * (y + 1), fill="white")
        canvas.create_oval(133.33*x+15,133.33*y+15,133.33*(x+1)-15,133.33*(y+1)-15)
        x = int(x)
        y = int(y)
        state[x][y] = "o"

        check_state(state)
    for i in range(3):
        for j in range(3):


            button[i][j] = canvas.create_oval(133.33*i+30,133.33*j+30,133.33*(i+1)-30, 133.33*(j+1)-30,fill = "orange")

    for i in range(3):
        for j in range(3):
            def clicked(event):
                global c
                x = event.x
                y = event.y
                x = x//133.33
                y = y//133.33
                c +=1
                if c%2 == 1:
                    X_turn(x,y)

                else:
                    O_turn(x,y)
            canvas.tag_bind(button[i][j], "<Button-1>", clicked)
canvas.pack()
window.mainloop()
