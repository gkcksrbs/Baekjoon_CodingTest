import sys

def check_R(r, num):
    if num in sudoku[r]:
        return False
    else:
        return True

def check_C(c, num):
    for i in range(9):
        if num == sudoku[i][c]:
            return False
    return True

def check_Box(r, c, num):
    br = r//3*3
    bc = c//3*3

    for i in range(3):
        for j in range(3):
            if num == sudoku[br+i][bc+j]:
                return False
    return True

def Sudoku(index):
    if index == len(zeros):
        for i in sudoku:
            for j in i:
                print(j, end=" ")
            print()
        sys.exit(0)

    else:
        for i in range(1, 10):
            row = zeros[index][0]
            col = zeros[index][1]

            if check_Box(row, col, i) and check_C(col, i) and check_R(row, i):
                sudoku[row][col] = i
                Sudoku(index+1)
                sudoku[row][col] = 0

sudoku = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
zeros = [(i, j) for i in range(9) for j in range(9) if sudoku[i][j] == 0]
Sudoku(0)



