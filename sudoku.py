def sudoku():
    sudoku = [  [5, 0, 0, 0, 4, 0, 0, 0, 9],
                [0, 2, 0, 0, 1, 0, 6, 8, 0],
                [0, 0, 9, 8, 7, 0, 1, 0, 0],
                [0, 0, 6, 7, 0, 0, 2, 0, 0],
                [0, 9, 0, 3, 5, 4, 0, 6, 0],
                [3, 0, 0, 0, 0, 0, 0, 0, 1],
                [9, 0, 0, 0, 6, 0, 0, 0, 2],
                [0, 1, 4, 0, 3, 0, 0, 5, 7],
                [0, 0, 5, 0, 8, 7, 0, 0, 0] ]
    return sudoku

# Path: sudoku.py
def print_sudoku(sudoku):
    for i in range(9):
        for j in range(9):
            print(sudoku[i][j], end=' ')
        print()

# Path: sudoku.py
def solve_sudoku(sudoku):
    is_valid = True
    # Check if the sudoku is solved
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                break
        else:
            continue
        break
    # Find the first empty cell
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                # Try all numbers from 1 to 9
                for k in range(1, 10):
                    sudoku[i][j] = k
                    if is_valid(sudoku, i, j):
                        if solve_sudoku(sudoku):
                            return True
                sudoku[i][j] = 0
                return False
    return True
