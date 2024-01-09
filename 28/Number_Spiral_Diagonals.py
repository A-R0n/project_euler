## Number Soiral Diagonals

## Find the sum of diagonals


import math
from time import perf_counter
from functools import lru_cache
L = 1001
W = L

def get_right_down_sum():
    return sum([n*n for n in range(1, L+1, 2)])

def get_left_down_sum():
    return sum([n*(n-1)+1 for n in range(1, L+1, 2)])

def get_left_up_sum():
    return sum([n*(n-2)+2 for n in range(1, L+1, 2)])

def get_right_up_sum():
    return sum([n*(n-3)+3 for n in range(1, L+1, 2)])

def create_spiral():
    right_down_sum = get_right_down_sum()
    left_down_sum = get_left_down_sum()
    left_up_sum = get_left_up_sum()
    right_up_sum = get_right_up_sum()
    return sum([right_down_sum, left_down_sum, left_up_sum, right_up_sum]) - 3

def solve():
    return create_spiral()

if __name__ == '__main__':
    start = perf_counter()
    solution = solve()
    end = perf_counter()
    print(solution)
    total = end - start
    print(f'Program takes {total} seconds to complete!')