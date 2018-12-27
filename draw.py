import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('out.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=' ')
    for row in plots:
        x.append(float(row[0]))
        y.append(float(row[1]))

plt.grid(True)
plt.plot(x,y)
plt.xlabel('dimension')
plt.ylabel('time, s')
plt.title('Strassen algorithm')
plt.legend()
plt.show()