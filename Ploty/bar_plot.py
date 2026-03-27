import matplotlib.pyplot as plt

labels = ["prvaci", "druhaci", "tretaci", "ctvrtaci"]
values = [100,80,60,40]

y = [80,75,60,45]

plt.bar(labels,values, label="sloupce")
plt.plot(labels,y, linestyle=":", label="čára", color="red")
plt.legend()
plt.title("Počet studentů")
plt.show()