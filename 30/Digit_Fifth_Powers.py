## Digit Fifth Powers

## Find the sum of all the numbers
## that can be written as the sum of fifth powers of their digits


from time import perf_counter

def get_upper_bound() -> int:
    return 10000

def digits_are_sum_fifth_power(num: int) -> bool:
    return True

def solve():
    upper_bound = get_upper_bound()
    return sum([num for num in range(upper_bound + 1) if digits_are_sum_fifth_power(num)])


if __name__ == '__main__':
    start = perf_counter()
    solution = solve()
    end = perf_counter()
    print(solution)
    total = end - start
    print(f'Program takes {total} seconds to complete!')