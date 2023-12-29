## What is the greatest product
## of Y adjacent numbers
## up to X
## in the same direction (up, down, left, right, or diagonally) in the grid (N X N)?
import numpy as np
from itertools import zip_longest

Y = 4
X = 99
N = 20

GREATEST_PRODUCT_VERTICAL = 0
GREATEST_PRODUCT_HORIZONTAL = 0
GREATEST_PRODUCT_DIAGONAL = 0

path_to_board = '/Users/aaronestes/projects/project_euler/11/board.txt'

def massage_data(f_read_split: list):
    board = []
    row = []
    for num in f_read_split:
        if len(row) < N - 1:
            row.append(num)
        elif len(row) == N - 1:
            l = num.split('\n')
            last_num_curr_row = l[0]
            row.append(last_num_curr_row)
            board.append(row)
            row = []
            if len(l) == 2:
                first_num_next_row = l[1]
                row.append(first_num_next_row)
    return board

def find_prod(l: list):
    p = np.prod(l)
    return p


def find_greatest_product_horizontal(board) -> int:
    greatest_product = 0
    for row in board:
        # print(f'row: {row}')
        tmp_list = []
        # print(f'tmp list {tmp_list}')
        for num in row:
            # print(f'int num {int(num)}')
            if len(tmp_list) < 4:
                tmp_list.append(int(num))
            else:
                ## reduce to get product
                prod = np.prod(tmp_list)
                if prod > greatest_product:
                    # print(f'new greatest product {prod}')
                    greatest_product = prod
                ## keep scanning the row left to right
                ## by forgetting the first element in our list
                ## so that tmp_list is now sized at 3
                tmp_list = tmp_list[1:]
                tmp_list.append(int(num))
                find_prod(tmp_list)
            # print(f'tmp list after doing stuff {tmp_list}')
    return greatest_product


def transpose_board(board):
    return list(map(list, zip(*board)))

def find_greatest_product_vertical(board) -> int:
    ## transpose list of lists!
    ## https://stackoverflow.com/questions/6473679/transpose-list-of-lists
    board_transposed = transpose_board(board)
    greatest_product = 0
    for row in board_transposed:
        # print(f'row: {row}')
        tmp_list = []
        # print(f'tmp list {tmp_list}')
        for num in row:
            # print(f'int num {int(num)}')
            if len(tmp_list) < 4:
                tmp_list.append(int(num))
            else:
                ## reduce to get product
                prod = np.prod(tmp_list)
                if prod > greatest_product:
                    # print(f'new greatest product {prod}')
                    greatest_product = prod
                ## keep scanning the row left to right
                ## by forgetting the first element in our list
                ## so that tmp_list is now sized at 3
                tmp_list = tmp_list[1:]
                tmp_list.append(int(num))
                find_prod(tmp_list)
            # print(f'tmp list after doing stuff {tmp_list}')
    GREATEST_PRODUCT_VERTICAL = greatest_product        
    return greatest_product

def find_greatest_product_diagonal(board) -> int:
    ## we need a better way to do this
    greatest_product = 0
    return greatest_product

def chunk(source, n):
    return zip_longest(*([iter(source)] * n))

def better_way(s):
    ## take a Y x Y chunk out of the board
    ## do all vertical, horizontal, and diagonal products
    ## then move one index to the right until we get to the end of our row
    ## then go to the new row
    ## until no rows left
    return list(chunk(chunk(s.split(" "), Y), Y))
            

def largest_product_in_a_grid():
    f = open(path_to_board, 'r')
    f_read = f.read()
    f_read_split = f_read.split(" ")
    board = massage_data(f_read_split)
    # print(board)

    ## this is good
    # gph = find_greatest_product_horizontal(board)
    # print(gph)

    # ## this is good
    # gpv = find_greatest_product_vertical(board)
    # print(gpv)

    ## TODO idk about this
    # gpd = find_greatest_product_diagonal(board)
    # print(gpd)

    ## TODO better way
    bw = better_way(f_read)
    print(bw)




if __name__ == '__main__':
    largest_product_in_a_grid()