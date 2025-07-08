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


# https://www.codewars.com/kata/54d512e62a5e54c96200019e/train/python
#
# Given a positive number n > 1 find the prime factor decomposition of n.
# The result will be a string with the following form:
#  "(p1**n1)(p2**n2)...(pk**nk)"
# with the p(i) in increasing order and n(i) empty if n(i) is 1.
#
# Example: n = 86240 should return "(2**5)(5)(7**2)(11)"


def prime_factors(n: int) -> str:
    return str((2**5) * (5) * (7**2) * (11))


check_result(prime_factors(7775460), "(2**2)(3**3)(5)(7)(11**2)(17)")
check_result(prime_factors(7919), "(7919)")
