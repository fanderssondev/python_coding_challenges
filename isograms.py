# An isogram is a word that has no repeating letters, consecutive or
# non-consecutive. Implement a function that determines whether a string
# that contains only letters is an isogram. Assume the empty string
# is an isogram. Ignore letter case.


# def is_isogram(string: str) -> bool:
# input = string.lower()
# i = 0
# while i < len(input):
#     if input.find(input[i], 0, i) != -1:
#         return False
#     i += 1
# return True


def is_isogram(string: str) -> bool:
    input = string.lower()
    for char in range(len(input)):
        if input.find(input[char], 0, char) != -1:
            return False
    return True


print(is_isogram("Dermatoglyphics"), True)
print(is_isogram("isogram"), True)
print(is_isogram("aba"), False, "same chars may not be adjacent")
print(is_isogram("moOse"), False, "same chars may not be same case")
print(is_isogram("isIsogram"), False)
print(is_isogram(""), True, "an empty string is a valid isogram")
