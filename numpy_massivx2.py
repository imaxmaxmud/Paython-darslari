import matplotlib.pyplot as plt

# Ma'lumotlar
holatlar = ['LPM (Uyqu)', 'CPU (Ish rejimi)', 'Radio Listen', 'Radio Transmit']
quvvat_sarfi = [0.01, 1.8, 18, 21]

# Gistogramma
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(holatlar, quvvat_sarfi, color=['gold', 'lightcoral', 'lightgreen', 'skyblue'])

# Qiymatlarni ustun ustiga yozish
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval + 0.5, f'{yval:.2f} mW',
            ha='center', va='bottom', fontsize=10)

# O‘qlar nomi va grid
ax.set_ylabel("Quvvat sarfi (mW)")
ax.set_title("Har bir tugundagi o‘rtacha quvvat sarfi (mW)", fontsize=14, weight='bold')
ax.grid(axis='y', linestyle=':', linewidth=0.7)

# Asosiy o‘qlarni yashirish
for spine in ['top', 'right', 'left', 'bottom']:
    ax.spines[spine].set_visible(False)

# Chegaralar
ax.set_xlim(-0.5, 4.2)
ax.set_ylim(0, 24)

# Strelkali o‘qlar — x ni 0 emas, chap chekkaga yaqin joydan boshlab
x_start = -0.48  # chapga surilgan
ax.annotate("", xy=(4.2, 0), xytext=(x_start, 0),
            arrowprops=dict(arrowstyle="->", lw=1.5, color='black'))
ax.annotate("", xy=(x_start, 24), xytext=(x_start, 0),
            arrowprops=dict(arrowstyle="->", lw=1.5, color='black'))

plt.tight_layout()
plt.show()