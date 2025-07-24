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


# https://www.codewars.com/kata/534e01fbbb17187c7e0000c6/train/python
#
# Your task, is to create a NxN spiral with a given size.
#
# For example, spiral with size 5 should look like this:
#
# 00000
# ....0
# 000.0
# 0...0
# 00000
# and with the size 10:
#
# 0000000000
# .........0
# 00000000.0
# 0......0.0
# 0.0000.0.0
# 0.0..0.0.0
# 0.0....0.0
# 0.000000.0
# 0........0
# 0000000000
# Return value should contain array of arrays, of 0 and 1, with the first row being composed of 1s. For example for given size 5 result should be:
#
# [[1,1,1,1,1],[0,0,0,0,1],[1,1,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
# Because of the edge-cases for tiny spirals, the size will be at least 5.
#
# General rule-of-a-thumb is, that the snake made with '1' cannot touch to itself.


# TODO Not implemented
def spiralize(size: int) -> list[int]:

    return []


# fmt:off
check_result(spiralize(5), [
    [1,1,1,1,1],
    [0,0,0,0,1],
    [1,1,1,0,1],
    [1,0,0,0,1],
    [1,1,1,1,1],
    ])

check_result(spiralize(8), [
    [1,1,1,1,1,1,1,1],
    [0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,0,1],
    [1,0,0,0,0,1,0,1],
    [1,0,1,0,0,1,0,1],
    [1,0,1,1,1,1,0,1],
    [1,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1],
    ])
# fmt: on
