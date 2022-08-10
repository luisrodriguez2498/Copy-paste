import pandas as pd
import matplotlib.pyplot as plt

#plt.xkcd()

df = pd.DataFrame({'frecuencia': [3457, 3030, 2258, 2212, 1845, 599, 476, 404, 378, 281, 202, 147]})
df.index = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
df = df.sort_values(by='frecuencia',ascending=False)
frecuencia_relativa = df["frecuencia"].cumsum()
total_defectos = df["frecuencia"].sum()
df["cumpercentage"] = frecuencia_relativa/total_defectos*100


fig, ax = plt.subplots()
ax.bar(df.index, df["frecuencia"], color="C0")
ax2 = ax.twinx()
ax2.plot(df.index, df["cumpercentage"], color="C1", marker="o", ms=5)



plt.show()