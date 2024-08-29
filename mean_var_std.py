import numpy as np

def calculate(list):
    if len(list)!=9:
        raise ValueError("List must contain nine numbers.")
    numbers = np.array(list).reshape(3,3)
    calculations = {
        "mean":[numbers.mean(axis=0).tolist(),numbers.mean(axis=1).tolist(),numbers.mean().tolist()],
        "variance":[numbers.var(axis=0).tolist(), numbers.var(axis=1).tolist(),numbers.var().tolist()],
        "standard deviation":[numbers.std(axis=0).tolist(),numbers.std(axis=1).tolist(),numbers.std().tolist()],
        "max":[numbers.max(axis=0).tolist(),numbers.max(axis=1).tolist(),numbers.max().tolist()],
        "min":[numbers.min(axis=0).tolist(),numbers.min(axis=1).tolist(),numbers.min().tolist()],
        "sum":[numbers.sum(axis=0).tolist(),numbers.sum(axis=1).tolist(),numbers.sum().tolist()]
    }
    return calculations