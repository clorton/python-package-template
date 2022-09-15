from functools import lru_cache
from math import pi

@lru_cache()
def fib(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

def __pi():
    return pi
