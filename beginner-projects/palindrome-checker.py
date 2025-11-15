import re

def is_palindrome_slice(text):
    return text == text[::-1]

def is_palindrome_loop(text):
    length = len(text)
    for i in range(length // 2):
        if text[i] != text[length - 1 - i]:
            return False
    return True

def is_palindrome_cleaned(text):
    cleaned_text = re.sub(r'[^a-zA-Z0-9]', '', text).lower()
    return cleaned_text == cleaned_text[::-1]

def show_result(is_pal):
    if is_pal:
        print("Yes! It's a palindrome.")
    else:
        print("No, it's not a palindrome.")

def main():
    while True:
        print("\n~ Palindrome Checker ~")
        print("1) Check palindrome (simple slice)")
        print("2) Check palindrome (manual loop)")
        print("3) Check palindrome (ignore punctuation & case)")
        print("4) Exit")

        choice = input("Choose an option: ")

        if choice == "4":
            print("Goodbye!")
            break

        text = input("Enter text to check: ")

        if choice == "1":
            show_result(is_palindrome_slice(text))
        elif choice == "2":
            show_result(is_palindrome_loop(text))
        elif choice == "3":
            show_result(is_palindrome_cleaned(text))
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
