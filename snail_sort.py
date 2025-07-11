from typing import Literal


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


# https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1/train/python
#
# Given an n x n array, return the array elements arranged from outermost elements to
# the middle element, traveling clockwise.

# array = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
#     ]
#
# snail(array) #=> [1,2,3,6,9,8,7,4,5]
#
# For better understanding, please follow the numbers of the next array consecutively:
#
# array = [
#     [1,2,3],
#     [8,9,4],
#     [7,6,5]
#     ]
# snail(array) #=> [1,2,3,4,5,6,7,8,9]

# NOTE: The idea is not sort the elements from the lowest value to the highest; the idea
# is to traverse the 2-d array in a clockwise snailshell pattern.
#
# NOTE 2: The 0x0 (empty matrix) is represented as en empty array inside an array [[]].


# def snail(snail_map: list[list[int]]) -> list[int]:
#     output: list[int] = []
#     curr_dir = 0
#     right = 0
#     down = 0
#     left = 0
#     up = 1
#     width = len(snail_map[0])
#     total = width * width
#     x, y = 0, 0

#     while total > 0:
#         output.append(snail_map[y][x])
#         total -= 1

#         if x + right == width - 1 and curr_dir == 0:
#             right += 1
#             curr_dir = (curr_dir + 1) % 4
#             y += 1
#         elif y + down == width - 1 and curr_dir == 1:
#             down += 1
#             curr_dir = (curr_dir + 1) % 4
#             x -= 1
#         elif x - left == 0 and curr_dir == 2:
#             left += 1
#             curr_dir = (curr_dir + 1) % 4
#             y -= 1
#         elif y - up == 0 and curr_dir == 3:
#             up += 1
#             curr_dir = (curr_dir + 1) % 4
#             x += 1
#         else:
#             if curr_dir == 0:
#                 x += 1
#             elif curr_dir == 1:
#                 y += 1
#             elif curr_dir == 2:
#                 x -= 1
#             elif curr_dir == 3:
#                 y -= 1

#     return output


def snail(snail_map: list[list[int]]) -> list[int]:
    if snail_map:
        top_row = list(snail_map[0])

        rotated_array = [list(row) for row in zip(*snail_map[1:])]
        rotated_array = rotated_array[::-1]

        return top_row + snail(rotated_array)
    else:
        return []


# fmt: off
array = [
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]
    ]
# fmt: on
expected = [1, 2, 3, 6, 9, 8, 7, 4, 5]
check_result(snail(array), expected)

# fmt:off
array = [
    [1, 2, 3],
    [8, 9, 4],
    [7, 6, 5]
    ]
# fmt: on
expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
check_result(snail(array), expected)

# fmt:off
array = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
    ]
# fmt: on
expected = [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
check_result(snail(array), expected)
