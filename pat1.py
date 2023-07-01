from turtle import *
speed('fastest')
color = ['yellow', 'orange',]
bgcolor('black')
for i in range(5):
    pencolor('red')
    pensize('2')
    fd(100)
    for i in range(4):
        pencolor('blue')
        pensize('2')
        fd(50)
        fillcolor(color[i%2])
        begin_fill()
        for i in range(3):
            pencolor('green')
            pensize('2')
            fd(25)
            lt(360/3)
        end_fill()
        lt(360/4)
    lt(360/5)
mainloop()