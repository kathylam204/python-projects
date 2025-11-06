import random
import string

def generate_password(length=12, use_special_chars=True):
    # Define the character set to use for the password
    characters = string.ascii_letters + string.digits
    if use_special_chars:
        characters += string.punctuation
    
    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Example usage
if __name__ == "__main__":
    password_length = int(input("Enter the desired password length: "))
    password = generate_password(password_length)
    print(f"Your generated password is: {password}")
