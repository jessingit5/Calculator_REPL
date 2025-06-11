# calculator/main.py

import sys

def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Returns the difference of two numbers."""
    return a - b

def multiply(a, b):
    """Returns the product of two numbers."""
    return a * b

def divide(a, b):
    """
    Returns the division of two numbers.
    Raises a ValueError if the divisor is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

OPERATIONS = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def get_operation(prompt_func=input):
    """
    Prompts the user to select an operation and validates it.
    Loops until a valid operation is entered.
    """
    while True:
        print("Available operations: " + " ".join(OPERATIONS.keys()))
        op_symbol = prompt_func("Select an operation: ")
        if op_symbol in OPERATIONS:
            return op_symbol
        print(f"Invalid operation '{op_symbol}'. Please try again.")

def get_number(prompt, prompt_func=input):
    """
    Prompts the user for a number and validates it.
    Loops until a valid float is entered.
    """
    while True:
        try:
            return float(prompt_func(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def run_calculator_repl(prompt_func=input, output_func=print):
   
    output_func("Welcome to the Python Command-Line Calculator!")
    while True:
        try:
            num1 = get_number("Enter the first number: ", prompt_func)
            op_symbol = get_operation(prompt_func)
            num2 = get_number("Enter the second number: ", prompt_func)

            calculation_function = OPERATIONS[op_symbol]
            result = calculation_function(num1, num2)
            output_func(f"Result: {num1} {op_symbol} {num2} = {result}")

        except ValueError as e:
            output_func(f"Error: {e}")
        except (KeyboardInterrupt, EOFError):

            output_func("\nExiting calculator. Goodbye!")*

        while True:
            continue_choice = prompt_func("Do you want to perform another calculation? (y/n): ").lower()
            if continue_choice in ['y', 'n']:
                break
            output_func("Invalid choice. Please enter 'y' or 'n'.")

        if continue_choice == 'n':
            output_func("Exiting calculator. Goodbye!")
            break

def main():
    """Main entry point for the application."""
    run_calculator_repl()

if __name__ == "__main__":
    # This allows the script to be executable
    main()
