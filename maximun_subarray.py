def check_result(func, func_args, expected_result):
    func_res = func(func_args)
    output = "✅" if func_res == expected_result else "❌"
    print(output, "\t", func_res, "\t", expected_result)


# The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers:
# max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# should be 6: [4, -1, 2, 1]
#
# Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array.
# If the list is made up of only negative numbers, return 0 instead.

# Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarray.


# def max_sequence(arr: list[int]) -> int:
#     current, max = 0, 0
#     for num in arr:
#         if current + num < 0:
#             current = 0
#         else:
#             current += num
#             if current > max:
#                 max = current
#     return max


def max_sequence(arr: list[int]) -> int:
    current, max = 0, 0
    for num in arr:
        current += num
        if current < 0:
            current = 0
        if current > max:
            max = current
    return max


check_result(max_sequence, [], 0)
check_result(max_sequence, [-2, 1, -3, 4, -1, 2, 1, -5, 4], 6)
check_result(max_sequence, [-2, -1, -3, -4, -1, -2, -1, -5, -4], 0)
check_result(
    max_sequence,
    [7, 4, 11, -11, 39, 36, 10, -6, 37, -10, -32, 44, -26, -34, 43, 43],
    155,
)
