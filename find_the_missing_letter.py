from typing import TypeVar

T = TypeVar("T")


def check_result(func: T, expected_result: T) -> None:
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


# Write a method that takes an array of consecutive (increasing) letters as input and
# that returns the missing letter in the array.

# You will always get an valid array. And it will be always exactly one letter be missing.
# The length of the array will always be at least 2.
# The array will always contain letters in only one case.
#
# Example:
#
# ['a','b','c','d','f'] -> 'e'
# ['O','Q','R','S'] -> 'P'
# (Use the English alphabet with 26 letters!)


# def find_missing_letter(chars: list[str]) -> str:
#     num = 0
#     for i, char in enumerate(chars):
#         if i > 0 and num + 1 != ord(char):
#             return chr(num + 1)
#         num = ord(char)
#     return chr(num)


def find_missing_letter(chars: list[str]) -> str:
    num = 0
    while ord(chars[num]) == ord(chars[num + 1]) - 1:
        num += 1
    return chr(1 + ord(chars[num]))


check_result(find_missing_letter(["a", "b", "c", "d", "f"]), "e")
check_result(find_missing_letter(["O", "Q", "R", "S"]), "P")
check_result(find_missing_letter(["b", "d"]), "c")
