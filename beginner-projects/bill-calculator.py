bill = float(input("What was the total bill? $"))
tip_percent = int(input("What percentage tip would you like to give? "))
num_people = int(input("How many people to split the bill? "))

calculate_bill = bill * (1 + tip_percent / 100) / num_people
final_amount = f"{calculate_bill:.2f}"

print(f"Each person should pay: ${final_amount}")
