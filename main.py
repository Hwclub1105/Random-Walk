import matplotlib.pyplot as plt
import random

coords = [[0,0]] 
x = []
y = []
coord = [0,0]
while len(x)<= 20:
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
            print(copyCoord,coords)
            break
    coords.append(copyCoord)
    coord = copyCoord
    x.append(coord[0])
    y.append(coord[1])
print(x)
print(y)
plt.plot(x,y)
plt.show()