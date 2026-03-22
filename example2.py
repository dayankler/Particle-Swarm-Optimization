from pyswarm import pso

# Objective function
def func(x):
    return x[0]**2

lb = [-10]
ub = [10]

best, _ = pso(func, lb, ub)
print("Best:", best)
