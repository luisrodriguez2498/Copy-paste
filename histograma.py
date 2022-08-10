import matplotlib.pyplot as plt

edades = [480, 2750, 3400, 2500, 2225, 1750, 2300, 600]

intervalos = ["Hasta 499", "500 a 999", "1000 a 1499", "1500 a 1999", 
"2000 a 2499", "2500 a 2999", "3000 a 4999", "5000 o más"] #indicamos los extremos de los intervalos

plt.bar(range(len(edades)), edades, align='center')
plt.xticks(range(len(intervalos)), intervalos, size='small', rotation='vertical')
plt.show()