import numpy 
import pylab 
import random 
  
#number of steps 
n = int(input("Input Number of Steps: "))
  
#creating two array for x and y coordinate, filled with 0
x = numpy.zeros(n) 
y = numpy.zeros(n) 


# filling the coordinates
for i in range(1, n): 
    val = random.uniform(0, 100) 
    print("Random Value: ",val)
    if val < 12.5 : 
        #north
        x[i] = x[i - 1]
        y[i] = y[i - 1] + 1
    elif val < 25 : 
        #north east
        x[i] = x[i - 1] + 1
        y[i] = y[i - 1] + 1
    elif val < 37.5: 
        #east
        x[i] = x[i - 1] + 1
        y[i] = y[i - 1] 
    elif val < 50:
        #south east
        x[i] = x[i - 1] + 1
        y[i] = y[i - 1] - 1
    elif val < 62.5: 
        #south
        x[i] = x[i - 1] 
        y[i] = y[i - 1] - 1
    elif val < 75:
        #south west 
        x[i] = x[i - 1] - 1
        y[i] = y[i - 1] - 1
    elif val < 87.5:
        #west
        x[i] = x[i - 1] - 1
        y[i] = y[i - 1] 
    else:
        #north west
        x[i] = x[i - 1] - 1
        y[i] = y[i - 1] + 1
      
# output:
print("Start")
for a in range (0,n):
    print("Coordinate:","(",x[a]," , ",y[a],")")
print("End")

# plotting: 
pylab.title("Random Walk ($n = " + str(n) + "$ steps)") 
pylab.plot(x, y) 
pylab.savefig("Rizki_Ramadhan__random_walk.png",bbox_inches="tight",dpi=300) 
pylab.show() 