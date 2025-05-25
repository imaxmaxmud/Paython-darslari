import numpy as np
from uuid import uuid4
import random
n=10
massiv=[]
n=int(input(" n ni kiriting :"))
m=int(input('m ni kiriting : '))
for i in range(n):
    satr=[]
    for j in range(m):
         satr=[random.randint(0,100) for _ in range(n)]
    print(satr)
    massiv.append(satr)    
# arr1=np.array(massiv)
# print(arr1)