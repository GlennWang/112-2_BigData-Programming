import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0, 2 * np.pi, 360)
x = np.cos(theta)
y = np.sin(theta)

plt.figure(figsize=(6, 6))
plt.plot(x, y)

plt.xticks(np.arange(-1.0, 1.5, 0.5))
plt.yticks(np.arange(-1.0, 1.25, 0.25))

plt.axis('equal')
plt.title('Circle')
plt.grid(True)

plt.show()
