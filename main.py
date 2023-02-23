import matplotlib.pyplot as plt
import random

step = int(input('Enter number of steps: '))

coords = [[0,0]] 
x = []
y = []
coord = [0,0]
while len(x)<= step:
    while True:
        copyCoord = coord.copy()
        dir = random.randint(0,3)
        if dir == 0:
            copyCoord[0] -= 1
        elif dir == 1:
            copyCoord[1] += 1
        elif dir == 2:
            copyCoord[0] += 1
        else:
            copyCoord[1] -= 1
        if copyCoord not in coords:
            break
    coords.append(copyCoord)
    coord = copyCoord
    x.append(coord[0])
    y.append(coord[1])
plt.plot(x,y)
plt.show()