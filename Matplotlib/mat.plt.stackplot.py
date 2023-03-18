from matplotlib import pyplot as plt
from numpy import random as rnd
age = sorted([10,22,25,36,45,52,45,65,35,75])
player1 = [0,0,0,1,1,2,2,2,2,2]
player2 = [1,1,1,2,2,2,2,2,3,3]

plt.style.use("fivethirtyeight")
plt.stackplot(age,player1,player2, labels = ['player1','player2'])
plt.legend()
plt.tight_layout()
plt.show()