import numpy as np
import matplotlib.pyplot as plt

y = [1,2,3,-5,7,6]
y2 = [2,3,8,7.7,5,8.3]
x = [1,3,5,7,9,11]
plt.plot(x,y, label="U [V]")
plt.plot(x,y2, label="I [mA]")
plt.xlabel("t [s]")
plt.ylabel("U [V]")
plt.title("Graf elektriky v čase")
plt.legend()
plt.show()