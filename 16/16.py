## Power Digit Sum

## 2^15 = 32768
## and the sum of its digits is 3+2+7+6+8 = 26

## What is the sum of the digits of the number 2^1000

from functools import reduce
from time import perf_counter

BASE_NUM = 2
TO_POWER = 1000

def solve():
    ## pow function abbreviates really large numbers with e+
    ## so we have to chop that part off
    ## which is ok - 
    ## the sum of 300 zero's is neglible
    num = pow(BASE_NUM, TO_POWER)
    num_str = str(num)
    num_str_split = "".join(num_str.split('e')[0].split('.'))
    numbers = [int(n) for n in num_str_split]
    return reduce(lambda x, y: x+y, numbers)

if __name__ == '__main__':
    start = perf_counter()
    power_digit_sum = solve()
    end = perf_counter()
    total = end - start
    print(f'{power_digit_sum} is the power digit sum!')
    print(f'program takes {total} seconds to complete!')
