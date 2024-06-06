import numpy as np
import matplotlib.pyplot as plt

def lagrange_interpolation(x, y, x_new):
    n = len(x)
    p = 0
    for i in range(n):
        L = 1
        for j in range(n):
            if i != j:
                L *= (x_new - x[j]) / (x[i] - x[j])
        p += y[i] * L
    return p

x = np.array([5, 10, 15, 20, 25, 30, 35, 40])
y = np.array([40, 30, 25, 40, 18, 20, 22, 15])

x_new = np.linspace(5, 40, 100)
y_new = lagrange_interpolation(x, y, x_new)

plt.scatter(x, y, color='red', label='Data asli')
plt.plot(x_new, y_new, color='blue', label='Interpolasi Lagrange')
plt.xlabel('Tegangan')
plt.ylabel('Waktu Patah')
plt.title('Interpolasi Lagrange untuk Tegangan vs Waktu Patah')
plt.legend()
plt.show()
