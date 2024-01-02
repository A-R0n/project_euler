## Longest Collatz Sequence

## if the number is odd, multiply by 3 then add 1
## if the number is even, divide by 2
## For example, if we start with 13
## the sequence is: 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

## Although it has not been proved yet,
## it is thought that all starting numbers finish at 1

## Which starting number, under one million, produces the longest chain?

from time import perf_counter

LONGEST_COLLATZ_SEQUENCE = {}

def get_length_of_chain(startingNum: int):
    chain = []
    chain.append(startingNum)
    while chain[-1] != 1:
        if chain[-1] % 2 != 0:
            next_num = chain[-1] * 3 + 1
            chain.append(next_num)
        else:
            next_num = chain[-1] // 2
            chain.append(next_num)
    LONGEST_COLLATZ_SEQUENCE[str(startingNum)] = len(chain)
    return len(chain)


def solve():
    max_chain = max([get_length_of_chain(n) for n in range(1,1000000)])
    print(f'max chain {max_chain}')
    num_with_max_chain = {i for i in LONGEST_COLLATZ_SEQUENCE if LONGEST_COLLATZ_SEQUENCE[i]==max_chain}
    print(f'num with max chain {num_with_max_chain}')
    return num_with_max_chain

if __name__ == '__main__':
    start = perf_counter()
    len_of_chain = solve()
    end = perf_counter()
    total_time = end - start
    print(f'program took {total_time} seconds to compute')
