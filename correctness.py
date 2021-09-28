from sieve_primes_antic import *
from list_primes import *
from sieve_primes import *
from sieve_primes_linear import *

def test_function(func, func_name, n):
    p1 = list_primes(n)
    p2 = func(n)
    if p1 == p2:
        print(func_name + " all good for n = " + str(n))
    else:
        print(func_name + " error. Not equal for some n under + " + str(n))


if __name__ == '__main__':
    for n in [99, 103, 200]:
        test_function(sieve_primes_antic, "sieve_primes_antic", n)
        test_function(sieve_primes, "sieve_primes", n)
        test_function(sieve_primes_linear, "sieve_primes_linear", n)
