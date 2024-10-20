
import matplotlib.pyplot as plt
import numpy as np

x_values = [1,2,3,4,5,6,7,8,9]
y_values = [1,4,8,12,46,82,70,82,92]


#Simple line plot.

# plt.plot(x_values,y_values)
# plt.xlabel("X-placeholder")
# plt.ylabel("Y-placeholder")
# plt.show()
# plt.savefig('visualizations/linePlot.png')  # Save the figure as a PNG file
# plt.close()


#Scatter plot.

# plt.scatter(x_values,y_values)
# plt.xlabel("X-placeholder")
# plt.ylabel("Y-placeholder")
# plt.title("Title Placeholder")
# plt.show()
# plt.savefig('visualizations/scatterPlot.png') 
# plt.close()

# bar plot

# animal = ['cat','dog','parrot','gold fish']

# animal_values = [10,20,30,40]

# plt.bar(animal,animal_values,color="green")
# plt.xlabel("animal")
# plt.ylabel("population of animal in Locality")
# plt.title("Animal")
# plt.show()
# plt.savefig('visualizations/barPlot.png') 
# plt.close()


#Histogram of a normal distribution

# x_normal = np.random.normal(0,2,50)

# plt.hist(x_normal,color="green")
# plt.xlabel("x")
# plt.ylabel("Frequency")
# plt.title("Random Normal DIstribution.")
# plt.savefig('visualizations/histogram.png') 
# plt.close()


#Population distribution.
from scipy.stats import norm

x_normal = np.random.normal(0,2,50)

x_values = np.arange(-4,4,0.01)

y_values = norm.pdf(x_values)

counts,bins,ignored = plt.hist(x_normal,30,density=True,color="forestgreen",label="sampling distribution")

plt.plot(x_values,y_values,color="y",linewidth=2.5,label="population Distribution")

plt.title("Randomly generation 10000 obs from normal distribution mu=0 sigma=1")
plt.ylabel("Probability")
plt.legend()
plt.savefig('visualizations/population Distribution.png') 
plt.close()

