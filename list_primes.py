import math

def has_divisors2(n):
    for i in range(2, math.ceil(math.sqrt(n)) + 1):
        if n % i == 0:
            return True
    return False

def list_primes(n):
    primes = [2] # add 2 because has_divisors2 only works for numbers ≥ 3
    for m in range(3, n + 1):
        if not has_divisors2(m):
            primes.append(m)
    return primes
