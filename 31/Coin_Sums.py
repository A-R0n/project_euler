## Coin Sums

## How many different ways can 2 pounds be made using any number of euro coins?

from time import perf_counter
from itertools import product

def solve():
    coin_sums = 0
    what_we_want_to_make = 200
    euro_coins = [1, 2, 5, 10, 20, 50, 100, 200]

    ## we want to sort our coins in reverse because our lowest combo of coins
    ## will occur at the beginning
    ## needs to be at the beginning
    ## so we can break our loop and increment the count
    ## at the beginning
    euro_coins.sort(reverse=True)

    print(f'euro coins {euro_coins}')

    ## we don't need to include coins higher than the total in our calc
    euro_coins = [coin for coin in euro_coins if coin <= what_we_want_to_make]
    print(f'euro coins after that {euro_coins}')
    # return 0

    startingIdx = 0

    for coin in euro_coins:
        if coin == what_we_want_to_make:
            startingIdx += 1
            coin_sums += 1
        else:
            break

    euro_coins = euro_coins[startingIdx:]
    print(f'euro coins starting with the second highest {euro_coins}')

    count = 2

    import time
    while True:

        for items in product(euro_coins, repeat=count):

            total = sum(items)
            if total == what_we_want_to_make:
                print(f'items {items}')
                coin_sums += 1
                # time.sleep(1)
                break
        
        count += 1

        if count == 15:
            return coin_sums
    

if __name__ == '__main__':
    start = perf_counter()
    solution = solve()
    end = perf_counter()
    print(solution)
    total = end - start
    print(f'Program takes {total} seconds to complete!')