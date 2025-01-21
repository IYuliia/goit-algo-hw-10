import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

def f(x):
    return x ** 2

a = 0  
b = 2  


def monte_carlo_integral(f, a, b, n_points=10000):
    x_random = np.random.uniform(a, b, n_points)  
    y_random = f(x_random)  
    integral = (b - a) * np.mean(y_random)  
    return integral

monte_carlo_result = monte_carlo_integral(f, a, b, n_points=10000)
quad_result, quad_error = spi.quad(f, a, b)


print(f"Результат методом Монте-Карло: {monte_carlo_result}")
print(f"Результат функції quad: {quad_result}, похибка: {quad_error}")


x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()
