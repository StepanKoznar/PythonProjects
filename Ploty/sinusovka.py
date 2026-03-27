import numpy as np
import matplotlib.pyplot as plt

x = []
y = []
for i in range (0, 5000):
    x.append(i*0.01)
    y.append(np.sin(i*0.01))

plt.plot(x,y)
plt.show()
