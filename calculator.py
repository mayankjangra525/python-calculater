def calculator(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        try:
            return a / b
        except ZeroDivisionError:
            return "Error: Division by zero is not allowed!"
    else:
        return "Invalid operation! Please use +, -, *, or /"

while True:
    try:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        op = input("Choose the operation (+, -, *, /): ")

        result = calculator(a, b, op)
        print("Result:", result)
    except ValueError:
        print("Invalid number input! Please enter numeric values only.")

    # Ask if user wants to continue
    again = input("Do you want to calculate again? (yes/no): ").strip().lower()
    if again != "yes":
        print("Goodbye! 👋")
        break
