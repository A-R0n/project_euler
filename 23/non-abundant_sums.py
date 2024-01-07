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

def get_nums() -> list:
    abundant_nums = []
    for num in range(1, UPPER_LIMIT+1):
        num_sum = sum_div(num)
        if num < num_sum:
            abundant_nums.append(num)
    return abundant_nums

def get_nums_not_written_as_sum_2_abundant_nums(abundant_nums: list) -> list:
    nums = [num for num in range(1,UPPER_LIMIT+1)]
    idx = 0
    for num in abundant_nums:
        for n in abundant_nums[idx:]:
            next_num = n + num
            if next_num <= UPPER_LIMIT:
                if next_num in nums:
                    ## then the non_abundant_number is a sum of two abundant numbers
                    ## so we need to remove it
                    nums.remove(next_num)
            else:
                break
        idx += 1

    return nums


def solve():
    abundant_nums = get_nums()
    nums_not_written_as_sum_2_abundant_nums = get_nums_not_written_as_sum_2_abundant_nums(abundant_nums)
    total_sum = sum(nums_not_written_as_sum_2_abundant_nums)
    return total_sum

if __name__ == '__main__':
    start = perf_counter()
    solution = solve()
    end = perf_counter()
    total = end - start
    print(solution)
    print(f'Program took {total} seconds to compute!')