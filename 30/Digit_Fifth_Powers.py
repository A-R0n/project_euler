## Digit Fifth Powers

## Find the sum of all the numbers
## that can be written as the sum of fifth powers of their digits


from time import perf_counter
import math


def get_upper_bound() -> int:
    ## how do we know this is the limit?
    return 194979

def digits_are_sum_n_power(num: int, nPower) -> bool:
    total = 0
    for n in str(num):
        total += math.pow(int(n), nPower)

    if total == num:
        print(f'total {total} eqauals num')
        return True
    return False

def solve():
    n_power = 5
    upper_bound = get_upper_bound()
    return sum([num for num in range(2, upper_bound + 1) if digits_are_sum_n_power(num, n_power)])


if __name__ == '__main__':
    start = perf_counter()
    solution = solve()
    end = perf_counter()
    print(solution)
    total = end - start
    print(f'Program takes {total} seconds to complete!')