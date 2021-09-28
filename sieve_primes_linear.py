def sieve_primes_linear(n):
    primes = []
    candidates = [0] * (n+1) #list of n zerosx
    for i in range(2, n+1): # is an index that directly corresponds to a number
        if candidates[i] == 0: # i is prime
            primes.append(i)
            candidates[i] = i # lowest prime factor of i is i
        for p in primes:
            if p * i >= n or p <= candidates[i]:
                break
            else:
                candidates[i * p] = p
        # j = 0
        # while j < len(primes) and primes[j] <= candidates[i]:
        #     if (i * primes[j]) < (n+1):
        #         # primes[j] is the lowest prime factor of this multiple
        #         candidates[i * primes[j]] = primes[j]
        #     j += 1
    return primes
