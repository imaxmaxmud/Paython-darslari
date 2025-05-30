import matplotlib.pyplot as plt

# Ma'lumotlar
intervals = ['1 daqiqa', '5 daqiqa', '10 daqiqa', '30 daqiqa', '1 soat', '2 soat', '6 soat']
advantage_scores = [5, 4, 4, 3, 3, 2, 1]  # Afzallik darajasi
limitation_scores = [5, 4, 3, 3, 2, 2, 1]  # Cheklov darajasi

# Chizish
plt.figure(figsize=(10, 6))
plt.plot(intervals, advantage_scores, marker='o', color='orange', label='Afzallik darajasi')
plt.plot(intervals, limitation_scores, marker='s', color='orangered', linestyle='--', label='Cheklov darajasi')

# Yozuvlar
plt.xlabel("Monitoring oralig‘lari")
plt.ylabel("Ball (1 - past, 5 - yuqori)")
plt.title(" ")

# Tarmoq chiziqlari
plt.grid(True, linestyle='--', alpha=0.5)

# Afsona (legend)
plt.legend()

# Tik holatda x o‘qi yozuvlari
plt.xticks(rotation=45) 
# ax1.spines['top'].set_visible(False)
# ax1.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()
