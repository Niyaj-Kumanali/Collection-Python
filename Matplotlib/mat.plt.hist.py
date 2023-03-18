from matplotlib import pyplot as plt

ages = sorted([10,22,25,36,45,52,45,65,35,75])
bins = [i for i in range(0,100,10)]
plt.style.use('fivethirtyeight')

plt.hist(ages, edgecolor = 'black', bins=bins)
plt.xticks(ticks=bins, labels=bins)
plt.tight_layout()
plt.show()