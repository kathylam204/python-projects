def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    
    if mode == 'decrypt':
        shift = -shift

    for char in text:
        if 'a' <= char <= 'z':
            start = ord('a')
            shifted = (ord(char) - start + shift) % 26 + start
            result += chr(shifted)
        elif 'A' <= char <= 'Z':
            start = ord('A')
            shifted = (ord(char) - start + shift) % 26 + start
            result += chr(shifted)
        else:
            result += char

    return result


def main():
    while True:
        print("\n~ Caesar Cipher ~")
        print("1) Encrypt a message")
        print("2) Decrypt a message")
        print("3) Exit")

        choice = input("Choose an option: ")

        if choice == "3":
            print("Goodbye!")
            break

        text = input("Enter your message: ")
        
        # Get shift safely
        while True:
            try:
                shift = int(input("Enter the shift amount (1-25): "))
                if 1 <= shift <= 25:
                    break
                else:
                    print("Shift must be between 1 and 25.")
            except ValueError:
                print("Please enter a number.")

        if choice == "1":
            encrypted = caesar_cipher(text, shift, mode='encrypt')
            print(f"\nEncrypted message: {encrypted}")

        elif choice == "2":
            decrypted = caesar_cipher(text, shift, mode='decrypt')
            print(f"\nDecrypted message: {decrypted}")

        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
