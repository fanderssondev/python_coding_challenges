# A Narcissistic Number (or Armstrong Number) is a positive number which
# is the sum of its own digits, each raised to the power of the number of
# digits in a given base. In this Kata, we will restrict ourselves to decimal (base 10).

# 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153


# def narcissistic(value: int) -> bool:
#     digits = [int(d) for d in str(value)]
#     total = 0
#     for d in digits:
#         total += d ** len(digits)
#     return total == value


def narcissistic(value: int) -> bool:
    number = value
    total = 0
    digits: list[int] = []
    while number > 0:
        digits.append(number % 10)
        number //= 10
    digits.reverse()
    for d in digits:
        total += d ** len(digits)
    return total == value


print(narcissistic(7), True)
print(narcissistic(371), True)
print(narcissistic(122), False)
print(narcissistic(4887), False)
