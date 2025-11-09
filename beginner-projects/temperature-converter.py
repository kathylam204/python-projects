choice = input("Type C to convert from Celsius or F to convert from Fahrenheit: ").strip().upper()

if choice == 'C':
    c = float(input("Enter temperature in Celsius: "))
    f = (c * 1.8) + 32
    print(f"{c}°C is equal to {f:.2f}°F")

elif choice == 'F':
    f = float(input("Enter temperature in Fahrenheit: "))
    c = (f - 32) / 1.8
    print(f"{f}°F is equal to {c:.2f}°C")

else:
    print("Invalid. Please type C or F.")
