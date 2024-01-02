## highly divisible triangular number

## What is the value of the first triangle number to have over five hundred divisors?
from time import perf_counter
NUM_DIVISORS_TEST = 100

def get_n_triangle_num(n):
    nums = []
    for num in range(1, n+1):
        nums.append(num)
    return sum(nums)

## i think we need to reverse this?
def get_num_divisors(n_triangle_num: int) -> int:
    divisors = []
    for num in range(1, n_triangle_num+1):
        if n_triangle_num % num == 0:
            # print(num)
            divisors.append(num)
    return len(divisors)

def solve():
    n = 7
    n_triangle_num = get_n_triangle_num(n)
    num_divisors = get_num_divisors(n_triangle_num)

    while num_divisors < NUM_DIVISORS_TEST:
        n += 1
        n_triangle_num += n
        num_divisors = get_num_divisors(n_triangle_num)
    
    print(n_triangle_num)
    return n_triangle_num

if __name__ == '__main__':
    start = perf_counter()
    solve()
    end = perf_counter()
    total = (end - start)/60
    print(f'total time : {total} minutes!')