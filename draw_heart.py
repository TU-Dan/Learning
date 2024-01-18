import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2, 2, 1000)
y1 = np.sqrt(1-(abs(x)-1)**2)
y2 = -3*np.sqrt(1-(abs(x)/2)**0.5)

fig, ax = plt.subplots()
ax.fill_between(x, y1, color='red')
ax.fill_between(x, y2, color='red')

plt.show()