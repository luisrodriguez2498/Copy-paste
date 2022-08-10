import numpy as np
import matplotlib.pyplot as plt
data = [22, 87, 5, 43, 56, 73, 55, 54, 11, 20, 51, 5, 79, 31, 27]
classInterval = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
values, base = np.histogram(data, bins=classInterval)
cumsum = np.cumsum(values)
plt.plot(base[1:], cumsum, marker='o', linestyle='-')
  
plt.xlabel("Intevalos de clases")
plt.ylabel("Frecuencia acumulada")
plt.show()