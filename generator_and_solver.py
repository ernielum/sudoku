from random import shuffle


def generate_board(board=None):
    if not board:
        board = [[0 for i in range(9)] for j in range(9)]

    if not find_empty(board):
        return True
    else:
        row, col = find_empty(board)

    number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    shuffle(number_list)

    for num in number_list:
        if valid(board, num, (row, col)):
            board[row][col] = num

            if solve(board):
                remove_numbers(board)
                return board

            board[row][col] = 0

    return False


def get_non_empty_squares(board):
    non_empty_squares = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            non_empty_squares.append((i, j))
    shuffle(non_empty_squares)
    return non_empty_squares


def remove_numbers(board):
    non_empty_squares = get_non_empty_squares(board)
    non_empty_squares_count = len(non_empty_squares)

    # 17 clues is the minimum number of necessary clues to create a unique solution for a Sudoku puzzle
    while non_empty_squares_count >= 17:
        row, col = non_empty_squares.pop()
        non_empty_squares_count -= 1
        board[row][col] = 0

    return

def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("-----------------------")
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    return None


def valid(board, num, pos):
    # check row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # check column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # check section
    section_x = pos[1] // 3
    section_y = pos[0] // 3

    for i in range(section_y * 3, section_y * 3 + 3):
        for j in range(section_x * 3, section_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True


def solve(board):
    # No empty cells means that we have found the solution.

    if not find_empty(board):
        return True
    else:
        row, col = find_empty(board)

    for i in range(1, 10):
        if valid(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False
