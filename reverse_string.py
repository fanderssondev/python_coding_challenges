# def solution(string: str) -> str:
#     reversed: str = ""
#     print(f"Input length {len(string)}")
#     for c in range(len(string) - 1, -1, -1):
#         print(f"Index {c}")
#         reversed += string[c]
#     return reversed


def solution(string: str) -> str:
    if len(string) <= 1:
        return string

    return solution(string[1:]) + string[0]


print(solution("Hello"), "olleH")
print(solution("Hello World"), "dlroW olleH")
