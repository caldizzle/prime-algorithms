def sieve_primes(n):
    candidates = list(range(0, n+1))
    primes = []
    for i in range(2, n+1):
        if candidates[i] > 0:
            p = candidates[i]
            primes.append(p)
            for m in range(2*p, n+1, p):
                candidates[m] = 0
    return primes
