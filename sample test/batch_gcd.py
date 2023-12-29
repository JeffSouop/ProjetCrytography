from math import gcd
from itertools import combinations

def batch_gcd(*args):
    gcds = []
    comb = combinations(args, 2)
    for pair in comb:
        gcds.append(gcd(pair[0], pair[1]))
    return gcds
