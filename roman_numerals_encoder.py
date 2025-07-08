# Create a function taking a positive integer between 1 and 3999 (both included) as its parameter and returning
# a string containing the Roman Numeral representation of that integer.

# Modern Roman numerals are written by expressing each digit separately starting with the leftmost digit and
# skipping any digit with a value of zero. There cannot be more than 3 identical symbols in a row.

# In Roman numerals:
#
# 1990 is rendered: 1000=M + 900=CM + 90=XC; resulting in MCMXC.
# 2008 is written as 2000=MM, 8=VIII; or MMVIII.
# 1666 uses each Roman symbol in descending order: MDCLXVI.


# def solution(n: int) -> str:
#     if n < 1 or n > 3999:
#         raise ValueError("Number must be between 1 and 3999")

#     symbols = {
#         1000: "M",
#         900: "CM",
#         500: "D",
#         400: "CD",
#         100: "C",
#         90: "XC",
#         50: "L",
#         40: "XL",
#         10: "X",
#         9: "IX",
#         5: "V",
#         4: "IV",
#         1: "I",
#     }

#     result = ""
#     for i in symbols:
#         count = n // i
#         result += symbols[i] * count
#         n -= i * count
#         print(f"i, {i}\t count: {count}\t result: {result}")

#     return result


def solution(n: int) -> str:
    if n < 1 or n > 3999:
        raise ValueError("Number must be between 1 and 3999")

    symbols = [
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

    result: list[str] = []
    for key, value in symbols:
        while n >= key:
            input_n = n
            result.append(value)
            n -= key
            # print(f"n: {input_n}\t\tkey: {key}\t\tvalue: {value}\t\tresult: {result}")

    return "".join(result)


# solution(13)

print(solution(1), "I", "solution(1),'I'")
print(solution(4), "IV", "solution(4),'IV'")
print(solution(6), "VI", "solution(6),'VI'")
print(solution(14), "XIV", "solution(14),'XIV")
print(solution(21), "XXI", "solution(21),'XXI'")
print(solution(89), "LXXXIX", "solution(89),'LXXXIX'")
print(solution(91), "XCI", "solution(91),'XCI'")
print(solution(984), "CMLXXXIV", "solution(984),'CMLXXXIV'")
print(solution(1000), "M", "solution(1000), M")
print(solution(1889), "MDCCCLXXXIX", "solution(1889),'MDCCCLXXXIX'")
print(solution(1989), "MCMLXXXIX", "solution(1989),'MCMLXXXIX'")
