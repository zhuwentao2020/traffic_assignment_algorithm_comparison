import numpy as np
from scipy import optimize
from functools import partial


def classic(demand, capacity, free, n):
    def opt_function(x):
        return np.sum(np.multiply(free, x) + np.multiply(x, x) / capacity / 2)

    def constraints_function(x, i):
        return x[i]

    cons = [{'type': 'ineq', 'fun': partial(constraints_function, i=i)} for i in range(n)]
    cons.append({'type': 'eq', 'fun': lambda x: np.sum(x) - demand})

    x0 = demand / n * np.ones(n)
    x_opt = optimize.minimize(opt_function, x0, method='SLSQP', constraints=cons)

    return x_opt.x, free + x_opt.x / capacity
