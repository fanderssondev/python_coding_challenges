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


# Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.
#
# Examples:
#
# pig_it('Pig latin is cool') --> igPay atinlay siay oolcay
# pig_it('Hello world !')     --> elloHay orldway !


def pig_it(text: str) -> str:
    lst: list[str] = []
    for word in text.split(" "):
        if word.isalpha():
            lst.append(word[1:] + word[0] + "ay")
        else:
            lst.append(word)
    return " ".join(lst)


check_result(pig_it("Pig latin is cool"), "igPay atinlay siay oolcay")
check_result(pig_it("This is my string"), "hisTay siay ymay tringsay")
check_result(
    pig_it("Quis custodiet ipsos custodes ?"), "uisQay ustodietcay psosiay ustodescay ?"
)
check_result(pig_it("This is my string"), "hisTay siay ymay tringsay")
