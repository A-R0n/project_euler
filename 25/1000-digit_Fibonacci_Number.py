## What is the index of the first Fibonacci number
## to contain 1000 digits

from time import perf_counter

def solve():
    N = 1000
    fib_nums = [0,1]
    last_fib_num = fib_nums[-1]

    while len(str(last_fib_num)) < N:
        last_fib_num = sum([fib_nums[-2], last_fib_num])
        fib_nums.append(last_fib_num)

    return len(fib_nums) - 1

if __name__ == '__main__':
    start = perf_counter()
    solution = solve()
    end = perf_counter()
    print(solution)
    total = end - start
    print(f'Program takes {total} time to complete!')