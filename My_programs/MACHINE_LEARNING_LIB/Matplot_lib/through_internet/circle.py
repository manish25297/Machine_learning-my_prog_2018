import matplotlib.pyplot as plt
import numpy as np

x=[5]
y=[5]
x1=np.linspace(0,2,100)
print x1[0]
y1=[]
import math
"""
for m in range(100):
  y1.append(math.sqrt(4-(x1[m]*x1[m])))"""
for m in range(100):
  y1.append(math.sqrt(4-(x1[m]*x1[m])))
#x1.append(i)
print y1
y1=np.array(y1)
x2=[]
y2=[]



x2=[x1,-x1,-x1,x1]#1,2,3,4
y2=[y1,y1,-y1,-y1]
plt.plot(x1,y1,color="red")
plt.grid( color="green")
plt.show()
