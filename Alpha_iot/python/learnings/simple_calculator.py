# This is a simple calculator program
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y


def main():
    operations = ['+', '-', '*', '/']  # List of valid operators
    arr = []
    arrayOfOperands = []
    arrayOfOperators = []
    while True:
        # try:
            expression = input("Expression (number operator number): ")  # Prompt the user for an expression
            array = expression.split(" ")
            for i in array:
                if i in operations:
                    arrayOfOperators.append(i)
                else:
                    arrayOfOperands.append(i)
            if arrayOfOperators[0] == '+':
                add(float(arrayOfOperands[0]), float(arrayOfOperands[1]))
                (arrayOfOperands[0]).pop()
            elif arrayOfOperators[0] == '-':
                subtract(float(arrayOfOperands[0]), float(arrayOfOperands[1]))
                (arrayOfOperands[0]).pop()
            elif arrayOfOperators[0] == '*':
                multiply(float(arrayOfOperands[0]), float(arrayOfOperands[1]))
                (arrayOfOperands[0]).pop()
            elif arrayOfOperators[0] == '/':
                divide(float(arrayOfOperands[0]), float(arrayOfOperands[1]))
                (arrayOfOperands[0]).pop()
            else:
                print("Invalid operator. Please enter a valid operator (+, -, *, /).")
                continue
                  
        #     if len(expression.split(" ")) != 3:  # Check if the expression has three parts
        #         print("Invalid expression. Please enter a valid expression in the format 'number operator number'.")
        #         continue
        #     else:
        #         operand1, operator, operand2 = expression.split(" ")  # Split the expression into operands and operator
        #         operand1 = float(operand1)  # Convert operand1 to float
        #         operand2 = float(operand2)  # Convert operand2 to float
        # except ValueError:
        #     print("Invalid numbers. Please enter valid numeric values.")
        #     continue

        # if operator not in operations:  # Check if the operator is valid
        #     print("Invalid operator. Please enter a valid operator (+, -, *, /).")
        #     continue         

        # if operator == '+':  # Addition
        #     print(operand1 + operand2)
        # elif operator == '-':  # Subtraction
        #     print(operand1 - operand2)
        # elif operator == '*':  # Multiplication
        #     print(operand1 * operand2)
        # elif operator == '/':  # Division
        #     if operand2 == 0:  # Check for division by zero
        #         print("Division by zero is not allowed.")
        #         continue
        #     else:
        #         print(operand1 / operand2)
        # break

main()