import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,2.2,0.2)
y = np.arange(0,2.2,0.2)


X, Y = np.meshgrid(x, y)
u = 1
v = 2*Y*X


fig, ax = plt.subplots(figsize=(7,7))
ax.quiver(X,Y,u,v)
fig.savefig("edo_quiver.pdf", bbox_inches='tight')

plt.show()