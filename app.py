from datetime import datetime

board_m = [
    [6, 0, 5, 2, 0, 0, 7, 0, 8],
    [0, 0, 0, 0, 0, 8, 0, 9, 0],
    [0, 1, 8, 0, 0, 0, 2, 0, 0],
    [0, 6, 1, 0, 0, 7, 9, 5, 0],
    [0, 0, 0, 1, 0, 5, 0, 0, 6],
    [5, 3, 0, 6, 0, 2, 0, 0, 0],
    [0, 0, 0, 5, 2, 0, 0, 7, 0],
    [0, 5, 0, 7, 0, 4, 0, 6, 2],
    [0, 7, 0, 9, 6, 3, 0, 0, 4],
]

board_m_ready = [
    [6, 4, 5, 2, 1, 9, 7, 3, 8],
    [7, 2, 3, 4, 5, 8, 6, 9, 1],
    [9, 1, 8, 3, 7, 6, 2, 4, 5],
    [2, 6, 1, 8, 4, 7, 9, 5, 3],
    [8, 9, 7, 1, 3, 5, 4, 2, 6],
    [5, 3, 4, 6, 9, 2, 8, 1, 7],
    [4, 8, 6, 5, 2, 1, 3, 7, 9],
    [3, 5, 9, 7, 8, 4, 1, 6, 2],
    [1, 7, 2, 9, 6, 3, 5, 8, 4],
]


board_x = [
    [4, 0, 0, 5, 0, 0, 0, 0, 0],
    [1, 0, 3, 0, 6, 4, 0, 0, 2],
    [0, 0, 0, 0, 0, 0, 0, 6, 8],
    [0, 0, 4, 9, 0, 0, 1, 0, 5],
    [0, 0, 0, 0, 0, 1, 0, 8, 9],
    [0, 0, 9, 3, 0, 8, 2, 0, 0],
    [0, 7, 0, 0, 0, 0, 0, 2, 0],
    [0, 3, 0, 0, 9, 0, 6, 0, 4],
    [2, 0, 0, 0, 0, 0, 0, 0, 0],
]

board_x_ready = [
    [4, 6, 8, 5, 7, 2, 9, 3, 1],
    [1, 9, 3, 8, 6, 4, 7, 5, 2],
    [5, 2, 7, 1, 3, 9, 4, 6, 8],
    [3, 8, 4, 9, 2, 6, 1, 7, 5],
    [6, 5, 2, 7, 4, 1, 3, 8, 9],
    [7, 1, 9, 3, 5, 8, 2, 4, 6],
    [9, 7, 6, 4, 1, 5, 8, 2, 3],
    [8, 3, 5, 2, 9, 7, 6, 1, 4],
    [2, 4, 1, 6, 8, 3, 5, 9, 7],
]

test_board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]


def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print('- - - - - - - - - - - - - - - -')
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(' | ', end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]), " ", end="")


def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)  # row col
    return None


def validate(board, number, coordinates):
    # row
    for i in range(len(board[0])):
        if board[coordinates[0]][i] == number and coordinates[1] != i:
            return False

    # column
    for i in range(len(board)):
        if board[i][coordinates[1]] == number and coordinates[0] != i:
            return False

    # square
    square_x = coordinates[1] // 3
    square_y = coordinates[0] // 3
    for i in range(square_y * 3, square_y * 3 + 3):
        for j in range(square_x * 3, square_x * 3 + 3):
            if board[i][j] == number and (i, j) != coordinates:
                return False

    return True


def solve(board):
    coordinates = find_empty(board)
    if not coordinates:
        return True
    else:
        row, col = coordinates

    for number in range(1, 10):
        if validate(board, number, (row, col)):
            board[row][col] = number

            if solve(board):
                return True

            board[row][col] = 0

    return False


def timer(func):
    now = datetime.now()
    func()
    print(f'Time spent: {now - datetime.now}')


board = test_board

print_board(board)

print(f'Start: {datetime.now()}')
solve(board)
print(f'Finished: {datetime.now()}')
print()
print()
print_board(board)
print(board)
