## Lattice Paths

## starting in the top left corner of a 2 x 2 grid
## and only being able to move right and down
## there are exactly 6 different routes to the bottom right corner

## How many such routes are there through a 20 x 20 grid?

from math import factorial, pow
from time import perf_counter

N = 20
M = N

def solve():
    return int(factorial(N * 2) / pow(factorial(N), 2))

if __name__ == '__main__':
    start = perf_counter()
    number_lattice_paths = solve()
    end = perf_counter()
    total = end - start
    print(f'{number_lattice_paths} lattice paths in a {N} by {M} grid!')
    print(f'program takes {total} seconds to complete!')
