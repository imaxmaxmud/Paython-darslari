import numpy as np

def massiv_yaratuvchi(n):
  " Massive yaratuvchi funskiya "
  massiv=[]
  for i in range(n):
      massiv.append(i)

  return np.array(massiv)
print(massiv_yaratuvchi(10))