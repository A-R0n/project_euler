## Quadratic Primes

## Find the product of the coefficients, a and b
## for the quadratic expression
## that produces the maximum number of primes for consecutive values of n, starting with n = 0

N_UPPER = 1000
UPPER_BOUND = N_UPPER + 1

import math
from time import perf_counter
from functools import lru_cache

@lru_cache(None)
def is_num_prime(num: int) -> bool:
    num = abs(num)
    for n in range(2, int(math.sqrt(num) + 1)):
        if num % n == 0:
            return False
    return True

def get_prime_nums():
    return [n for n in range(-N_UPPER, N_UPPER+1) if is_num_prime(n)]

def solve():
    max_count_a = None
    max_count_b = None
    max_count = 0
    count = 0
    prime_nums = get_prime_nums()
    for a in prime_nums:
        for b in prime_nums:
            for n in range(N_UPPER+1):
                quad_expression = n*n + (a*n) + b
                if not is_num_prime(quad_expression):
                    count = 0
                    break
                else:
                    count += 1
                if count > max_count:
                    max_count = count
                    max_count_a = a
                    max_count_b = b

    formula = (max_count, max_count_a, max_count_b)
    print(f'n = {max_count}, a: {max_count_a}, b: {max_count_b}')
    return formula[1] * formula[2]

if __name__ == '__main__':
    start = perf_counter()
    solution = solve()
    end = perf_counter()
    print(solution)
    total = end - start
    print(f'Program takes {total} seconds to complete!')