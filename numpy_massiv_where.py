import numpy as np
import random 

massiv=np.random.rand(5,5)

result=np.where(massiv<0, -2, 2)
print(result)