import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 10, 0.1)
x1 = np.arange(0, 5, 0.1)

y = x
y1 = 2 * x1

plt.title("Proportional Function")
plt.plot(x, y)
plt.plot(x1, y1)
plt.show()