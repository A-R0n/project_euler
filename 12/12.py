## highly divisible triangular number

## What is the value of the first triangle number to have over five hundred divisors?
from time import perf_counter
NUM_DIVISORS_TEST = 500

def get_nth_triangle_num(n):
    nums = []
    for num in range(1, n+1):
        nums.append(num)
    return sum(nums)

def get_num_divisors(nth_triangle_num: int) -> int:
    divisors = []
    nums = range(1, nth_triangle_num+1)
    for n in nums:
        if nth_triangle_num % n == 0:
            compliment = nth_triangle_num // n
            if n > compliment:
                ## weve already done this compution
                ## where current compliment was n
                break
            divisors.append(compliment)
            divisors.append(n)

    return len(list(set(divisors)))

def get_next_triangle_num(running_total: int, n: int):
    return running_total + n

def solve():
    nth = 7
    nth_triangle_num = get_nth_triangle_num(nth)
    num_divisors = get_num_divisors(nth_triangle_num)

    while num_divisors < NUM_DIVISORS_TEST:
        nth += 1
        nth_triangle_num += nth
        num_divisors = get_num_divisors(nth_triangle_num)
    
    return nth_triangle_num

if __name__ == '__main__':
    start = perf_counter()
    solution = solve()
    print(f'{solution} is the first triangle number with over {NUM_DIVISORS_TEST} divisors')
    end = perf_counter()
    total = (end - start)
    print(f'- Program takes {total} seconds to compute...')