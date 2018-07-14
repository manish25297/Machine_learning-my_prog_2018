import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")
from sklearn.cluster import KMeans
import pandas as pd

a=pd.read_csv("urli.csv")   # importing the csv file
print a.head(7)             #printing the first seven data
x= a.iloc[:,1]              # accessing the first columns
y= a.iloc[:,2]              # accessing the second columns
#z=zip(x,y);
#print z
X=np.array(zip(x,y))        
kmeans = KMeans(n_clusters=4)
kmeans.fit(X)
centroids = kmeans.cluster_centers_
labels = kmeans.labels_
print(centroids)
print(labels)

colors = ['r', 'g', 'b', 'y', 'c', 'm']
plt.scatter(x,y,c="c",s=1)
plt.scatter(centroids[:,0],centroids[:,1],c=colors,marker='*',s=100)
plt.show()
