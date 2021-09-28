def sieve_primes_antic(n):
    candidates = list(range(2, n + 1))
    primes = []
    while len(candidates) != 0:
        p = candidates[0]
        primes.append(p)
        candidates.remove(p)
        for x in candidates[1:]:
            if x % p == 0:
                candidates.remove(x)
    return primes
