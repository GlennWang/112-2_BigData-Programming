import numpy as np
import matplotlib.pyplot as plt

x_degrees = np.arange(0, 361, 1)
x_radians = np.deg2rad(x_degrees)

y_sin = np.sin(x_radians)
y_cos = np.cos(x_radians)
y_sin_3x = np.sin(3 * x_radians)

plt.figure(figsize=(10, 6))
plt.plot(x_degrees, y_sin, label='sin(x)')
plt.plot(x_degrees, y_cos, label='cos(x)')
plt.plot(x_degrees, y_sin_3x, label='sin(3x)')

plt.title('sin(x), cos(x), sin(3x)')
plt.legend()

plt.grid(True)
plt.show()
