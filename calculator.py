
import sys

def add(a, b):

    return a + b

def subtract(a, b):

    return a - b

def multiply(a, b):

    return a * b

def divide(a, b):

    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

OPERATIONS = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def get_operation():
    while True:
        print("Available operations: " + " ".join(OPERATIONS.keys()))
        op_symbol = input("Select an operation: ")
        if op_symbol in OPERATIONS:
            return op_symbol
        print(f"Invalid operation '{op_symbol}'. Please try again.")

def get_number(prompt, input=input):
    
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def run_calculator_repl(input=input):
   
    print("Welcome to the Python Command-Line Calculator!")
    while True:
        try:
            num1 = get_number("Enter the first number: ", input)
            op_symbol = get_operation(input)
            num2 = get_number("Enter the second number: ", input)

            calculation_function = OPERATIONS[op_symbol]
            result = calculation_function(num1, num2)
            print(f"Result: {num1} {op_symbol} {num2} = {result}")

        except ValueError as e:
            print(f"Error: {e}")
        except (KeyboardInterrupt, EOFError):

            print("\nExiting calculator. Goodbye!")

        while True:
            continue_choice = input("Do you want to perform another calculation? (y/n): ").lower()
            if continue_choice in ['y', 'n']:
                break
            print("Invalid choice. Please enter 'y' or 'n'.")

        if continue_choice == 'n':
            print("Exiting calculator. Goodbye!")
            break

def main():
    """Main entry point for the application."""
    run_calculator_repl()

if __name__ == "__main__":
    main()
