from matplotlib import pyplot as plt
import numpy as np
x_values = [i for i in range(0, 11)]
y_values = [i for i in np.random.randint(10000,500000,size = len(x_values))]
plt.style.use('fivethirtyeight')

plt.bar(x_values,y_values, width=0.5, align='center')
y_values = [i for i in np.random.randint(10000,500000,size = len(x_values))]
plt.bar(x_values,y_values, width=0.5, align='edge')
plt.xticks(ticks=x_values, labels=[i for i in range(1,len(y_values)+1)])
plt.tight_layout()
plt.show()


# plt.xticks() for specifying the x ticks
# width = 0.5 for specifying the width of a bar
# align = 'edge' for moving bar at right side by default it is 'center'
# labels = [] for specifying the name/label for each bar and in plt.xticks() to specify the ticks of x-axis
# ticks = x_values the current values/ticks of x-axis


