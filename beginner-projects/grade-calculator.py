def get_marks():
    marks = []
    n = int(input("How many subjects? "))

    for i in range(n):
        while True:
            try:
                mark = float(input(f"Enter grades for subject {i+1}: "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Grade must be between 0 and 100.")
            except ValueError:
                print("Please enter a valid number.")

    return marks


def calculate_average(marks):
    return sum(marks) / len(marks)


def get_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"


def calculate_grades():
    marks = get_marks()
    avg = calculate_average(marks)
    grade = get_grade(avg)
    print(f"\nAverage: {avg:.2f}")
    print(f"Your Grade is: {grade}")


def main():
    actions = {
        "1": calculate_grades,
    }

    while True:
        print("\n~Grade Calculator~")
        print("1) Enter grades and get your average.")
        print("2) Exit")

        choice = input("Enter your choice: ")

        if choice == "2":
            print("Goodbye!")
            break

        if choice in actions:
            actions[choice]()
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
