import numpy as np


def msa(demand, capacity, free, n):
    x0 = demand / n * np.ones(n)

    iterate = 100000

    x = x0
    for i in range(iterate):
        time = free + x / capacity
        a = np.argmin(time)
        delta_x = np.zeros(n)
        delta_x[a] = demand
        x = (i + 1) / (i + 2) * x + 1 / (i + 2) * delta_x

    return x, time
