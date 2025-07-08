def check_result[T](func: T, expected_result: T) -> None:
    """
    Compares a the return value of the tested function (func) against an
    expected result and prints the outcome.

    Args:
        func (T): The return value of the function being checked.
        expected_result (T): The expected output of the function (func).

    Returns:
        None: This function prints the result and does not return anything.
    """
    print(f"{"✅" if func == expected_result else "❌"}\t {func}\t {expected_result}")


# If we were to set up a Tic-Tac-Toe game, we would want to know whether the board's current
# state is solved, wouldn't we? Our goal is to create a function that will check that for us!
#
# Assume that the board comes in the form of a 3x3 array, where the value is 0 if a spot is empty,
# 1 if it is an "X", or 2 if it is an "O", like so:
#
# [[0, 0, 1],
#  [0, 1, 2],
#  [2, 1, 0]]
# We want our function to return:
#
# -1 if the board is not yet finished AND no one has won yet (there are empty spots),
# 1 if "X" won,
# 2 if "O" won,
# 0 if it's a cat's game (i.e. a draw).
# You may assume that the board passed in is valid in the context of a game of Tic-Tac-Toe.


type Board = list[list[int]]


def is_solved(board: Board) -> int:
    # fmt: off
    lines = (
        board[0], board[1], board[2],             # rows
        [board[0][0], board[1][0], board[2][0]],  # col 0
        [board[0][1], board[1][1], board[2][1]],  # col 1
        [board[0][2], board[1][2], board[2][2]],  # col 2
        [board[0][0], board[1][1], board[2][2]],  # diag \
        [board[0][2], board[1][1], board[2][0]],  # diag /
    )
    # fmt: on

    for line in lines:
        if line[0] != 0 and all(cell == line[0] for cell in line):
            return line[0]
    if any(0 in row for row in board):
        return -1
    return 0


# def is_solved(board: Board) -> int:
#     for i in range(3):  # check rows and columns
#         if board[i][0] != 0 and board[i][0] == board[i][1] == board[i][2]:
#             return board[i][0]
#         if board[0][i] != 0 and board[0][i] == board[1][i] == board[2][i]:
#             return board[0][i]
#     if board[1][1] != 0:  # check diagonals
#         if board[0][0] == board[1][1] == board[2][2]:
#             return board[1][1]
#         if board[0][2] == board[1][1] == board[2][0]:
#             return board[1][1]
#     if any(0 in row for row in board):  # check for empty cells
#         return -1
#     return 0  # Draw


# fmt: off
board = [
    [0, 0, 1], 
    [0, 1, 2], 
    [2, 1, 0]
    ]
check_result(is_solved(board), -1)  # not finished

board = [
    [1, 1, 1],
    [0, 2, 2],
    [0, 0, 0]
    ]
check_result(is_solved(board), 1)  # 1 wins

board = [
    [2, 1, 2],
    [2, 1, 1],
    [1, 1, 2]
    ]
check_result(is_solved(board), 1)  # 1 wins

board = [
    [2, 1, 2],
    [2, 1, 1],
    [1, 2, 1]
    ]
check_result(is_solved(board), 0)  # Tie

board = [
[2,1,1],
[0,1,1],
[2,2,2]
]
check_result(is_solved(board), 2)  # 2 wins
# fmt: on
