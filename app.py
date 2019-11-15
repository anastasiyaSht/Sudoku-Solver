from datetime import datetime


board = [
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


def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print('- - - - - - - - - - - - - - -')
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print('| ', end="")

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


if __name__ == '__main__':
    print_board(board)
    now = datetime.now()
    solve(board)
    print(f'Started at {now}, finished at {datetime.now()}')
    print_board(board)
