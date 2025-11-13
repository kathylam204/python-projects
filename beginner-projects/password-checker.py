import re

rules = [
    (lambda p: len(p) > 8, "Password must be longer than 8 characters."),
    (lambda p: re.search(r"[a-z]", p), "Must include a lowercase letter."),
    (lambda p: re.search(r"[A-Z]", p), "Must include an uppercase letter."),
    (lambda p: re.search(r"[0-9]", p), "Must include a number."),
    (lambda p: re.search(r"[_@$!.]", p), "Must include a special character (_, @, $, !, .)."),
    (lambda p: not re.search(r"\s", p), "Cannot contain spaces."),
]

password = input("Enter password: ")

valid = True
for check, message in rules:
    if not check(password):
        print("X", message)
        valid = False

if valid:
    print("Valid Password!")
