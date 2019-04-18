import numpy 
import pylab 
import random 
  
#number of steps 
n = 10000
  
#creating two array for x and y coordinate, filled with 0
x = numpy.zeros(n) 
y = numpy.zeros(n) 
  
# filling the coordinates
for i in range(1, n): 
    val = random.randint(1, 8) 
    if val == 1: 
        #north
        x[i] = x[i - 1]
        y[i] = y[i - 1] + 1
    elif val == 2: 
        #north east
        x[i] = x[i - 1] + 1
        y[i] = y[i - 1] + 1
    elif val == 3: 
        #east
        x[i] = x[i - 1] + 1
        y[i] = y[i - 1] 
    elif val == 4:
        #south east
        x[i] = x[i - 1] + 1
        y[i] = y[i - 1] - 1
    elif val == 5: 
        #south
        x[i] = x[i - 1] 
        y[i] = y[i - 1] - 1
    elif val == 6:
        #south west 
        x[i] = x[i - 1] - 1
        y[i] = y[i - 1] + 1
    elif val == 7:
        #west
        x[i] = x[i - 1] - 1
        y[i] = y[i - 1] 
    else:
        #north west
        x[i] = x[i - 1] - 1
        y[i] = y[i - 1] + 1
      
  
# plotting stuff: 
pylab.title("Random Walk ($n = " + str(n) + "$ steps)") 
pylab.plot(x, y) 
pylab.savefig("random_walk"+str(n)+".png",bbox_inches="tight",dpi=600) 
pylab.show() 