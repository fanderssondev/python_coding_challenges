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


# Some numbers have funny properties. For example:
# 89 --> 8¹ + 9² = 89 * 1
# 695 --> 6² + 9³ + 5⁴= 1390 = 695 * 2
# 46288 --> 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51
#
# Given two positive integers n and p, we want to find a positive integer k,
# if it exists, such that the sum of the digits of n raised to consecutive
# powers starting from p is equal to k * n.
#
# In other words, writing the consecutive digits of n as a, b, c, d ...,
# is there an integer k such that :
#
# ( a^p + b^(p + 1) + c^(p + 2) + d^(p + 3) +... ) = n * k
#
# If it is the case we will return k, if not return -1.
#
# Note: n and p will always be strictly positive integers.
#
# Examples:
# n = 89; p = 1 ---> 1 since 8¹ + 9² = 89 = 89 * 1
# n = 92; p = 1 ---> -1 since there is no k such that 9¹ + 2² equals 92 * k
# n = 695; p = 2 ---> 2 since 6² + 9³ + 5⁴= 1390 = 695 * 2
# n = 46288; p = 3 ---> 51 since 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51


# def dig_pow(n: int, p: int) -> int:
#     num_list: list[int] = [int(d) for d in str(n)]
#     total = 0
#     for i, d in enumerate(num_list):
#         total += d ** (p + i)
#     k = 1
#     while (n * k) <= total:
#         if (n * k) == total:
#             return k
#         k += 1
#     return -1


def dig_pow(n: int, p: int) -> int:
    k: int = -1
    total: int = 0
    for i, d in enumerate(str(n)):
        total += int(d) ** (p + i)
    if total % n == 0:
        k = total // n
    return k


check_result(dig_pow(89, 1), 1)
check_result(dig_pow(92, 1), -1)
check_result(dig_pow(46288, 3), 51)
check_result(dig_pow(41, 5), 25)
check_result(dig_pow(114, 3), 9)
check_result(dig_pow(8, 3), 64)
