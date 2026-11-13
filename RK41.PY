import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Differential equation: dy/dx = y
def f(t, y):
    return y

# RK4 implementation
def rk4(f, t, y, h):
    k1 = f(t, y)
    k2 = f(t + h/2, y + h*k1/2)
    k3 = f(t + h/2, y + h*k2/2)
    k4 = f(t + h, y + h*k3)
    return y + (h/6) * (k1 + 2*k2 + 2*k3 + k4)

# Initial conditions
t = 0
y = 1
h = 0.1

times = [t]
values = [y]

# Calculating 30 steps
for i in range(30):
    y = rk4(f, t, y, h)
    t += h
    times.append(t)
    values.append(y)

# Plotting results
plt.plot(times, values, 'o-', label='RK4')
plt.plot(times, np.exp(times), '--', label='Exact solution')
plt.xlabel('Time')
plt.ylabel('y')
plt.title('RUNGE-KUTTA 4TH ORDER SIMULATION')
plt.legend()
plt.grid()
plt.savefig('RK41_result.png')
plt.close()