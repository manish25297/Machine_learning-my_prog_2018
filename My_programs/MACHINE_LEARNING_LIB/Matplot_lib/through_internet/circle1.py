import matplotlib.pyplot as plt
import numpy as np
import math

def circle(r):
  x=np.linspace(0,r,200)                      # taking 100 values between -r to r here between (-3,3)
  y=[]                                        # making a list 

  for m in range(200):
    y.append(math.sqrt((r*r)-(x[m]*x[m])))    # calculating the value of y
    
  y=np.array(y)                               # making a array from list so that we can easily perfom operations on it.

  plt.plot(x,y,color="red")                   # plotting Ist quadrant
  plt.plot(-x,y,color="red")                  # plotting IInd quadrant 
  plt.plot(-x,-y,color="red")                 # plotting IIIrd quadrant
  plt.plot(x,-y,color="red")                  # plotting IVth quadrant 

  plt.grid( color="green")                    # making a grid 
  


circle (1)
circle(2)
circle(3)
circle(4)
circle (50)
plt.show()                                  # showing the plot 
