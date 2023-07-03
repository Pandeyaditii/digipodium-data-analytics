from turtle import *
speed('fastest')
bgcolor('black')
colors =['red', 'orange', 'yellow',
         'green', 'blue', 'purple', 'magenta']
i = 0
while True:
    pencolor(colors[i%6])
    fd(10+i)
    lt(190)
    i += 1
mainloop()