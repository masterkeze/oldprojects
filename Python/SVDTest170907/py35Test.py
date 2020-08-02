import numpy as np
import matplotlib.pylab as plt

grid = np.array([[1,2,3,4],[5,6,7,8],[10,11,12,13],[14,15,16,17]])
fig,ax = plt.subplots()
ax.imshow(grid)
plt.show()
