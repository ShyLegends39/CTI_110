# Putting in the user's inputs for the four floating-point numbers
num1 = float(input())
num2 = float(input())
num3 = float(input())
num4 = float(input())

# Calculating the product (a.k.a. your_value_product) of the four floating-point numbers from the user's inputs
your_value_product = num1 * num2 * num3 * num4

# Calculating the average(a.k.a. your_value_avg) of the four floating-point numbers from the user's inputs
your_value_avg = (num1 + num2 + num3 + num4)/4

# Output for results of the user's inputs and string formatting expression helps with conversion specifiers
print(f'{your_value_product:.0f}' ' ' f'{your_value_avg:.0f}'.format(your_value_product, your_value_avg)) # This shows the inputs to round each integers for each floating-point value
print(f'{your_value_product:.3f}' ' ' f'{your_value_avg:.3f}'.format(your_value_product, your_value_avg)) # This shows the inputs that each floating-point value with three digits after the decimal point