import matplotlib.pyplot as plt
import numpy as np
from load_data import load_data
from sort import bubble_sort

data = load_data('activity.csv')
power_W = data['PowerOriginal']
zeit = np.arange(len(power_W))
sorted_power_W = bubble_sort(power_W)

# Plot
plt.figure()
plt.plot(zeit, sorted_power_W, label="Leistungskurve", color="orange")
plt.xlabel("Zeit[s]")
plt.ylabel("Leistung[W]")
plt.title("Leistungskurve")
plt.grid()
plt.legend()
plt.tight_layout()
plt.savefig('figures\powercurve.png')
plt.show()
