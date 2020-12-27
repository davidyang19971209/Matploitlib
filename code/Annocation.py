import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
t = np.arange(0., 5., 0.01)
s = np.cos(2 * np.pi * t)
ax.plot(t, s, lw=2)  # lw表示线条宽度

ax.annotate('local max', xy=(2, 1), 
             xytext=(3, 1.5))

ax.set_ylim(-2, 2)
plt.show()