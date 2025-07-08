def check_result(func, func_args, expected_result):
    func_res = func(func_args)
    output = "✅" if func_res == expected_result else "❌"
    print(output, func_res, "\t", expected_result)


# You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items.
# We want to create the text that should be displayed next to such an item.
#
# Implement the function which takes an array containing the names of people that like an item.
# It must return the display text as shown in the examples:
#
# []                                -->  "no one likes this"
# ["Peter"]                         -->  "Peter likes this"
# ["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
# ["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
# ["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
#
# Note: For 4 or more names, the number in "and 2 others" simply increases.


# def likes(names: list[str]) -> str:
#     output = f"{"no one" if len(names) == 0 else names[0]}"

#     match len(names):
#         case 2:
#             output += f" and {names[1]}"
#         case 3:
#             output += f", {names[1]} and {names[2]}"
#         case n if n > 3:
#             output += f", {names[1]} and {len(names) -2} others"

#     output += f" like{"s" if len(names) < 2 else ""} this"
#     return output


def likes(names: list[str]) -> str:
    count = len(names)

    templates = {
        0: "no one likes this",
        1: "{} likes this",
        2: "{} and {} like this",
        3: "{}, {} and {} like this",
        4: "{}, {} and {others} others like this",  # `others` needs to be named in order to prevent a `name` from being injected as 3rd value
    }

    return templates[min(4, count)].format(*names[:3], others=count - 2)


check_result(likes, [], "no one likes this")
check_result(likes, ["Peter"], "Peter likes this")
check_result(likes, ["Jacob", "Alex"], "Jacob and Alex like this")
check_result(likes, ["Max", "John", "Mark"], "Max, John and Mark like this")
check_result(
    likes, ["Alex", "Jacob", "Mark", "Max"], "Alex, Jacob and 2 others like this"
)
check_result(
    likes,
    ["Alex", "Jacob", "Mark", "Max", "Thomas", "Anna"],
    "Alex, Jacob and 4 others like this",
)
