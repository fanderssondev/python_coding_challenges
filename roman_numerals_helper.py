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


# Write two functions that convert a roman numeral to and from an integer value. Multiple
# roman numeral values will be tested for each function.
#
# Modern Roman numerals are written by expressing each digit separately starting with the
# left most digit and skipping any digit with a value of zero. In Roman numerals:
#
# 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC
# 2008 is written as 2000=MM, 8=VIII; or MMVIII
# 1666 uses each Roman symbol in descending order: MDCLXVI.
# Input range : 1 <= n < 4000
#
# In this kata 4 should be represented as IV, NOT as IIII (the "watchmaker's four").
#
# Examples
# to roman:
# 2000 -> "MM"
# 1666 -> "MDCLXVI"
#   86 -> "LXXXVI"
#    1 -> "I"
#
# from roman:
# "MM"      -> 2000
# "MDCLXVI" -> 1666
# "LXXXVI"  ->   86
# "I"       ->    1
# Help
# +--------+-------+
# | Symbol | Value |
# +--------+-------+
# |    M   |  1000 |
# |   CM   |   900 |
# |    D   |   500 |
# |   CD   |   400 |
# |    C   |   100 |
# |   XC   |    90 |
# |    L   |    50 |
# |   XL   |    40 |
# |    X   |    10 |
# |   IX   |     9 |
# |    V   |     5 |
# |   IV   |     4 |
# |    I   |     1 |
# +--------+-------+


class RomanNumerals:
    roman_map = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]

    @staticmethod
    def to_roman(val: int) -> str:
        result: list[str] = []
        for numeric, symbol in RomanNumerals.roman_map:
            while val >= numeric:
                result.append(symbol)
                val -= numeric
        return "".join(result)

    @staticmethod
    def from_roman(roman_num: str) -> int:
        index, total = 0, 0
        for numeric, symbol in RomanNumerals.roman_map:
            while roman_num[index : index + len(symbol)] == symbol:
                total += numeric
                index += 1
        return total


check_result(RomanNumerals.to_roman(1000), "M")
check_result(RomanNumerals.to_roman(4), "IV")
check_result(RomanNumerals.to_roman(1), "I")
check_result(RomanNumerals.to_roman(1990), "MCMXC")
check_result(RomanNumerals.to_roman(2008), "MMVIII")

check_result(RomanNumerals.from_roman("XXI"), 21)
check_result(RomanNumerals.from_roman("I"), 1)
check_result(RomanNumerals.from_roman("IV"), 4)
check_result(RomanNumerals.from_roman("MMVIII"), 2008)
check_result(RomanNumerals.from_roman("MDCLXVI"), 1666)
