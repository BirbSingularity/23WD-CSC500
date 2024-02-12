# Ask the user to input two numbers
num1 = float(input("Enter the first number (num1): "))
num2 = float(input("Enter the second number (num2): "))

# Perform addition
numSum = num1 + num2
print("The sum of num1 and num2 is: ", numSum)

# Perform subtraction
difference = num1 - num2
print("The difference between num1 and num2 is: ", difference)

# Ask the user to input two numbers
num1 = float(input("Enter the first number (num1): "))
num2 = float(input("Enter the second number (num2): "))

# Perform multiplication
product = num1 * num2
print("The product of num1 and num2 is: ", product)

# Perform division
if num2 != 0:
    quotient = num1 / num2
    print("The division of num1 by num2 results in: ", quotient)
else:
    print("Division by zero is not allowed.")
