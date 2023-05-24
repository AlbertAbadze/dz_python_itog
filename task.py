import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return -12*x**4*np.sin(np.cos(x)) - 18*x**3 + 5*x**2 + 10*x - 30

# Нахождение корней
roots = np.roots([-12, 0, -18, 5, 10, -30])
print("Корни функции f(x):", roots)

# Нахождение интервалов возрастания и убывания
x_values = np.linspace(-10, 10, 1000)
y_values = f(x_values)

increasing_intervals = []
decreasing_intervals = []

for i in range(len(x_values)-1):
    if y_values[i+1] > y_values[i]:
        increasing_intervals.append((x_values[i], x_values[i+1]))
    elif y_values[i+1] < y_values[i]:
        decreasing_intervals.append((x_values[i], x_values[i+1]))

print("Интервалы возрастания функции f(x):", increasing_intervals)
print("Интервалы убывания функции f(x):", decreasing_intervals)

# Построение графика
plt.plot(x_values, y_values)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('График функции f(x)')
plt.grid(True)
plt.show()

# Вычисление вершины
vertex_x = x_values[np.argmin(y_values)]
vertex_y = np.min(y_values)
vertex = (vertex_x, vertex_y)
print("Вершина функции f(x):", vertex)

# Определение промежутков, на которых f > 0 и f < 0
positive_intervals = []
negative_intervals = []

for i in range(len(x_values)-1):
    if y_values[i] > 0 and y_values[i+1] > 0:
        positive_intervals.append((x_values[i], x_values[i+1]))
    elif y_values[i] < 0 and y_values[i+1] < 0:
        negative_intervals.append((x_values[i], x_values[i+1]))

print("Промежутки, на которых f(x) > 0:", positive_intervals)
print("Промежутки, на которых f(x) < 0:", negative_intervals)
