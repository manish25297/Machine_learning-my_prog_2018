
import pandas as pd

name=["manish","aman","rakesh","ashok","dakshit"]
roll=[25,26,27,28,29]
percentage=[70,71,72,73,74]

joined=zip(name,roll,percentage)
#print joined
"""for i,j,k in zip(name,roll,percentage):
  print i,j,k"""

activity= pd.DataFrame(joined,index=range(5,10),columns=['name','roll','percentage'])
print activity


"""for i,j,k,l in [(0,1,2,3),(4,5,6,7)]:
	print i+j


   for i,j in [[0,4],[4,6]]:
	i+j
"""
