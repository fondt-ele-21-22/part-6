import math

def shepherd(x0, r, N, n):
    res = [None for k in range(n+1)]
    res[0] = x0
    x = x0
    for k in range(1, n+1):
        # Calcolo il prossimo valore della popolazione
        x = r * x / (1 + (x/N)**2)
        # Lo memorizzo nella lista
        res[k] = x
    return res