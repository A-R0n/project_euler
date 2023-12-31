## Amicable Numbers

## Evaluate the sum of all amicable numbers under 10000
from time import perf_counter
import math
NUM = 10000

def get_divisors(num: int) -> list:
    return [n for n in range(1, (num//2) + 1) if num % n == 0]

def create_divisors_dict(n: int) -> dict:
    return {str(num): get_divisors(num) for num in range(2, n+1)}

def sum_values_in_lists(d: dict) -> dict:
    return {str(val): sum(d[str(val)]) for val in d}

def is_amicable_pair(divisors_dict_sums: dict, num1: str) -> bool:
    num1_sum = divisors_dict_sums[str(num1)]
    num2_sum = divisors_dict_sums[str(num1_sum)]
    if num2_sum == int(num1):
        return True
    return False

def is_sum_not_itself(divisors_dict_sums: dict, num: str) -> bool:
    num_sum = divisors_dict_sums[str(num)]
    if int(num) != int(num_sum):
        return True
    return False

def is_nonprime_sum_in_dict(divisors_dict_sums: dict, num: str) -> bool:
    num_sum = divisors_dict_sums[str(num)]
    if 2 <= int(num_sum) <= NUM:
        return True
    return False

def parse_dict(divisors_dict_sums: dict, num: str) -> int:
    if is_nonprime_sum_in_dict(divisors_dict_sums, num):
        if is_sum_not_itself(divisors_dict_sums, num):
            if is_amicable_pair(divisors_dict_sums, num):
                return divisors_dict_sums[str(num)]
            return 0
        return 0
    return 0

def solve(n: int):
    divisors_dict = create_divisors_dict(n)
    divisors_dict_sums = sum_values_in_lists(divisors_dict)
    return sum([parse_dict(divisors_dict_sums, num) for num in divisors_dict_sums])

if __name__ == '__main__':
    start = perf_counter()
    solution = solve(NUM)
    print(solution)
    end = perf_counter()
    total_seconds = end - start
    print(f'Program takes {total_seconds} seconds to complete!')