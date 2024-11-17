# AdvancedLinePlot.py
import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Plotting
plt.plot(x, y1, label='Sine', linestyle='--')
plt.plot(x, y2, label='Cosine', linestyle='-')
plt.title('Advance Line Plot')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.legend()
plt.show()

