import pandas as pd
import numpy as np
from sklearn.cluster import KMeans

li = []
with open("url.csv") as f:
    for line in f:
       li.append(line.split())
with open("urli.csv","w") as f:
    for line in li:
        st = ",".join(line)
        f.write(st + "\n")



"""
f=open("url.csv","r")
for i in f:
  print ",".join(i.split())
  
"""
a="manish                       kumar            singh"
print a
print a.split()       #  returns a  list 
b= a.split()
print b
print a.strip()        # returns a  string
c=a.strip()
print c
d= ",".join(c)
print d
