import matplotlib.pyplot as plt
import numpy as np
from sort import bubble_sort
from load_data import load_data

data = load_data('activity.csv')
power_W = data['PowerOriginal']
sorted_power_W = bubble_sort(power_W)

N_Steps = len(power_W)
zeitachse = np.arange(N_Steps)

# Plot
plt.figure()
plt.plot(zeitachse, sorted_power_W, label="Leistungskurve", color="orange")
plt.xlabel("Zeit [s]")
plt.ylabel("Leistung [W]")
plt.title("Leistungskurve")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("Leistungskurve.png")
plt.show()