from turtle import *

def hexagone(size, color='red'):
    fillcolor(color)
    begin_fill()
    for i in range(6):
        fd(size)
        lt(72)
    end_fill()
hexagone(100) #calling


def square(size, color='brown'):
    fillcolor(color)
    begin_fill()
    for i in range(4):
        fd(size)
        rt(90) 
    end_fill()
square(100) 

square(100, 'brown') #calling
square(50,'black')
hexagone(100)   
hexagone(50)


mainloop()   