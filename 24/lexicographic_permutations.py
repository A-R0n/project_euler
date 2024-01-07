## A permutation is an ordered arrangement of objects
## for example, 3124 is one possible permutation of 1, 2, 3, and 4
## When all the permutations are listed numerically or alphatically, we call it lexicographic order

## TODO: What is the 1,000,000 lexicographic permutation of 0, 1, 2, 3, 4, 5, 6, 7, 8, and 9

from time import perf_counter
from itertools import permutations

def get_digits() -> list:
    return [num for num in range(0, 10)]

def get_nth_permutation(digits: list, n: int) -> tuple:
    return list(permutations(digits))[n-1]

def format_as_str(sol: tuple) -> str:
    sol_str = ''
    for s in sol:
        sol_str += str(s)
    return sol_str

def solve():
    n = 1000000   
    digits = get_digits()
    sol = get_nth_permutation(digits, n)
    return format_as_str(sol)

if __name__ == '__main__':
    start = perf_counter()
    solution = solve()
    end = perf_counter()
    print(solution)
    total = end - start
    print(f'Program takes {total} time to complete!')