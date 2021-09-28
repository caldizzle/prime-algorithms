import timeit
from sieve_primes_antic import *
from list_primes import *
from sieve_primes import *
from sieve_primes_linear import *

'''Test all the programs with the input number n ranging
from 100,000 to 1,000,000 with step 100,000. For each number
in this interval, record the average time taken by both
algorithms repeated 10 times.'''

def function_wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

def performance_test(num_tests, N, funcs, func_names):
    times = []

    for i in range(0, len(funcs)):
        # Get min time from num_test repetitions of algorithm
        func = function_wrapper(funcs[i], N)
        times.append( (N, func_names[i], timeit.timeit(func, number=num_tests)) )
    #return results
    return times

if __name__ == '__main__':
    num_tests = 1
    # min_N = 10000
    # max_N = 100000
    # step = 10000
    N = 20000000
    #funcs = [list_primes, sieve_primes, sieve_primes_linear]
    #func_names = ["list_primes", "sieve_primes", "sieve_primes_linear"]
    funcs = [sieve_primes_linear, sieve_primes]
    func_names = ["sieve_primes_linear", sieve_primes]
    times = performance_test(num_tests, N, funcs, func_names)
    for time in times:
        print(str(time))
    for time in times:
        print(str(time[2]))
