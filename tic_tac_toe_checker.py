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


# If we were to set up a Tic-Tac-Toe game, we would want to know whether the board's current state is solved, wouldn't we? Our goal is to create a function that will check that for us!
#
# Assume that the board comes in the form of a 3x3 array, where the value is 0 if a spot is empty, 1 if it is an "X", or 2 if it is an "O", like so:
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
    return 100


board = [[0, 0, 1], [0, 1, 2], [2, 1, 0]]
check_result(is_solved(board), -1)

board = [[1, 1, 1], [0, 2, 2], [0, 0, 0]]
check_result(is_solved(board), 1)

board = [[2, 1, 2], [2, 1, 1], [1, 1, 2]]
check_result(is_solved(board), 1)

board = [[2, 1, 2], [2, 1, 1], [1, 2, 1]]
check_result(is_solved(board), 0)
