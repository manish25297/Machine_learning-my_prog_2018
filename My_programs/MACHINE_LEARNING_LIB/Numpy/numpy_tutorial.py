import numpy as np

a=np.array([(1,2,3),(4,5,6)])
print a

"""
-------------------------------------------------------------------------
--------------------------------------------------------------------------
why we are using numpy array
     it occupies less space
     it is faster than a list
     it is more convinient to work with numpy as compared to list
---------------------------------------------------------------------------
"""
import time
import sys
s=range(1000)
print (sys.getsizeof(s[0])*len(s))  #shows the memory occupied by a list 
D=np.arange(1000)
print(D.size*D.itemsize)             #shows the memory occupied by numpy array



import time
import sys
SIZE=1000000
l1=range(SIZE)     # making a list of size 1000
l2=range(SIZE)

a1=np.arange(SIZE)   #making a np array of size 1000
a2=np.arange(SIZE)

start=time.time()     # storing the time before doing operation on list 
result=[(x,y) for x,y in zip(l1,l2)]
print((time.time()-start)*1000)     # printing the time taken by list operation

start=time.time()      #storing the time before doing operation on np.array
result=a1+a2
print((time.time()-start)*1000)    #printing the time taken by the np opearation
"""
------------------------------------------------------------------------------
opeartions of numpy array
--------------------------------------------------------------------------------
"""
import numpy as np
a=np.array([(1,2,3),(2,3,4)])
print("dimensions ",a.ndim)   #print the dimensions of the array
a=np.array([1,2,3])
print("dimensions ",a.ndim)              #print the dimensions of the array
print("itemsize",a.itemsize)             # printing the byte size of  each element of a
print (a.dtype)                          #printing the data type of a
print a.size                             # prints the size of the array
a=np.array([(1,2,3,5),(2,3,4,7)])
print a.shape                            #printing  the shape of the array
print a
b=a.reshape(4,2)
print b
