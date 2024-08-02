from turtle import *
import time
import random

speed(10) 
rt(-90) 
angle = 15

def y(sz, level):    
   if level > 0: 
        colormode(255)
        if level < 3:
             pensize(7-level)
             largo = 0.8 * (sz + random.randrange(-15,5))
        else:
            pensize(int(level/1.1)+2)
            largo = 0.8 * (sz + random.randrange(0,16))

        #pensize(int((12-level)/2))
        pencolor(100, 200//level, 0) 
        fd(sz) 
        angulo = angle + random.randrange(-int(level*1.5),int(level*1.2))
        rt(angulo) 
        
        y(largo, level-1) 
        pencolor(100, 200//level, 0) 
        lt( 2 * angulo ) 
        y(largo, level-1) 
        pencolor(100, 200//level, 0)  
        rt(angulo) 
        fd(-sz) 

setup(800, 480, 0, 0)
penup()
goto(0,-240)
pendown()
#time.sleep(8)          
y(50, 13) 
exitonclick()