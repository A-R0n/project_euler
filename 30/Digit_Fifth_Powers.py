## Digit Fifth Powers

## Find the sum of all the numbers
## that can be written as the sum of fifth powers of their digits

from time import perf_counter
import math
UPPER_L = 194979

def get_digit_scores(nPower: int) -> dict:
    return {str(num):int(math.pow(num, nPower)) for num in range(10)}

def get_upper_bound(nPower: int) -> int:
    ## 295246 is the upper limit
    ## but its a lot higher than our last sum, 194979
    ## can we reduce this somehow?
    return nPower * int(math.pow(9, nPower)) + 1

def digits_are_sum_n_power(num: int, nPower: int) -> bool:
    total = 0
    for n in str(num):
        if total > num:
            return False
        total += math.pow(int(n), nPower)
    if total != num:
        return False
    print(f'total {total} eqauals num')
    return True

def solve():
    n_power = 5
    upper_bound = get_upper_bound(n_power)
    return sum([num for num in range(2, upper_bound + 1) if digits_are_sum_n_power(num, n_power)])

if __name__ == '__main__':
    start = perf_counter()
    solution = solve()
    end = perf_counter()
    print(solution)
    total = end - start
    print(f'Program takes {total} seconds to complete!')