def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

def expo(a,b):
    return a ** b

operations = {
    1: ("+", add),
    2: ("-", sub),
    3: ("*", mul),
    4: ("/", div),
    5: ("^", expo)
}

print("Please select operation -")
print("1) Addition")
print("2) Subtraction")
print("3) Multiplication")
print("4) Division")
print("5) Exponentiation")

try:
    sel = int(input("Select operation (1-5): "))
    n1 = float(input("First number: "))
    n2 = float(input("Second number: "))

    if sel in operations:
        symbol, func = operations[sel]
        result = func(n1, n2)
        print(f"{n1} {symbol} {n2} = {result}")
    else:
        print("Invalid operation selected.")

except ValueError:
    print("Invalid number input.")
