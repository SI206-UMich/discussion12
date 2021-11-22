import matplotlib.pyplot as plt
import numpy as np

x = ['Nuclear', 'Hydra', 'Gas', 'Oil', 'Coal', 'Biofuel']
energy = [5,6,15,22,24,8]

plt.bar(x, energy, color = 'green')

plt.xlabel("Energy Source")
plt.ylabel("Energy Output (GJ)")
plt.title("Energy output from various fuel sources")

plt.xticks(x)

plt.show()