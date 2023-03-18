from matplotlib import pyplot as plt
# from sklearn import preprocessing
import numpy as np
# import pandas as pd

plt.style.use('fivethirtyeight')

x_values = np.arange(10)
y_values = np.random.random(10)
plt.plot(x_values, y_values, label = 'lines1' ,linewidth=2, color = 'g', linestyle = '--', marker = '^')

y_values = np.random.random(10)
plt.plot(x_values, y_values, label = 'lines2')

# plt.grid()
# plt.fill_between(x_values, y_values)
plt.title('plot between x and y')
# plt.suptitle(' used for superior title')
plt.xlabel('x values')  #labeling the x axis
plt.ylabel('y values')  #labeling the y axis
plt.legend()
plt.tight_layout()
plt.show()


# label = '' for specifying a name for a line
# linewidth = 2 for the setting the width of the line to 2 it can ranges from 0 to infinity
# color = '' for specifying the color of the line
# linestyle = '' for specifying the style of the line
# marker = '' for specifying the marker or point on the line
# go-- is short for above three in which g is color, o for round dot of marker and -- for dotted line of linestyle but above three are suitable or readable
# plt.suptitle() the title superior to title
# plt.title() for naming the figure or plot
# plt.xlabel() and plt.ylabel() for naming the X-axis and Y-axis respectively
# plt.style.available to shows the available style to use for plot styling
# plt.style.use() for using the style for the plot
# plt.legend() for specifying the names for each line we can also specify them in plt.plot() using label
# plt.grid for the grid lines on the plot
# plt.tight_layout() for adding the padding and margin to the plot
# plt.show() for showing the plot/graph without it plot is not showns
