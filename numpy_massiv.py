import numpy as np



def massiv_yarat(n,m):
    " Massiv yaratuvchi funskiya"
    massiv=[]
   
    for i in range(n):
        satr=[]
        for j in range(m):
           qiymat=int(input(f"massiv {[i]}{[j]} chi sonini kiriting :"))
           satr.append(qiymat)
        massiv.append(satr)
    massiv=np.array(massiv)
    return massiv
n=int(input(" Satrni kiriting : "))
m=int(input(" ustunlar sonini kiriting : "))
print(massiv_yarat(n,m))