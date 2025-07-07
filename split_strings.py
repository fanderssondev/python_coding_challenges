# Complete the solution so that it splits the string into pairs of two characters.
# If the string contains an odd number of characters then it should replace the
# missing second character of the final pair with an underscore ('_').

# check even odd


def solution(s: str) -> list[str]:
    output: list[str] = []

    i = 0
    while i < len(s):
        if i < len(s) - 1:
            output.append(s[i : i + 2])
        elif i < len(s):
            output.append(s[i:] + "_")
        i += 2
    return output


print(solution("asdfadsf"), ["as", "df", "ad", "sf"])
print(solution("asdfads"), ["as", "df", "ad", "s_"])
print(solution(""), [])
print(solution("x"), ["x_"])
