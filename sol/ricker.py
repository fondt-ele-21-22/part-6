import math

def ricker(x0, r, N, n):
    res = [None for k in range(n+1)]
    res[0] = x0
    x = x0
    for k in range(1, n+1):
        # Calcolo il prossimo valore della popolazione
        x = x * math.exp(r * 1 - x/N)
        # Lo memorizzo nella lista
        res[k] = x
    return res