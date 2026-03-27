import matplotlib.pyplot as plt

x = [5,7,4,8,4,2,4]
y = [7,5,7,1,-1,25,14]

plt.scatter(x,y)
plt.show()

x1 = [1,2,3]
y1 = [2,3,4]

x2 = [1,2,3]
y2 = [5,1,2]

x3 = [1,3,5]
y3 = [1,4,5]

plt.scatter(x1, y1, color="red",s=100, marker="o", label="data1")
plt.scatter(x2, y2, color="green", marker="s", label="data2")
plt.scatter(x3, y3, color="cyan", marker="d", label="data3")

plt.legend()
plt.xlabel("čas[s]")
plt.ylabel("hodnota")
plt.grid()
plt.show()