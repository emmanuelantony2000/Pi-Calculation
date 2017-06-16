import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')
plt.ion()


def plotting(maxVal, jump, colour):
    #For Square
    x = np.array([maxVal, maxVal, -maxVal, -maxVal, maxVal])
    y = np.array([maxVal, -maxVal, -maxVal, maxVal, maxVal])

    plt.plot(x, y, color=colour)

    #For circle
    function1 = '(('+str(maxVal**2)+') - x1**2)**(1/2)'
    function2 = '-(('+str(maxVal**2)+') - x2**2)**(1/2)'

    x1 = np.arange(-2, (2+jump), jump)
    x2 = np.arange((2-jump), (-2-jump), -jump)

    y1 = eval(function1)
    y2 = eval(function2)

    x = np.append(x1, x2)
    y = np.append(y1, y2)

    plt.plot(x, y, color=colour)


colour = 'red'
colourPoint = 'yellow'
jump = 0.0001
loopRange = 150
precision = 10000
maxVal = 0.5
circlePoint = 0
squarePoint = 0

plotting(maxVal, jump, colour)

for i in range(loopRange):
    #plt.clf()

    #plotting(maxVal, jump, colour)

    xRandom = (random.randrange(-(maxVal*precision),
                                (maxVal*precision)+1))/precision
    yRandom = (random.randrange(-(maxVal*precision),
                                (maxVal*precision)+1))/precision

    if (xRandom**2 + yRandom**2) < maxVal**2:
        circlePoint += 1
        squarePoint += 1
    elif (xRandom**2 + yRandom**2) > maxVal**2:
        squarePoint +=1

    plt.xlabel('x-axis')
    plt.ylabel('y-axis')

    plt.text((maxVal*1.2), (maxVal*1.2), 'n='+str(i+1))

    plt.axis('equal')
    plt.scatter(xRandom, yRandom, color=colourPoint)
    plt.show()
    plt.pause(0.00001)


print((circlePoint/squarePoint)*4)



