# You are given an list `strarr` of strings and an integer k.
# Your task is to return the first longest string consisting of k
# consecutive strings taken in the array.

# n being the length of the `strarr`
# if n = 0 or k > n or k <= 0 return ""


def longest_consec(strarr: list[str], k: int) -> str:
    n = len(strarr)
    if n == 0 or k > n or k <= 0:
        return ""

    longest = ""
    for i in range(n - k + 1):
        combined = "".join(strarr[i : i + k])
        if len(combined) > len(longest):
            longest = combined
    return longest


print(
    longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2),
    "abigailtheta",
)
print(
    longest_consec(
        [
            "ejjjjmmtthh",
            "zxxuueeg",
            "aanlljrrrxx",
            "dqqqaaabbb",
            "oocccffuucccjjjkkkjyyyeehh",
        ],
        1,
    ),
    "oocccffuucccjjjkkkjyyyeehh",
)
print(longest_consec([], 3), "")
print(
    longest_consec(
        [
            "itvayloxrp",
            "wkppqsztdkmvcuwvereiupccauycnjutlv",
            "vweqilsfytihvrzlaodfixoyxvyuyvgpck",
        ],
        2,
    ),
    "wkppqsztdkmvcuwvereiupccauycnjutlvvweqilsfytihvrzlaodfixoyxvyuyvgpck",
)
print(
    longest_consec(["wlwsasphmxx", "owiaxujylentrklctozmymu", "wpgozvxxiu"], 2),
    "wlwsasphmxxowiaxujylentrklctozmymu",
)
print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], -2), "")
print(
    longest_consec(["it", "wkppv", "ixoyx", "3452", "zzzzzzzzzzzz"], 3),
    "ixoyx3452zzzzzzzzzzzz",
)
print(longest_consec(["it", "wkppv", "ixoyx", "3452", "zzzzzzzzzzzz"], 15), "")
print(longest_consec(["it", "wkppv", "ixoyx", "3452", "zzzzzzzzzzzz"], 0), "")
