import numpy as np
import matplotlib.pyplot as plt

def divided_diff(x, y):
    n = len(y)
    coef = np.zeros([n, n])
    coef[:,0] = y
    
    for j in range(1,n):
        for i in range(n-j):
            coef[i][j] = (coef[i+1][j-1] - coef[i][j-1]) / (x[i+j]-x[i])
            
    return coef

def newton_poly(coef, x_data, x):
    n = len(x_data) - 1 
    p = coef[n]
    for k in range(1,n+1):
        p = coef[n-k] + (x -x_data[n-k])*p
    return p

x = np.array([5, 10, 15, 20, 25, 30, 35, 40])
y = np.array([40, 30, 25, 40, 18, 20, 22, 15])

coef = divided_diff(x, y)

x_new = np.linspace(5, 40, 100)
y_new = newton_poly(coef[0, :], x, x_new)

plt.scatter(x, y, color='red', label='Data asli')
plt.plot(x_new, y_new, color='blue', label='Interpolasi Newton')
plt.xlabel('Tegangan')
plt.ylabel('Waktu Patah')
plt.title('Interpolasi Newton untuk Tegangan vs Waktu Patah')
plt.legend()
plt.show()
