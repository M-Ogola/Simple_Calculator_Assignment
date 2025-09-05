# This is a simple calculator program that takes two numbers and an operator
# from the user and performs the requested calculation.

def calculator():
    """
    Asks the user for two numbers and an arithmetic operation,
    then performs the calculation and prints the result.
    """
    print("Hi! Welcome to My Simple Python Calculator!")

    while True:
        # Get the first number from the user.
        # Use a try-except block to handle non-numeric input.
        try:
            num1_str = input("Enter the first number: ") # User can type 'exit' to quit
            if num1_str.lower() == 'exit':
                print("Peace out! 🤙🏾")
                return # Exit the function to end the program
            num1 = float(num1_str) # Convert input to float
        except ValueError:
            print("Uh Oh! That's an invalid input. Please enter a valid number.") # Prompt user again
            continue

        # Get the second number.
        try:
            num2_str = input("Enter the second number: ")
            if num2_str.lower() == 'exit':
                print("Peace out! 🤙🏾")
                return # Exit the function to end the program
            num2 = float(num2_str) # Convert input to float
        except ValueError:
            print("Uh Oh! That's an invalid input. Please enter a valid number.")
            continue

        # Get the operator.
        operator = input("Enter an operation (+, -, *, /, //): ")

        # Perform the calculation based on the operator.
        result = None # Initialize result variable
        if operator == '+':
            result = num1 + num2 # Perform addition
        elif operator == '-':
            result = num1 - num2 # Perform subtraction
        elif operator == '*':
            result = num1 * num2 # Perform multiplication
        elif operator == '/':
            if num2 == 0:
                print("Error: Cannot divide by zero 😬. Clock that 🫵🏾.") 
                continue
            result = num1 / num2 # Perform division
        elif operator == '//':
            if num2 == 0:
                print("Error: Cannot divide by zero 😬. Clock that 🫵🏾.")
                continue
            result = num1 // num2 # Perform floor division  
        else:
            print(f"Invalid operator '{operator}'. Please use one of the specified operators.")
            continue

        # Print the final result in the requested format.
        print(f"\nResult: {num1} {operator} {num2} = {result}\n")

        # Give the user an option to exit the program.
        another_calculation = input("Do you want to perform another calculation? (yes/no): ").lower()
        if another_calculation != 'yes':
            print("Peace out! 🤙🏾")
            break

# Run the calculator program.
if __name__ == "__main__":
    calculator()
