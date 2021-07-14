import matplotlib.pyplot as plt
import numpy as np


labels = ['Orange', 'Soy', 'Banana', 'Milk', 'Meat']
bra_means = [25, 50, 30, 25, 65]
usa_means = [30, 40, 15, 27, 40]

x = np.arange(len(labels))  
width = 0.40  

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, bra_means, width, label='BRA', color='green')
rects2 = ax.bar(x + width/2, usa_means, width, label='USA', color='red')

ax.set_ylabel('Exportation (in billion)')
ax.set_title('Exportation by Country')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

fig.tight_layout()

plt.show()