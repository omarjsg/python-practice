from random import sample


def shuffle(s):
    return sample(s, len(s))


def pattern(r, c, base, side):
    return (base * (r % base) + r // base + c) % side


def printBoard(board):
    for line in board: print(line)
    print('\n')


def find_empty_location(arr, l, rank):
    for row in range(rank**2):
        for col in range(rank**2):
            if (arr[row][col] == 0):
                l[0] = row
                l[1] = col
                return True
    return False

def used_in_row(arr, row, num, rank):
    for i in range(rank**2):
        if (arr[row][i] == num):
            return True
    return False

def used_in_col(arr, col, num, rank):
    for i in range(rank**2):
        if (arr[i][col] == num):
            return True
    return False

def used_in_box(arr, row, col, num, rank):
    for i in range(rank):
        for j in range(rank):
            if (arr[i + row][j + col] == num):
                return True
    return False

def check_location_is_safe(arr, row, col, num, rank):
    return not used_in_row(arr, row, num, rank) and not used_in_col(arr, col, num, rank) and not used_in_box(arr, row - row % rank,
                    col - col % rank, num, rank)



def solveSuduko(board, rank):
    l = [0, 0]
    if (not find_empty_location(board, l, rank)):
        return True
    row = l[0]
    col = l[1]
    for num in range(1, rank**2 + 1):
        if (check_location_is_safe(board,
                                   row, col, num, rank)):
            board[row][col] = num
            if (solveSuduko(board, rank)):
                return True
            board[row][col] = 0
    return False


if __name__ == '__main__':
    print("Enter the rank of the sudoku puzzle: ")
    rank = int(input())
    solved =False
    side = rank * rank
    rBase = range(rank)
    rows = [g * rank + r for g in shuffle(rBase) for r in shuffle(rBase)]
    cols = [g * rank + c for g in shuffle(rBase) for c in shuffle(rBase)]
    nums = shuffle(range(1, rank * rank + 1))
    board = [[nums[pattern(r, c, rank, side)] for c in cols] for r in rows]
    squares = side * side
    empties = squares * 3 // 4
    for p in sample(range(squares), empties):
        board[p // side][p % side] = 0
    printBoard(board)
    if (solveSuduko(board, rank)):
        printBoard(board)
        print("Sudoku with rank " + rank + "has been solved.")
    else:
        print("Unsolvable.")
