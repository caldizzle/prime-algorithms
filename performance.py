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

def performance_test(num_tests, min_len, max_len, step, funcs, func_names):
    times = []

    for i in range(0, len(funcs)):
        for N in range (min_len, max_len+step, step):
            # Get min time from num_test repetitions of algorithm
            func = function_wrapper(funcs[i], N)
            times.append( (func_names[i], timeit.timeit(func, number=num_tests)) )
    #return results
    return times

if __name__ == '__main__':
    num_tests = 10
    min_N = 100000
    max_N = 1000000
    step = 100000
    funcs = [sieve_primes_antic]
    func_names = ["sieve_primes_antic"]
    times = performance_test(num_tests, min_N, max_N, step, funcs, func_names)
    for time in times:
        print(str(time))
