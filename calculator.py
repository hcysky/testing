# Define the add function
def add(x, y):
    return x + y

# Define the subtract function
def subtract(x, y):
    return x - y

# Define the multiply function
def multiply(x, y):
    return x * y

# Define the divide function
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

# Define the calculate function
def calculate(operation, num1, num2):
    if operation == 'add':
        return add(num1, num2)
    elif operation == 'subtract':
        return subtract(num1, num2)
    elif operation == 'multiply':
        return multiply(num1, num2)
    elif operation == 'divide':
        return divide(num1, num2)
    else:
        return "Invalid operation"

# Example usage
if __name__ == "__main__":
    operation = 'add'  # Example operation
    num1 = 10  # Example number 1
    num2 = 5   # Example number 2
    result = calculate(operation, num1, num2)
    print(f"Result: {result}")