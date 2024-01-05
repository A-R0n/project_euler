## Factorial Digit Sum

## Find the sum of the digits in the number 100!

N = 100

def solve():
    factorial = 1

    for num in reversed(range(1, 100)):
        factorial *= num

    factorial_digit_sum = 0
    for one_digit_num in str(factorial):
        factorial_digit_sum += int(one_digit_num)

    return factorial_digit_sum


if __name__ == '__main__':
    solution = solve()
    print(solution)