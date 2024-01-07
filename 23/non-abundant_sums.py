## Non-Abundant Sums

## a perfect number is one where the sum of its divisors equals itself
## for example: 28 is a perfect number because 1 + 2 + 4 + 7 + 14 = 28

## a number is called deficient if the sum is less than n
## and abundant if the sum is greater than n

## TODO: find the sum of all the positive integers whcih cannot be written as the sum of two abundant numbers

UPPER_LIMIT = 28123
SMALLESET_ABUNDANT_NUMBER = 12
SMALLEST_NUM_SUM_2_ABUNDANT_SUMS = 24

from time import perf_counter
import math
from functools import lru_cache

@lru_cache(None)
def sum_div(num: int):
    total = 1
    for n in range(2, int(math.sqrt(num) + 1)):
        if num % n == 0:
            total += n
            y = num // n
            if y > n:
                total += y
    return total

def get_abundant_nums() -> list:
    return [num for num in range(1, UPPER_LIMIT+1) if num < sum_div(num)]

def update_nums(all_nums: list, abundant_nums: list) -> list:
    idx = 0
    for num in abundant_nums:
        for n in abundant_nums[idx:]:
            next_num = n + num
            if next_num <= UPPER_LIMIT:
                ## O(1) compared to O(n) before
                all_nums[next_num-1][-1] = False
            else:
                break
        idx += 1
    return [n[0] for n in all_nums if n[-1] == True]

def get_nums_not_written_as_sum_2_abundant_nums(all_nums: list, abundant_nums: list) -> list:
    return sum(update_nums(all_nums, abundant_nums))

def solve():
    all_nums = [[num, True] for idx, num in enumerate([num for num in range(1,UPPER_LIMIT+1)])]
    abundant_nums = get_abundant_nums()
    return get_nums_not_written_as_sum_2_abundant_nums(all_nums, abundant_nums)

if __name__ == '__main__':
    start = perf_counter()
    solution = solve()
    end = perf_counter()
    total = end - start
    print(solution)
    print(f'Program took {total} seconds to compute!')