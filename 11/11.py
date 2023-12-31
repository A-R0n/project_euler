## What is the greatest product
## of Y adjacent numbers
## up to X
## in the same direction (up, down, left, right, or diagonally) in the grid (N X N)?
import numpy as np

Y = 4
X = 99
N = 20

GREATEST_PRODUCT_VERTICAL = 0
GREATEST_PRODUCT_HORIZONTAL = 0
GREATEST_PRODUCT_DIAGONAL = 0

path_to_board = '/Users/aaronestes/projects/project_euler/11/board.txt'


def find_prod(l: list):
    p = np.prod(l)
    return p

def transpose_board(board):
    return list(map(list, zip(*board)))

def get_max_row_prod(matrix: np.array) -> int:
    max_row_prod = 0
    for r in matrix:
        prod = find_prod(r)
        if prod > max_row_prod:
            max_row_prod = prod
    return max_row_prod

def get_max_col_prod(matrix: np.array) -> int:
    max_col_prod = 0
    for r in np.transpose(matrix):
        prod = find_prod(r)
        if prod > max_col_prod:
            max_col_prod = prod
    return max_col_prod

def get_max_diag_prod(matrix: np.array):
    diag_left_right = find_prod(matrix.diagonal())
    diag_right_left = find_prod(np.rot90(matrix).diagonal())
    return max(diag_left_right, diag_right_left)

def find_max_matrix_product(matrix: np.array) -> int:
    max_row_prod = get_max_row_prod(matrix)
    print(f'max_row_prod {max_row_prod}')
    max_col_prod = get_max_col_prod(matrix)
    print(f'max_col_prod {max_col_prod}')
    max_diag_prod = get_max_diag_prod(matrix)
    print(f'max_diag_prod {max_diag_prod}')
    return max(max_row_prod, max_col_prod, max_diag_prod)

def better_way(myS):
    ## take a Y x Y chunk out of the board
    ## do all vertical, horizontal, and diagonal products
    ## then move one index to the right until we get to the end of our row
    ## then go to the new row by returning to the first column and decrementing the row by 1
    ## until no rows left
    myL = myS.split()
    myVector = []
    myRow = []
    count = 0
    rowNum = 1
    for num in myL:
        count += 1
        if rowNum == Y + 1:
            break
        if count <= 4:
            myRow.append(int(num))
        if len(myRow) == 4:
            myVector.append(myRow)
            myRow = []
        if count == N:
            count = 0
            rowNum += 1

    myMatrix = np.array(myVector)
    print(f'myMatrix: {myMatrix}')
    ## this is the max of our first matrix
    ## but we need to find the max of the max
    ## aka: the max of all the matrices
    return find_max_matrix_product(myMatrix)
            

def largest_product_in_a_grid():
    f = open(path_to_board, 'r')
    f_read = f.read()
    bw = better_way(f_read)
    print(bw)

if __name__ == '__main__':
    largest_product_in_a_grid()