# Write a function that takes in a string of one or more words,
# and returns the same string, but with all words that have five
# or more letters reversed (Just like the name of this Kata).
# Strings passed in will consist of only letters and spaces.
# Spaces will be included only when more than one word is present.


def spin_words(sentence: str) -> str:
    output = sentence.split(" ")

    for i, word in enumerate(output):
        if len(word) >= 5:
            output[i] = word[::-1]

    return " ".join(output)


def reverse(string: str) -> str:
    if len(string) <= 1:
        return string
    return reverse(string[1:]) + string[0]


print(spin_words("Welcome"), "emocleW")
print(spin_words("to"), "to")
print(spin_words("CodeWars"), "sraWedoC")
print(spin_words("Hey fellow warriors"), "Hey wollef sroirraw")
print(spin_words("This sentence is a sentence"), "This ecnetnes is a ecnetnes")
