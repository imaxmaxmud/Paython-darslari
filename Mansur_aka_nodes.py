import matplotlib.pyplot as plt
import numpy as np

# Tugun koordinatalari
nodes = {
    'A': (1, 5), 'B': (1, 3), 'C': (1, 1),
    'D': (3, 5), 'E': (3, 3), 'F': (3, 1),
    'G': (5, 5), 'H': (5, 3), 'I': (5, 1)
}

# Har bir tugun uchun radius
radius = 2.5

# Markaziy bazaviy stansiya koordinatasi
base_station = (0, 3)

fig, ax = plt.subplots()
ax.set_aspect('equal')

# Tugunlarni chizish
for name, (x, y) in nodes.items():
    circle = plt.Circle((x, y), radius, color='black', linestyle='dotted', fill=False)
    ax.add_artist(circle)
    ax.plot(x, y, 'ko')  # Tugun nuqtasi
    ax.text(x, y, f' {name}', fontsize=12, va='center', ha='center')

# Baza stansiyasini chizish (antenna)
antenna_x, antenna_y = base_station
ax.plot(antenna_x, antenna_y, marker=(3, 0, 0), markersize=20, color='black')
ax.text(antenna_x - 0.2, antenna_y + 0.6, '📡', fontsize=20)

# Baza stansiya radiusi
base_circle = plt.Circle(base_station, radius, color='blue', linestyle='dotted', fill=False)
ax.add_artist(base_circle)

# Aloqalarni chizish (agar radius ichida bo'lsa)
for name, (x, y) in nodes.items():
    dist = np.linalg.norm(np.array([x, y]) - np.array(base_station))
    if dist <= radius:
        ax.plot([antenna_x, x], [antenna_y, y], 'gray', linewidth=1)

# Graf konfiguratsiyasi
ax.set_xlim(-1, 7)
ax.set_ylim(-1, 7)
plt.axis('off')
plt.title('Figure 3.1: Neighbor Discovery.')
plt.show()