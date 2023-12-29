## What is the greatest product
## of Y adjacent numbers
## up to X
## in the same direction (up, down, left, right, or diagonally) in the grid (N X N)?


Y = 4
X = 99
N = 20

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
            

def larget_product_in_a_grid():
    f = open(path_to_board, 'r')
    f_read = f.read()
    f_read_split = f_read.split(" ")
    board = massage_data(f_read_split)
    print(board)

if __name__ == '__main__':
    larget_product_in_a_grid()