import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
from math import sqrt

style.use('ggplot')
plt.ion()

iteration = 20
jump = 2

for i in range(iteration):
    plt.clf()

    function1 = '(4 - x1**2)**(1/2)'
    function2 = '-(4 - x2**2)**(1/2)'

    x1 = np.arange(-2, (2+jump), jump)
    x2 = np.arange((2-jump), (-2-jump), -jump)

    y1 = eval(function1)
    y2 = eval(function2)

    x = np.append(x1, x2)
    y = np.append(y1, y2)

    circum = np.array([sqrt((x[i+1]-x[i])**2 + (y[i+1]-y[i])**2) for i in \
                       range(int(4/jump))])
    circum = np.nansum(circum)
    circum *= 2

    pi = circum/4

    jump /= 2

    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    
    plt.text(2, 2, ('pi='+str(pi)))
    plt.text(-2, 2, ('loop '+str(i+1)))
    plt.text(-2, -2, 'n='+str(2**(i+2)))
    
    plt.axis('equal')
    plt.plot(x, y)
    plt.show()
    plt.pause(0.5)
