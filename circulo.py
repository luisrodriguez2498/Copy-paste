from matplotlib import pyplot as plt 
import numpy as np 
  
  
cars = ["Cinco estrellas", "Cuatro estrellas",
"Tres estrellas", "Dos estrellas", "Una estrella"] 
  
data = [4216253, 31960442, 24079125, 6331715, 2565219] 
  
fig = plt.figure(figsize =(10, 7)) 
plt.pie(data, labels = cars) 
  
plt.show() 