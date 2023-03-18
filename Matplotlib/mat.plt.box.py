import numpy as np
from matplotlib import pyplot as plt

s = np.random.rand(100)
fig = plt.figure()
plt.plot(s)
plt.plot(kind="box")
plt.show()




