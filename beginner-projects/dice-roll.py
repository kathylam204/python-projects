import random

def roll_dice(num_sides=6):
    """Returns a random roll from 1 to num_sides."""
    return random.randint(1, num_sides)

def get_sides():
    """Get a valid number of sides from the user."""
    while True:
        try:
            num = int(input("Enter number of sides (e.g., 6, 20 ... do not use D6 or D20): "))
            if num > 0:
                return num
            print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Enter a number.")

def main():
    print("Welcome to the Python Dice Roller Simulator!\n")

    while True:
        sides = get_sides()
        result = roll_dice(sides)
        print(f"You rolled a {result} on a {sides}-sided die!")

        if input("Roll again? (y/n): ").lower() != 'y':
            break

    print("\nThanks for rolling!")

if __name__ == "__main__":
    main()
