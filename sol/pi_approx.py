import math

def madhava_leibniz(m):
    res = [None for n in range(m+1)]
    s = 0
    for n in range(0, m+1):
        s += 4 * (-1)**n / (2*n+1)
        res[n] = s
    return res


def get_diff(series):
    return [v - math.pi for v in series]


def ramanujan(m):
    res = [None for n in range(m+1)]
    s = 0
    factor = 2 * math.sqrt(2) / 9801
    for n in range(0, m+1):
        num = math.factorial(4*n) * (1103 + 26390*n)
        den = math.factorial(n)**4 * 396**(4*n) 
        s += factor * num / den
        res[n] = 1/s
    return res