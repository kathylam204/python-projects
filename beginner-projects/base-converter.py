def convert_base(number_str, from_base, to_base):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # Convert to decimal
    decimal_num = int(number_str, from_base)

    # Convert from decimal to target base
    if decimal_num == 0:
        return "0"

    result = []
    while decimal_num > 0:
        result.append(digits[decimal_num % to_base])
        decimal_num //= to_base

    return "".join(reversed(result))


def main():
    while True:
        print("\n~ Base Converter ~")
        print("1) Convert a number between bases")
        print("2) Exit")

        choice = input("Enter your choice: ")

        if choice == "2":
            print("Goodbye!")
            break

        if choice == "1":
            number = input("Enter the number: ")
            from_base = int(input("Enter the base you're converting FROM (2–36): "))
            to_base = int(input("Enter the base you're converting TO (2–36): "))

            try:
                result = convert_base(number.upper(), from_base, to_base)
                print(f"\n{number} (base {from_base}) = {result} (base {to_base})")
            except ValueError:
                print("Invalid number for the given base. Try again.")
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
