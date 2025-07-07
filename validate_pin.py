# ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything
# but exactly 4 digits or exactly 6 digits.
# If the function is passed a valid PIN string, return true, else return false.

import re


def validate_pin(pin: str) -> bool:
    pattern = re.compile(r"^(?:\d{4}|\d{6})\Z")
    return bool(pattern.match(pin))


print(validate_pin("1"), False, "Wrong output for '1'")
print(validate_pin("12"), False, "Wrong output for '12'")
print(validate_pin("123"), False, "Wrong output for '123'")
print(validate_pin("12345"), False, "Wrong output for '12345'")
print(validate_pin("1234567"), False, "Wrong output for '1234567'")
print(validate_pin("-1234"), False, "Wrong output for '-1234'")
print(validate_pin("-12345"), False, "Wrong output for '-12345'")
print(validate_pin("1.234"), False, "Wrong output for '1.234'")
print(validate_pin("00000000"), False, "Wrong output for '00000000'")
print(validate_pin("a234"), False, "Wrong output for 'a234'")
print(validate_pin(".234"), False, "Wrong output for '.234'")
print(validate_pin("1234"), True, "Wrong output for '1234'")
print(validate_pin("0000"), True, "Wrong output for '0000'")
print(validate_pin("1111"), True, "Wrong output for '1111'")
print(validate_pin("123456"), True, "Wrong output for '123456'")
print(validate_pin("098765"), True, "Wrong output for '098765'")
print(validate_pin("000000"), True, "Wrong output for '000000'")
print(validate_pin("123456"), True, "Wrong output for '123456'")
print(validate_pin("090909"), True, "Wrong output for '090909'")
print(validate_pin("090909\n"), False, "Wrong output for '090909'")
