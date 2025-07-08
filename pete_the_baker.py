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


# Pete likes to bake some cakes. He has some recipes and ingredients. Unfortunately he is not good in maths.
# Can you help him to find out, how many cakes he could bake considering his recipes?
#
# Write a function cakes(), which takes the recipe (object) and the available ingredients (also an object)
# and returns the maximum number of cakes Pete can bake (integer). For simplicity there are no units for the
# amounts (e.g. 1 lb of flour or 200 g of sugar are simply 1 or 200). Ingredients that are not present in the objects,
# can be considered as 0.
#
# Examples:
#
# must return 2
# cakes({flour: 500, sugar: 200, eggs: 1}, {flour: 1200, sugar: 1200, eggs: 5, milk: 200})
#
# must return 0
# cakes({apples: 3, flour: 300, sugar: 150, milk: 100, oil: 100}, {sugar: 500, flour: 2000, milk: 2000})


# def cakes(recipe: dict[str, int], available: dict[str, int]) -> int:
#     cakes = 1000
#     for key, value in recipe.items():
#         if key in available:
#             cakes = min(available[key] // value, cakes)
#         else:
#             return 0
#     return cakes


def cakes(recipe: dict[str, int], available: dict[str, int]) -> int:
    return min(available.get(key, 0) // recipe[key] for key in recipe)


recipe = {"flour": 500, "sugar": 200, "eggs": 1}
available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
check_result(cakes(recipe, available), 2)

recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
available = {"sugar": 500, "flour": 2000, "milk": 2000}
check_result(cakes(recipe, available), 0)
