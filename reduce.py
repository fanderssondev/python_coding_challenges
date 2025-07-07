from functools import reduce

# import operator

# Given a non empty list as input, multiply them together and return the result


def grow(num_list: list[int]) -> int:
    return reduce(lambda x, y: x * y, num_list)


print(grow([1, 2, 3]), 6)
print(grow([4, 1, 1, 1, 4]), 16)
print(grow([2, 2, 2, 2, 2, 2]), 64)
