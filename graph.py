import pandas as pd
import matplotlib.pyplot as plt
from scipy.io import savemat

# Ma'lumotlar
data = {
    "Ko‘rsatkich": ["P_OB", "P_ST-TK", "P_ST-TesK", "P_ST"],
    "Yanvar": [0.92, 0.96, 0.95, 0.84],
    "Fevral": [0.94, 0.97, 0.96, 0.87],
    "Mart": [0.95, 0.98, 0.97, 0.90],
    "Aprel": [0.96, 0.99, 0.98, 0.93],
    "May": [0.97, 0.98, 0.97, 0.92],
    "Iyun": [0.96, 0.97, 0.96, 0.89],
    "Iyul": [0.95, 0.96, 0.95, 0.86],
    "Avgust": [0.94, 0.95, 0.94, 0.84],
    "Sentyabr": [0.93, 0.94, 0.93, 0.82],
    "Oktyabr": [0.93, 0.93, 0.92, 0.78],
    "Noyabr": [0.92, 0.92, 0.91, 0.76],
    "Dekabr": [0.90, 0.91, 0.90, 0.74]
}

# DataFrame yaratish
df = pd.DataFrame(data)

# ------------ GRAFIK CHIZISH ------------
# Yorqin ranglar
colors = ['deepskyblue', 'limegreen', 'darkorange', 'magenta']

# Grafik o'lchami
plt.figure(figsize=(12, 6))

# Har bir ko‘rsatkichni chizish
for i in range(len(df)):
    plt.plot(df.columns[1:], df.iloc[i, 1:], label=df.iloc[i, 0], 
             marker='o', linewidth=2, color=colors[i])

# Grafikka sarlavha va yorliqlar
plt.title("Oylik Ko‘rsatkichlar (Line Graph)")
plt.xlabel("Oy")
plt.ylabel("Qiymat")
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)

# Grafikni ko‘rsatish
plt.tight_layout()
plt.show()

# ------------ MATLAB FAYLGA SAQLASH ------------
matlab_data = {
    'months': df.columns[1:].tolist(),
    'P_OB': df.iloc[0, 1:].tolist(),
    'P_ST_TK': df.iloc[1, 1:].tolist(),
    'P_ST_TesK': df.iloc[2, 1:].tolist(),
    'P_ST': df.iloc[3, 1:].tolist()
}

savemat("oylik_korsatkichlar.mat", matlab_data)