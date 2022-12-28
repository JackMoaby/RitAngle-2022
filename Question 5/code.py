import math
import time

start = time.perf_counter()

def attempt(angle):
    sidelength = math.sqrt((2/3.14159265359)-((2/3.14159265359)*math.cos(math.radians(angle))))
    print(sidelength)

    octogonSides = ((sidelength/2)/math.sin(math.radians(22.5)))
    octogonArea = 8* (0.5*octogonSides*octogonSides*math.sin(math.radians(45)))
    return octogonArea
                           
areas = []
areadifference= []

x = 1
change = 0.0001

for i in range(500000):
    current=attempt(x)
    up = attempt(x+change)          
    down = attempt(x-change)

    if (math.sqrt((1-down)*(1-down))) < (math.sqrt((1-current)*(1-current))):
        x=x-change
    elif (math.sqrt((1-up)*(1-up))) < (math.sqrt((1-current)*(1-current))):
        x=x+change
    else:
        change=change/2
        
print("x=",x)
print("Time taken:  ", (time.perf_counter() - start))
