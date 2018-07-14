import matplotlib.pyplot as plt
from matplotlib import style

style.use("ggplot")

x=[1,2,3]
y=[4,5,6]

x2=[7,8,9]
y2=[4,5,6]

plt.plot(x,y,color="cyan",label="population density")
plt.plot(x2,y2,color="red",label="city", linewidth=2)
plt.title("hellO matplot")  # for title naming of the graph
plt.xlabel("population")     #naming the x axis
plt.ylabel("year")            #naming the y axis
plt.legend()# for showing the labels of the plot
plt.grid(color='green')
plt.show()                  #for showing the graph 
