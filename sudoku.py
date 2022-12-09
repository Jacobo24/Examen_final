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

def print_sudoku(su):
    for i in range(len(su)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(su[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(su[i][j])
            else:
                print(str(su[i][j]) + " ", end="")


def find_empty(su):
    for i in range(len(su)):
        for j in range(len(su[0])):
            if su[i][j] == 0:
                return (i, j)  # row, col

    return None

def valid(su, num, pos):
    # Check row
    for i in range(len(su[0])):
        if su[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(su)):
        if su[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if su[i][j] == num and (i,j) != pos:
                return False

    return True

def solve(su):
    find = find_empty(su)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(su, i, (row, col)):
            su[row][col] = i

            if solve(su):
                return True

            su[row][col] = 0

    return False

print_sudoku(sudoku)
solve(sudoku)
print("____________________")
print_sudoku(sudoku)